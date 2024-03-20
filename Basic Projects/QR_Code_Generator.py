import qrcode
import requests
from PIL import Image
import os

def check_link_existence(url):
    try:
        response = requests.head(url)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

# Create QR code
qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10, border=4)

# Input URL for generating QR code
url = input("Enter the URL which you want to encode into the QR code: ")
qr.add_data(url)
qr.make(fit=True)
qr_image = qr.make_image(fill_color='black', back_color='white')

# Specify directory to save the image
image_path = input("Enter the directory path to save the QR code image: ")
image_path = os.path.join(os.getcwd(), image_path)
os.makedirs(image_path, exist_ok=True)

# Enter the image name with extension
image_name = input("Enter the image name with extension: ")
qr_image.save(os.path.join(image_path, image_name))
print("Image saved successfully at:", os.path.join(image_path, image_name))

# Check if the link exists
if check_link_existence(url):
    print("The link exists.")
else:
    print("The link does not exist.")


