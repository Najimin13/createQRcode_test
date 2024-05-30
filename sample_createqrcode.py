import os
import qrcode
from PIL import Image
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
   print("start")
   img = qrcode.make("test_createQRcode")
   img.save('sample_QRcode.png')
   if os.path.isfile('sample_QRcode.png'):
    print("有り")
else:
    print("無し")
   return ""
  
print("end")
