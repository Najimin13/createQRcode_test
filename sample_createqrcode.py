import qrcode
from PIL import Image
from flask import Flask
app = Flask(__name__)



@app.route('/')
def index():
   img = qrcode.make("test_createQRcode")
   img.save('sample_QRcode.png')
   return img.show()
  
print("end")
