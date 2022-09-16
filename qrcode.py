import pyqrcode
import png
from pyqrcode import QRCode

# Sito che dovrà essere convertito in qrcode
s = input('Inserisci il link del sito che vuoi trasformare in qrcode: ')

url = pyqrcode.create(s)


url.svg('qrcode.svg', scale = 6)

url.png('qrcode.png', scale = 6)

print("Codice QR creato!")