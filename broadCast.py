# import http.client
# import json

# connection = http.client.HTTPSConnection('api.github.com')

# headers = {'Content-type': 'application/json'}

# foo = {'text': 'Hello world github/linguist#1 **cool**, and #1!'}
# json_foo = json.dumps(foo)

# connection.request('POST', '/markdown', json_foo, headers)

# response = connection.getresponse()
# print(response.read().decode())

import time
import serial
import sys

serialPort = '/dev/ttyUSB0'

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port=serialPort,
    baudrate=9600,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS
)

ser.isOpen()

print('Sending Arg to ' + serialPort +' \r\nInsert "exit" to leave the application.')


ser.write(input)
ser.close()
exit()