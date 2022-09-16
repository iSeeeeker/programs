import pyqrcode
import png
from pyqrcode import QRCode

s = input('Insert here the link you want to transform into a qrcode')

url = pyqrcode.create(s)


url.svg('qrcode.svg', scale = 6)

url.png('qrcode.png', scale = 6)

print("QRcode generated!")
