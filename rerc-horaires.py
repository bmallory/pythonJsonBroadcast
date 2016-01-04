import urllib2, base64
import bs4 as BeautifulSoup
import serial
import sys
import unicodedata

serialPort = '/dev/ttyUSB0'
toSend = '{lcd1:"Prochain RER C:'

#html = urlopen('http://www.transilien.mobi/train/result?idOrigin=CHV&idDest=CPM').read()

request = urllib2.Request('http://api.transilien.com/gare/87393173/depart/87393058')
base64string = base64.encodestring('%s:%s' % ("XXX", "XXXXX")).replace('\n', '')
request.add_header("Authorization", "Basic %s" % base64string)   
xml = urllib2.urlopen(request).read()

soup = BeautifulSoup.BeautifulSoup(xml, "xml")
#for tag in soup.find_all(class_='heure_train'):
for train in soup.find_all("train"):
	for date in train.find_all("date"):
		toSend += ' '+ date.string[11:16]
	for etat in train.find_all("etat"):
		toSend += etat.string[0:1]
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
#ser.write(toSend.replace('Supprime', 'Sup.'))
ser.write(waz.encode('utf-8', 'ignore'))
ser.close()
exit()
