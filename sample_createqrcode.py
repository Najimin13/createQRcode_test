import os
import requests
import io
import qrcode
import subprocess
from PIL import Image
from flask import Flask, send_file, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html', title='おためし')
  

@app.route('/result', methods=['GET', 'POST'])
def result():
   print("start")
   RIPPLE_API_COMMAND = "index.js"


   if request.method == 'POST':
        name = request.form['miyuu']
        img = qrcode.make(name)
        img_byte_array = io.BytesIO()
        img.save(img_byte_array, format='PNG')
        img_byte_array.seek(0)   
        img.save('test_createQRcode.png')
        

        subprocess.check_call('node index.js', shell=True)
            
        return render_template('index.html', title='おためし成功？')
        
   if request.method == 'GET':
      return render_template('resultGet.html', title='おためしGET')
        
if __name__ == '__main__':
    app.run(debug=True)
  
print("end")
