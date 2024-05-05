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


def change_pic_2_ico(sImagePath, iWH=32):
    with Image.open(sImagePath) as img:
        new_img = img.resize((iWH, iWH))
        sNewPath = f"{os.path.splitext(sImagePath)[0]}.ico"
        new_img.save(sNewPath, format="ICO")



if __name__ == "__main__":
    # change_pic_size_by_cur_img("./img/avatar-by.jpg", "./img/hello_world.jpg")
    change_pic_2_ico("./img/ks_pic.png")