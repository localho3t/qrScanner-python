
import pyqrcode 
from pyqrcode import QRCode 

name = input("Enter Name : ")
s = name


url = pyqrcode.create(s) 
url.svg(name+".svg", scale = 8) 
