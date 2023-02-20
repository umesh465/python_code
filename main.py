import qrcode
img = qrcode.make("hello! my name is umesh, nice to meet you ")
img.save("my_qr_code.png")