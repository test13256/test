import qrcode  # pip install qrcode[pil]

FILE_NAME = "1.png"
VERSION = 'small'  #'big' or 'small'
URL = 'your_url'


def main():

    if VERSION == 'big':
        qr_ver = 10
        qr_err = qrcode.constants.ERROR_CORRECT_H
    elif VERSION == 'small':
        qr_ver = 5
        qr_err = qrcode.constants.ERROR_CORRECT_M
    else:
        return

    qr = qrcode.QRCode(
        version=qr_ver,
        error_correction=qr_err,
        box_size=10,
        border=1,
    )
    qr.add_data(URL)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(FILE_NAME)


main()