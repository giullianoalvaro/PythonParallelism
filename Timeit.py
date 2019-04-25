#! /usr/bin/env python
# encoding:utf-8
from PIL import Image

# try:
#     from PIL import Image
# except ImportError as e:
#     print(e.msg)
#     raise ImportError(e)


# try:
#     from PIL.Image import Image
# except e:
#     print(e)

# image_path = '/path/to/image'
# image = Image.open(image_path)
# count = 0

# image.getdata() returns all the pixels in the image
for pixel in image.getdata():
    if pixel == (255, 255, 255):
        count += 1

print(count)
