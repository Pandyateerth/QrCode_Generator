import qrcode
img = qrcode.make("https://www.instagram.com/")
img.save("instagram.jpg")