from PIL import Image
import cv2
from numpy import*
import matplotlib.cm as cm
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc


def pixelate(input_file_path, pixel_size):
    image = Image.open(input_file_path)
    image = image.resize(
        (image.size[0] // pixel_size, image.size[1] // pixel_size),
        Image.NEAREST
    )
    image = image.resize(
        (image.size[0] * pixel_size, image.size[1] * pixel_size),
        Image.NEAREST
    )

    #image.show()
    return image

#pixelate("download.png",16)

temp=pixelate("download.jpeg",60)
temp=temp.convert('1')      # Convert to black&white
A = array(temp)             # Creates an array, white pixels==True and black pixels==False
print(A)
new_A=empty((A.shape[0],A.shape[1]),None)    #New array with same size as A
for i in range(len(A)):
    for j in range(len(A[i])):
        if A[i][j]==True:
            new_A[i][j]=0
        else:
            new_A[i][j]=1

print(len(new_A))
shape = new_A.shape


# make a 1-dimensional view of arr
flat_arr = new_A.ravel()
print(sum(flat_arr), len(flat_arr))
vector = np.matrix(flat_arr)
arr2 = np.asarray(vector).reshape(shape)
plt.imsave('filename2.jpeg',arr2, cmap=cm.gray)
print(misc.imread("download.jpeg"))


