import os
import zipfile


class Docx(object):

    def __init__(self, fp: str, new_fp: str, tmp_dir: str):

        self.fp = fp if os.path.isfile(fp) else None
        self.new_fp = new_fp if os.path.isfile(new_fp) else None
        self.tmp_dir = tmp_dir if os.path.isdir(tmp_dir) else None
        if self.fp is None or self.new_fp is None or self.tmp_dir is None:
            raise ValueError

    def replace_images_with_text(self, png_path: str):
        # The text should be less than 30
        png_list: list = os.listdir(png_path)
        with zipfile.ZipFile(self.fp, "a") as zip_file:

            # Count if the images we are going to replace aren't more or less than what we want.
            img_count = 0
            for file in zip_file.filelist:
                if "word/media/" in file.filename:
                    img_count += 1
            # Check if the png_list are all png
            for png in png_list:
                if png[-3:-1] != ".png":
                    raise ValueError("Not a file path with only png")
            if len(png_list) != img_count:
                raise ValueError("the file path contain different amount of images than it should have")
            # start to replace the png in docx
