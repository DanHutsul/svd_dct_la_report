%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import time
import urllib.request
from urllib.request import urlopen
from PIL import Image
from scipy.fftpack import dct, idct


def dct2(a):
    return dct(dct(a.T, norm='ortho').T, norm='ortho')

def idct2(a):
    return idct(idct(a.T, norm='ortho').T, norm='ortho')

def get_2D_dct(img):
    """ Get 2D Cosine Transform of Image
    """
    return dct(dct(img.T, norm='ortho').T, norm='ortho')

def get_2d_idct(coefficients):
    """ Get 2D Inverse Cosine Transform of Image
    """
    return idct(idct(coefficients.T, norm='ortho').T, norm='ortho')

def get_reconstructed_image(raw):
    img = raw.clip(0, 255)
    img = img.astype('uint8')
    img = Image.fromarray(img)
    return img

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

width = imgAgray.size[1]

dct_size = imgAgrayMat.shape[0]
dct = get_2D_dct(imgAgrayMat)
reconstructed_images = [""]*(width)
print(len(reconstructed_images))
items = [int(width*0.05), int(width*0.15), int(width*0.25), int(width*0.5), int(width*0.75)]

for ii in items:
    dct_copy = dct.copy()
    dct_copy[ii:,:] = 0
    dct_copy[:,ii:] = 0
    
    # Reconstructed image
    r_img = get_2d_idct(dct_copy)
    reconstructed_image = get_reconstructed_image(r_img)

    # Create a list of images
    reconstructed_images[ii] = reconstructed_image

sizes = [0.05, 0.15, 0.25, 0.50, 0.75]

for size in sizes:
    i = int(width*size)

    plt.plot(8, 8, i + 1)
    plt.imshow(reconstructed_images[i], cmap=plt.cm.gray)
    title = "n = %s" % i
    plt.title(title)
    plt.show()

imgA = Image.open('ImageB.jpg')
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

width = imgAgray.size[1]

dct_size = imgAgrayMat.shape[0]
dct = get_2D_dct(imgAgrayMat)
reconstructed_images = [""]*(width)
print(len(reconstructed_images))
items = [int(width*0.05), int(width*0.15), int(width*0.25), int(width*0.5), int(width*0.75)]



for ii in items:
    dct_copy = dct.copy()
    dct_copy[ii:,:] = 0
    dct_copy[:,ii:] = 0
    
    # Reconstructed image
    r_img = get_2d_idct(dct_copy)
    reconstructed_image = get_reconstructed_image(r_img)

    # Create a list of images
    reconstructed_images[ii] = reconstructed_image

sizes = [0.05, 0.15, 0.25, 0.50, 0.75]

for size in sizes:
    i = int(width*size)

    plt.plot(8, 8, i + 1)
    plt.imshow(reconstructed_images[i], cmap=plt.cm.gray)
    title = "n = %s" % i
    plt.title(title)
    plt.show()