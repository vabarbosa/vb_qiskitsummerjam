from PIL import Image
import cv2
from numpy import*
import matplotlib.cm as cm
import numpy as np
import matplotlib.pyplot as plt
temp=Image.open('download.jpeg')
temp=temp.convert('1')      # Convert to black&white
A = array(temp)             # Creates an array, white pixels==True and black pixels==False
new_A=empty((A.shape[0],A.shape[1]),None)    #New array with same size as A
for i in range(len(A)):
    for j in range(len(A[i])):
        if A[i][j]==True:
            new_A[i][j]=0
        else:
            new_A[i][j]=1


#print(new_A, len(new_A))
shape = new_A.shape
flat_arr = new_A.ravel()
print(flat_arr)
vector = np.matrix(flat_arr)
arr2 = np.asarray(vector).reshape(shape)
# make a 1-dimensional view of arr


plt.imsave('filename1.jpeg',arr2, cmap=cm.gray)