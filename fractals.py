#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import random
from random import randrange

def get_iter(c:complex, thresh:int = 4, max_steps:int = 25) -> int:
    z=c
    i=1
    while i<max_steps and (z*z.conjugate()).real<thresh:
        z=z*z +c
        i+=1
    return i

def plotter(n, thresh, max_steps=25):
    mx = 2.48 / (n-1)
    my = 2.26 / (n-1)
    mapper = lambda x,y: (mx*x - 2, my*y - 1.13)
    img=np.full((n,n), 256)
    for x in range(n):
        for y in range(n):
            it = get_iter(complex(*mapper(x,y)), thresh=thresh, max_steps=max_steps)
            img[y][x] = 255 - it
    return img

cmaps=['viridis', 'plasma', 'inferno', 'magma', 'cividis', 'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', \
'Reds', 'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu', 'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn']

cmap=random.choice(cmaps)

print("Random cmap color chosen from list is: ", cmap)
n = randrange(2000)
img = plotter(n, thresh=4, max_steps=randrange(150))
plt.imshow(img, cmap=cmap)
plt.axis("off")
plt.show()
 
