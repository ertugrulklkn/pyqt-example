import sys

from PySide2.QtCore import QThreadPool
from PySide2.QtGui import QTextCursor
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox
from serial.tools.list_ports import comports

from com import Com, ComException
from ui.ui_mainwindow import Ui_MainWindow
from worker import Worker


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Time&Led")

        self.available_ports = comports()
        self.com_port = Com()

        self.threadPool = QThreadPool()

        for port, desc, hwid in self.available_ports:
            self.selectComPortComboBox.addItem(f"{port}")

        self.ledButtonOn.setDisabled(True)
        self.ledButtonOff.setDisabled(True)
        self.sendTimeButton.setDisabled(True)
        self.textEdit.moveCursor(QTextCursor.End)

        self.comConnectButton.clicked.connect(lambda: self.bindComPort(self.selectComPortComboBox.currentText()))
        self.ledButtonOn.clicked.connect(lambda: self.com_port.sendLedCommand(light=True))
        self.ledButtonOff.clicked.connect(lambda: self.com_port.sendLedCommand(light=False))
        self.sendTimeButton.clicked.connect(self.sendTime)

        self.show()

    def bindComPort(self, port):
        try:
            self.com_port.start(port, 115200)
        except ComException as e:
            msg = QMessageBox(self)
            msg.setWindowTitle("Error")
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.setText("Serial Port Error")
            msg.setDetailedText(str(e))
            msg.exec_()
        else:
            self.selectComPortComboBox.setDisabled(True)
            self.comConnectButton.clicked.connect(self.unbindComPort)
            self.comConnectButton.setText("Disconnect")
            self.ledButtonOn.setEnabled(True)
            self.ledButtonOff.setEnabled(True)
            self.sendTimeButton.setEnabled(True)

            self.comPortListenThread = Worker(self.comPortListen)
            self.comPortListenThread.signals.serialEventCallback.connect(self.serialEventHandler)
            self.threadPool.start(self.comPortListenThread)

    def unbindComPort(self):
        self.com_port.end()
        self.selectComPortComboBox.setEnabled(True)
        self.comConnectButton.clicked.connect(lambda: self.bindComPort(self.selectComPortComboBox.currentText()))
        self.comConnectButton.setText("Connect")
        self.ledButtonOn.setDisabled(True)
        self.ledButtonOff.setDisabled(True)
        self.sendTimeButton.setDisabled(True)

    def comPortListen(self, serialEventCallback):
        while True:
            print("some")
            self.com_port.readLine()
            line = self.com_port.popMessage()
            if line:
                serialEventCallback.emit(line)

    def sendTime(self):
        self.com_port.sendCommand(command=f"T{int(self.msInput.text())}\n")

    def serialEventHandler(self, line):
        self.textEdit.insertPlainText(line)
        self.textEdit.moveCursor(QTextCursor.End)

        if line[0] == 'L':
            if line[1] == '1':
                self.ledButtonOn.setDisabled(True)
                self.ledButtonOff.setEnabled(True)
            else:
                self.ledButtonOn.setEnabled(True)
                self.ledButtonOff.setDisabled(True)
        elif line[0] == 'T':
            if line[1] == 'S':
                self.msInput.setDisabled(True)
                self.sendTimeButton.setDisabled(True)
            elif line[1] == 'E':
                self.msInput.setEnabled(True)
                self.sendTimeButton.setEnabled(True)


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = MainWindow()
    # Run the main Qt loop
    sys.exit(app.exec_())
