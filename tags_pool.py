import uuid
import qrcode
import json
import time


class Database(object):
    def __init__(self, fp):
        self.tags = {}
        self.fp = fp
        # self.save_file = json

    class Tag(object):

        def __init__(self, uid=0):
            self.uid = uuid.uuid4().int if uid == 0 else uid

        def __str__(self):
            return self.uid

        def gen_qrcode(self, save_directory="./"):
            qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, border=0)
            qr.add_data(self.uid)
            qr.make_image(fill_color="black", back_color="white") \
                .save(save_directory + str(self.uid) + ".png")
            return True

    def load_tags(self):
        self.save_file.read_file(open(self.fp))
        # for key in self.save_file.keys():
        #   self.tags[key] = self.save_file[key]

    def save_tags(self):
        print("helloworld")
        #for _ in self.tags:

    # self.save_file[tag] = int(time.time())
    # self.save_file.write(self.fp)

    def create_tag(self):
        # ignore the possibility a new uuid conflict with a existing one.

        new_tag = self.Tag()
        self.tags[new_tag.uid] = new_tag
        return new_tag.__str__()

    def create_tags(self, count):

        uids = []
        for x in range(0, count):
            uids.append(self.create_tag())
        return tuple(uids)
