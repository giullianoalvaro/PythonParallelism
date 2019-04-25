#!/usr/bin/env python
from PIL import Image

def getImage(img_src):
    image_path = img_src
    image = Image.open(image_path)
    count = 0
    return image

if __name__ == "__main__":
    newimage2 = getImage('image.png')
    pix = newimage2.load()
    print(newimage2.size)
    print(" ")

    whitevalues = 0
    x = 0
    while x <= newimage2.width:
        y = 0
        while y <= newimage2.height:
            print(pix[x,y])
            if pix[x,y] == (255,255,255):
                whitevalues = whitevalues + 1
            y = y+1
        x = x+1
    print(whitevalues)


# from PIL import Image

# if __name__ == "__main__":
#     im = Image.open('dead_parrot.jpg') # Can be many different formats.
#     pix = im.load()
#     print(im.size)  # Get the width and hight of the image for iterating over
#     print(pix[x,y])  # Get the RGBA Value of the a pixel of an image
#     pix[x,y] = value  # Set the RGBA Value of the image (tuple)
#     im.save('alive_parrot.png')  # Save the modified pixels as .png
