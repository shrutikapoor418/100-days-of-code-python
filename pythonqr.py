import qrcode
import qrcode.constants
from PIL import Image
qrr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
qrr.add_data(" url to make qr ")
qrr.make(fit=True)
img = qrr.make_image(fill_color="green", back_color="white")
img.save("we_obb.png")
