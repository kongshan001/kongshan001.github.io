from PIL import Image

import sys
import os

print(f"os.getcwd:{os.getcwd()}")

with Image.open("./img/avatar-by.jpg") as img:
    new_size = img.size

with Image.open("./img/hello_world.jpg") as img:
    print(f"Image size: {img.size}")

    new_img = img.resize(new_size)
    new_img.save("./img/avatar-by1.jpg")



