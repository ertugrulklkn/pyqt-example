import sys

from PySide2.QtWidgets import QApplication, QMainWindow

from ui.ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Time&Led")


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = MainWindow()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec_())
