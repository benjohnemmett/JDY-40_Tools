import serial
import time
import sys

serial_port_name_1 = "/dev/tty.usbserial-00000000"
serial_port_name_2 = "/dev/tty.usbserial-A50285BI"
baud_rate = 9600


class serialously:

    def __init__(self, serial_port_name):
        self.ser = serial.Serial(serial_port_name, baud_rate)


    def send(self, cmd):
        print(f"> {cmd}")
        cmd_bytes = cmd + "\r\n"
        num_bytes = self.ser.write(cmd_bytes.encode())
        print(f" [{num_bytes}]")


    def recv(self):
        line = self.ser.readline()
        print(f"< {line.decode()}")
        return line



if __name__ == "__main__":

    serial_port_name = serial_port_name_1

    if len(sys.argv) > 1:
        serial_port_name = serial_port_name_2

    print(f" Connecting to {serial_port_name} at {baud_rate} baud")
    ser = serialously(serial_port_name)

    print("Listening...")
    while True:
        ser.recv()
