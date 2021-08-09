import sys
from threading import Thread

from serial.tools.list_ports import comports

from com import Com, ComException


def com_job(com: Com) -> None:
    '''
    Basic reading job

    Parameters
    ----------
    com : Com
        A initialized Com to use
    '''
    while True:
        com.readLine()
        line = com.popMessage()
        if line:
            print("Arduino : {}".format(line), end='')


def main():
    com_port = Com()
    available_ports = comports()

    print("Select a COM port to open :(i.e : `COM1`)")
    for port, desc, hwid in available_ports:
        print("[{}] : {}".format(port, desc))

    chosen_port = input()
    try:
        com_port.start(chosen_port, 115200)
    except ComException as e:
        print(e)
        sys.exit()

    com_thread = Thread(name="ComThread", target=com_job, daemon=True, args=(com_port,))
    com_thread.start()
    print("type `!EXIT` to exit...")
    while True:
        user_input = input()
        if user_input == "!EXIT":
            # com_thread.join()
            sys.exit()
        com_port.sendCommand(user_input + '\n')


if __name__ == '__main__':
    main()
