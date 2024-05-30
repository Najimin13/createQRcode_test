import qrcode
from PIL import Image

img = qrcode.make("test_createQRcode")
img.save('sample_QRcode.png')

img.show()
