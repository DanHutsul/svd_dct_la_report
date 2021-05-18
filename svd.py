%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import time
import urllib.request
from PIL import Image

import cv2 as cv

urllib.request.urlretrieve(
  'https://upload.wikimedia.org/wikipedia/commons/a/a3/Black-Magic-Big-Boy.jpg',
   "ImageA.jpg")

urllib.request.urlretrieve(
  'https://www.oddcities.com/wp-content/uploads/2015/05/Old-Town-Edinburgh-72.jpg',
   "ImageB.jpg")

imgA = Image.open('ImageA.jpg')
imgAcolor = imgA.convert('RGB')
imgAgray = imgA.convert('LA')
plt.figure(figsize=(9, 6))
plt.imshow(imgAcolor)
plt.figure(figsize=(9, 6))
plt.imshow(imgAgray)

imgAgrayMat = np.array(list(imgAgray.getdata(band=0)), float)
imgAgrayMat.shape = (imgAgray.size[1], imgAgray.size[0])
imgAgrayMat = np.matrix(imgAgrayMat)
plt.figure(figsize=(9,6))
plt.imshow(imgAgrayMat, cmap='gray')

U, sigma, V = np.linalg.svd(imgAgrayMat)

width = imgAgray.size[1]

sizes = [0.05, 0.15, 0.25, 0.50, 0.75]

for size in sizes:
    i = int(width*size)

    reconstimg = np.matrix(U[:, :i]) * np.diag(sigma[:i]) * np.matrix(V[:i, :])
    plt.imshow(reconstimg, cmap='gray')
    title = "n = %s" % i
    plt.title(title)
    plt.show()

imgB = Image.open('ImageB.jpg')
imgBcolor = imgB.convert('RGB')
imgBgray = imgB.convert('LA')
plt.figure(figsize=(9, 6))
plt.imshow(imgBcolor)
plt.figure(figsize=(9, 6))
plt.imshow(imgBgray)

imgBgrayMat = np.array(list(imgBgray.getdata(band=0)), float)
imgBgrayMat.shape = (imgBgray.size[1], imgBgray.size[0])
imgBgrayMat = np.matrix(imgBgrayMat)
plt.figure(figsize=(9,6))
plt.imshow(imgBgrayMat, cmap='gray')

U, sigma, V = np.linalg.svd(imgBgrayMat)

width = imgBgray.size[1]

sizes = [0.05, 0.15, 0.25, 0.50, 0.75]

for size in sizes:
    i = int(width*size)

    reconstimg = np.matrix(U[:, :i]) * np.diag(sigma[:i]) * np.matrix(V[:i, :])
    plt.imshow(reconstimg, cmap='gray')
    title = "n = %s" % i
    plt.title(title)
    plt.show()