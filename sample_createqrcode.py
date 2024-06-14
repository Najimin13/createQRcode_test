import os
import requests
import io
import qrcode
from PIL import Image
from flask import Flask, send_file, render_template, request
import  json
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
   print("start")

   if request.method == 'POST':
        name = request.form['miyuu']
        img = qrcode.make(name)
        img_byte_array = io.BytesIO()
        img.save(img_byte_array, format='PNG')
        img_byte_array.seek(0)   
        img.save('test_createQRcode.png')
        
        with open('test_createQRcode.png', "rb") as q:
	        url = "https://api.pinata.cloud/pinning/pinFileToIPFS"
	        files = [
	        ('file', ('test_createQRcode.png',q )),
	        ]
	        headers = {
	        'pinata_api_key': "7889b920748ef631b2b0",
	        'pinata_secret_api_key': "d8f3b545743f4760ec2937d3faf4df60b481a28b9b7d1c83c16ba72685455db4"
	        }
	        response = requests.request("POST", url, files=files, headers=headers)
	        print(response.text)
	        
	        q.close()
        os.remove('test_createQRcode.png')
        
        getUrl = 'https://gateway.pinata.cloud/ipfs/' + response.json()["IpfsHash"]
        
        #画面上にURLを返したい時はこっち
        #return render_template('index.html', title='おためし成功？', qrurl=getUrl)
        
        #単にURLを返したいだけの時はこっち
        return getUrl
        
   if request.method == 'GET':
      return render_template('resultGet.html', title='おためしGET')
        
if __name__ == '__main__':
    app.run(debug=True)
