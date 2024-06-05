import os
import requests
import io
import qrcode
from PIL import Image
from flask import Flask, send_file, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html', title='おためし')
  

@app.route('/result', methods=['GET', 'POST'])
def result():
   print("start")

   if request.method == 'POST':
        name = request.form['miyuu']
        img = qrcode.make(name)
        img_byte_array = io.BytesIO()
        img.save(img_byte_array, format='PNG')
        img_byte_array.seek(0)   
        return send_file(img_byte_array, mimetype='image/png', as_attachment=True, download_name='test_createQRcode.png')
        
   if request.method == 'GET':
      return render_template('resultGet.html', title='おためしGET')
        
if __name__ == '__main__':
    app.run(debug=True)
  
print("end")
