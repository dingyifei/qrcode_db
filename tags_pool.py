import uuid
import qrcode
import sqlite3
import time


class Database(object):
    def __init__(self, fp, data_table_name):
        self.fp = fp
        self.data_table_name = data_table_name
        self.sqlite = sqlite3.connect(fp)
        self.cursor = self.sqlite.cursor()
        try:
            self.cursor.execute('''
            CREATE TABLE ?(UID INT PRIMARY KEY,NAME TEXT,LAST_ACCESS_TIME INT,CREATE_TIME INT,EXPIRE_TIME INT,NOTE TEXT)
            ''', (data_table_name))
        except sqlite3.OperationalError:
            print("DATA TABLE ALREADY EXIT")

    def __del__(self):
        self.commit_db()
        self.sqlite.close()

    def gen_qrcode(self, uid, save_directory="./"):
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, border=0)
        qr.add_data(self.uid)
        qr.make_image(fill_color="black", back_color="white").save(save_directory + str(self.uid) + ".png")
        return True

    def commit_db(self):
        self.sqlite.commit()

    def create_tag(self, uid):

        new_tag = uuid.uuid4().int
        self.cursor.execute("INSERT INTO ? VALUES(?,?,?,?,?,?)",
                            (self.data_table_name, new_tag.uid, '', -1, -1, -1, ''))
        return new_tag.uid

    def get_tag(self, uid):
        # get tag from system
        return new_tag.uid
