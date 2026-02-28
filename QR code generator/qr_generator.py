import qrcode
url = input("Enter your URL : ").strip()
file_path = "C:\\Users\\Dharmin\\OneDrive\\Desktop\\qrcode.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

print("QR code generated") 
