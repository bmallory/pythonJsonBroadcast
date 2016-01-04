import urllib2, base64
import bs4 as BeautifulSoup
import serial
import sys
import unicodedata

serialPort = '/dev/ttyUSB0'
toSend = '{lcd1:"Prochain RER C:'

#html = urlopen('http://www.transilien.mobi/train/result?idOrigin=CHV&idDest=CPM').read()

request = urllib2.Request('http://api.transilien.com/gare/87393173/depart/87393058')
base64string = base64.encodestring('%s:%s' % ("username", "password")).replace('\n', '')
request.add_header("Authorization", "Basic %s" % base64string)   
xml = urllib2.urlopen(request)

soup = BeautifulSoup.BeautifulSoup(xml, "xml")
#for tag in soup.find_all(class_='heure_train'):
for tag in soup.find_all("date"):
	toSend += ' '+ tag.string[11:5]
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
