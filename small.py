from PIL import Image
from numpy import*
import matplotlib.cm as cm
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
from sklearn.decomposition import PCA
def pixelate(first_file, second_file, pixel_size):
    im1 = Image.open(first_file)
    im2 = Image.open(second_file)
    #resizing
    im1 = im1.resize((size, size), Image.BILINEAR)
    im2 = im2.resize((size, size), Image.BILINEAR)
    A1 = black_and_white(im1)
    A2 = black_and_white(im2)
    return A1, A2
def black_and_white(temp):
    temp=temp.convert('1')
    A = array(temp)             # Creates an array, white pixels==True and black pixels==False
    new_A=empty((A.shape[0],A.shape[1]),None)    #New array with same size as A
    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j]==True:
                new_A[i][j]=0
            else:
                new_A[i][j]=1
    return A
if __name__ == "__main__":
    file_1 = "download.png"
    file_2 = "download.jpeg"
    size = 100
    A1, A2 = pixelate(file_1, file_2, size)
    print(A1)
    print(A2)
    plt.imsave('filename2.jpeg',A2, cmap=cm.gray)