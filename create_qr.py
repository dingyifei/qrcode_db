import uuid
import qrcode


def gen_qrcode(uid=-1, save_directory="./"):
    uid = uuid.uuid4().int if uid == -1 else uid
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, border=0)
    qr.add_data(uid)
    qr.make_image(fill_color="black", back_color="white").save(save_directory + str(uid) + ".png")
    return uid

