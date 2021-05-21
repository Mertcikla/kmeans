from PIL import Image
import random
import numpy
from sklearn.cluster import KMeans
from IPython.display import display

im = Image.open('kitten.jpg').convert('RGB')
display(im)
k = 4  # number of clusters
r, g, b = im.getchannel(0), im.getchannel(
    1), im.getchannel(2)  # Split into 3 channels

rm = numpy.array(r)
gm = numpy.array(g)
bm = numpy.array(b)


def totuple(a):
    try:
        return tuple(totuple(i) for i in a)
    except TypeError:
        return a


def kmeans(m, k):
    c = []  # new color palette of length k
    p = []  # number of pixels that belong to n th color
    for i in range(0, k):  # init
        c.append((255*(i))/(k-1))
        p.append(1)

    a = m.flatten().astype(int)
    for i in a:
        closest = 50000  # arbitrary value to find max
        closest_index = 0
        for j in range(0, k):
            if int(abs(i - c[j])) < closest:
                closest = int(abs(i - c[j]))
                closest_index = j
        c[closest_index] = (
            c[closest_index]*p[closest_index] + i) / (p[closest_index]+1)  # update palette value
        p[closest_index] += 1

    return totuple(c)


rf = kmeans(rm, k)  # new palette (R1, R2, .... Rk) 
gf = kmeans(gm, k)  # new palette (G1, G2, .... Gk)
bf = kmeans(bm, k)  # new palette (B1, B2, .... Bk)

#instead of log255 =8 bits per channel, we can use logk bits per channel, per pixel

# for each pixel find and assign the closest new color from its channel palette

for i in range(im.width):
    for j in range(im.height):
        for p in range(k):
            l = (i, j)
            pixel = im.getpixel(l)
            # print(pixel)
            closest = 5000
            ind = 0
            for z in range(k):
                if abs(pixel[0]-rf[z]) < closest:
                    closest = abs(pixel[0]-rf[z])
                    ind = z
            newredvalue = int(rf[ind])
            closest = 5000
            ind = 0
            for z in range(k):
                if abs(pixel[1]-gf[z]) < closest:
                    closest = abs(pixel[1]-gf[z])
                    ind = z
            newgreenvalue = int(gf[ind])
            closest = 5000
            ind = 0
            for z in range(k):
                if abs(pixel[2]-bf[z]) < closest:
                    closest = abs(pixel[2]-bf[z])
                    ind = z
            newbluevalue = int(bf[ind])
            im.putpixel((i, j), (newredvalue, newgreenvalue, newbluevalue))

im.save('compressed_kitten.png')
