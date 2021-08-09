from queue import Queue

from serial import Serial
from serial.serialutil import SerialException


class ComException(Exception):
    def __init__(self, e: SerialException or ValueError, *args: object) -> None:
        super().__init__(*args)
        if e:
            self.message = e.strerror
        else:
            self.message = ""

    def __str__(self) -> str:
        return f"COM could not connect! {self.message}"


class Com(object):
    """COM port to communicate Arduino"""

    def __init__(self):
        self.led_status = False
        self.serial: Serial
        self.com_queue = Queue()

    def start(self, port, baud) -> None:
        """Set the serial port. Returns None, may\
        throw exception ComException if the port is not available.

        Parameters
        ----------
        port: str
            Name of port
        baud: int
            Baudrate to set

        """
        try:
            self.serial = Serial(port, baud)
        except (ValueError, SerialException) as e:
            raise ComException(e)

    def end(self):
        self.serial.close()

    def sendCommand(self, command: str) -> None:
        """Send a single line command to Arduino.

        Parameters
        ----------
        command: str
            Command to send
        """
        self.serial.write(command.encode())

    def readLine(self) -> None:
        """Read a single line message from Arduino to buffer."""
        self.com_queue.put(self.serial.readline().decode())

    def popMessage(self) -> str:
        """Get a single line message from buffer.\
            Returns None if buffer is empty.
        """
        if not self.com_queue.empty():
            return self.com_queue.get()
        return None

    def sendLedCommand(self, light: bool) -> bool:
        if light:
            self.sendCommand("L1\n")
        else:
            self.sendCommand("L0\n")
