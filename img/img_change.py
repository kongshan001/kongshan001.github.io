from PIL import Image

import sys
import os

print(f"os.getcwd:{os.getcwd()}")


def change_pic_size_by_cur_img(sCurImagePath, sNewImagePath):
    with Image.open(sCurImagePath) as img:
        new_size = img.size

    with Image.open(sNewImagePath) as img:
        print(f"Image size: {img.size}")

        new_img = img.resize(new_size)
        new_img.save(sCurImagePath)


if __name__ == "__main__":
    change_pic_size_by_cur_img("./img/avatar-by.jpg", "./img/hello_world.jpg")
