import qrcode as qr
from PIL import Image
qr=qr.QRCode(
    version=1,
    error_correction=qr.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data("https://2flix.lol/the-social-network/")
qr.make(fit=True)

img=qr.make_image(fill_color="orange",back_color="white")
img.save("social_network_qr.png")