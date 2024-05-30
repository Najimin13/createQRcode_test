import qrcode
from PIL import Image
from flask import Flask
app = Flask(__name__)

img = qrcode.make("test_createQRcode")
img.save('sample_QRcode.png')

@app.route('/')
def index():
   return "中川美憂"
  
print("end")
