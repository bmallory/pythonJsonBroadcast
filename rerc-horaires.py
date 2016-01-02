from urllib2 import urlopen
import bs4 as BeautifulSoup
import serial
import sys
import unicodedata

serialPort = '/dev/ttyUSB0'
toSend = '{lcd1:"Prochain RER C:'

html = urlopen('http://www.transilien.mobi/train/result?idOrigin=CHV&idDest=CPM').read()
soup = BeautifulSoup.BeautifulSoup(html, "html5lib")
for tag in soup.find_all(class_='heure_train'):
	toSend += ' '+ tag.string[0:5]
toSend += '"}'

print(toSend)


ser = serial.Serial(
    port=serialPort,
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

ser.isOpen()


waz = toSend
toSend = unicodedata.normalize('NFD', waz).encode('ascii', 'ignore')
ser.write(toSend.replace('Supprime', 'Sup.'))
ser.close()
exit()
