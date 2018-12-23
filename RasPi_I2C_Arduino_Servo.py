import smbus
from time import sleep

bus = smbus.SMBus(1)

SLAVE_ADDRESS = 0x04

def writeCommand(cmd):
    bus.write_byte(SLAVE_ADDRESS, cmd)
    print("send: ",cmd)

while True:
    command = int(input("Enter command, 0-180 : "))
    if command >= 0 and command <= 180:
        writeCommand(command)
    else:
        print("Error")
