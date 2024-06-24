import qrcode
from PIL import Image

# Create an instance of QRCode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

# Get the link from the user
link = input("Enter the link you want to convert to QR code: ")
qr.add_data(link)
qr.make(fit=True)

# Create the image
img = qr.make_image(fill_color="black", back_color="white")
img.save('Qrcode.png')
try:
    print("The QR code of your link is generated in the folder where you have stored your file.")
except Exception as e:
    print(e)
