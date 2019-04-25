import time
import datetime
import colorsys
import numpy as np
from PIL import Image
from time import strftime
from time import time as t
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3

# (1) Import the file to be analyzed!
#img_file = Image.open("dead_parrot.jpg")
img_file = Image.open("thedress.jpg")
img = img_file.load()

# (2) Get image width & height in pixels
[xs, ys] = img_file.size
max_intensity = 100
hues = {}

print("Total X: %d" % xs)
print("Total Y: %d" % ys)

begin = datetime.datetime.now()
medium_time = datetime.datetime.now()
medium_time -= medium_time

# (3) Examine each pixel in the image file
for x in range(0, xs):
    for y in range(0, ys):
        #print("Analyse x: %d | y: %d" % (x, y))
        start = datetime.datetime.now()
        # (4)  Get the RGB color of the pixel
        [r, g, b] = img[x, y]

        # (5)  Normalize pixel color values
        r /= 255.0
        g /= 255.0
        b /= 255.0

        # (6)  Convert RGB color to HSV
        [h, s, v] = colorsys.rgb_to_hsv(r, g, b)

        # (7)  Marginalize s; count how many pixels have matching (h, v)
        if h not in hues:
            hues[h] = {}
        if v not in hues[h]:
            hues[h][v] = 1
        else:
            if hues[h][v] < max_intensity:
                hues[h][v] += 1

        end = datetime.datetime.now()
        medium_time = (medium_time + (end - start)) / 2

        b = "Analyse x: %d | y: %d" % (x, y)
        m = "Average time measured: %s" % medium_time
        print (b + "\t" + m, end="\r")
        #print (m, end="\r")
        

end = datetime.datetime.now()
print('Before: %s' % begin)
print('After: %s' % end)
print('Average time measured: %s' % medium_time)

# (8)   Decompose the hues object into a set of one dimensional arrays we can use with matplotlib
h_ = []
v_ = []
i = []
colours = []


for h in hues:
    for v in hues[h]:
        h_.append(h)
        v_.append(v)
        i.append(hues[h][v])
        [r, g, b] = colorsys.hsv_to_rgb(h, 1, v)
        colours.append([r, g, b])

# (9)   Plot the graph!
fig = plt.figure()
ax = p3.Axes3D(fig)
ax.scatter(h_, v_, i, s=5, c=colours, lw=0)

ax.set_xlabel('Hue')
ax.set_ylabel('Value')
ax.set_zlabel('Intensity')
fig.add_axes(ax)
plt.show()
