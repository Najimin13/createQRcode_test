import os
import requests
import qrcode
from PIL import Image
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
   print("start")
   new_dir_path = 'qrImage/'
   if not os.path.isdir(new_dir_path):
    os.mkdir(new_dir_path)
   img = qrcode.make("test_createQRcode")
   img.save('qrImage/sample_QRcode.png')
   file_name = os.path.basename('https://createqrcode-test.onrender.comqrImage/sample_QRcode.png')
   response = requests.get('qrImage/sample_QRcode.png')
   with open(file_name, 'wb') as file:
    file.write('response.content')
   
   return ""
  
print("end")
