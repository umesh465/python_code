import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=input("Enter box_size  "),
    border=input("Enter border  "),
)

qr.add_data(input("Enter message"))
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("next_test.png")