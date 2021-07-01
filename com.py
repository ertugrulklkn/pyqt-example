from queue import Queue

from serial import Serial
from serial.serialutil import SerialException


class ComException(Exception):
    def __str__(self) -> str:
        return "COM could not connect!"


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
        except (ValueError, SerialException):
            raise ComException

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
