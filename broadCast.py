import serial
import sys

serialPort = '/dev/ttyUSB0'

toSend = sys.argv[0]

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port=serialPort,
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

ser.isOpen()

print('Sending \' '+ toSend +' \' --> ' + serialPort +' \r\n')

ser.write(toSend)
ser.close()
exit()