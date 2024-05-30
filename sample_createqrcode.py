import os
import requests
import io
import qrcode
from PIL import Image
from flask import Flask, send_file
app = Flask(__name__)

@app.route('/')
def index():
   print("start")
   # new_dir_path = 'qrImage/'
   # if not os.path.isdir(new_dir_path):
   #  os.mkdir(new_dir_path)
   
   img = qrcode.make("test_createQRcode")
   img_byte_array = io.BytesIO()
   img.save(img_byte_array, format='PNG')
   img_byte_array.seek(0)
   
   # file_name = os.path.basename('https://createqrcode-test.onrender.com/qrImage/sample_QRcode.png')
   # response = requests.get('https://createqrcode-test.onrender.com/qrImage/sample_QRcode.png')
   # with open(file_name, 'wb') as file:
   #  file.write('response.content')
   
   return send_file(img_byte_array, mimetype='image/png', as_attachment=True, attachment_filename='generated_image.png')

if __name__ == '__main__':
    app.run(debug=True)
  
print("end")
