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


print(new_A, len(new_A))

plt.imsave('filename.png', np.array(new_A), cmap=cm.gray)