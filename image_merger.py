#!/usr/bin/env python
# coding: utf-8

# In[1]:


# get_ipython().run_line_magic('matplotlib', 'inline')
# Importing standard Qiskit libraries and configuring account
from qiskit import QuantumCircuit, execute, Aer, IBMQ
from qiskit.compiler import transpile, assemble
from qiskit.tools.jupyter import *
from qiskit.visualization import *
# Loading your IBM Q account(s)
provider = IBMQ.load_account()


# In[129]:


from PIL import Image
from numpy import*
# import matplotlib.cm as cm
import numpy as np
# import matplotlib.pyplot as plt
temp=Image.open('download.png')
temp=temp.convert('1')      # Convert to black&white
A = array(temp)             # Creates an array, white pixels==True and black pixels==False
new_A=empty((A.shape[0],A.shape[1]),None)    #New array with same size as A
for i in range(len(A)):
    for j in range(len(A[i])):
        if A[i][j]==True:
            new_A[i][j]=0
        else:
            new_A[i][j]=1


shape = new_A.shape
#new_A = new_A[0:50,0:50]


# make a 1-dimensional view of arr
flat_arr = new_A.ravel()
print(sum(flat_arr), len(flat_arr))


# """
# COPIED CODE


# """
# import sys
# sys.path.append("../../qiskit-sdk-py/")
# from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
# import math
# from qiskit import(
#   QuantumCircuit,
#   execute,
#   Aer)
# from qiskit.tools.visualization import plot_histogram
# from qiskit import IBMQ

# # set up registers and program
# qr =  QuantumRegister(len(flat_arr), 'qr')
# cr = ClassicalRegister(len(flat_arr),'cr')
# qc = QuantumCircuit(qr, cr)

# # rightmost eight (qu)bits have ')' = 00101001
# count = 0;
# #for num, k in enumerate(flat_arr):
#     #if (k == 1):
# index = [index for index, value in enumerate(flat_arr) if value == 1]

# for k in index:
#     qc.x(qr[k])
#     qc.measure(qr[k], cr[k])


#     print("hello")
#     simulator = Aer.get_backend('qasm_simulator')
#     print("hello")
#     job = execute(qc, simulator, shots=1024)
#     print("hello")
#     results = job.result()
#     print("hello")
#     stats = results.get_counts(qc)

#     print("hello")

#     vector = np.matrix(flat_arr)



#         #print(count)
#        # if (count%100 == 0):
#          #   print(count)
#        # count = count +1


# In[2]:


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
    A1 = (im1)
    A2 = (im2)
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

file_1 = "download.png"
file_2 = "download.png"
size = 10
A1, A2 = pixelate(file_1, file_2, size)
plt.imsave('filename2.jpeg',A2, cmap=cm.gray)


# In[3]:


new_A=empty((A1.shape[0],A1.shape[1]),None)    #New array with same size as A
for i in range(len(A1)):
    for j in range(len(A1[i])):
        if A1[i][j]==True:
            new_A[i][j]=0
        else:
            new_A[i][j]=1


shape = new_A.shape
#new_A = new_A[0:50,0:50]


# In[4]:


img = np.asarray(A1)
new_img = img.reshape((img.shape[0]*img.shape[1]), img.shape[2])
new_img = new_img.transpose()


# In[126]:


new_img.shape


# In[53]:


from PIL import Image
from numpy import*
import matplotlib.cm as cm
import numpy as np
import matplotlib.pyplot as plt
#flat_arr = new_A.ravel()
#print(sum(flat_arr), len(flat_arr))


"""
COPIED CODE


"""
import sys
sys.path.append("../../qiskit-sdk-py/")
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
import math
from qiskit import(
  QuantumCircuit,
  execute,
  Aer)
from qiskit.tools.visualization import plot_histogram
from qiskit import IBMQ

# set up registers and program
qr =  QuantumRegister(15, 'qr')
cr = ClassicalRegister(15,'cr')
qc = QuantumCircuit(qr, cr)



# rightmost eight (qu)bits have ')' = 00101001
count = 0;
#for num, k in enumerate(flat_arr):
    #if (k == 1):
#index = [index for index, value in enumerate(flat_arr) if value == 1]
double = np.zeros((3,100))
count = 1
for p in range(3):
    for k in range(100):
        
        num_1 = bin(new_img[p][k])
        num_2 = bin(new_img[p][k])
        #print("num1 index: ", len(str(num_1)))
        for i in range(len(str(num_1))):
            if num_1[i] == str(1):
                qc.x(qr[i])
    
        qc.h(qr[7]) # create superposition on 9
        qc.cx(qr[7],qr[8]) # spread it to 8 with a cnot
        
        for i in range(len(str(num_2))):
                    if num_2[i] == str(1):
                        qc.x(qr[i+5])
                
        for j in range(15):
            qc.measure(qr[j], cr[j])      
                
        simulator = Aer.get_backend('qasm_simulator')

        job = execute(qc, simulator, shots=1)

        results = job.result()

        stats = results.get_counts(qc)
        
        register_value = stats.keys()
        
        
        for x in register_value:
        
            
            split = x[0:7]
            split2 = x[7:15]
            #print(split2)
            total = abs(int(split,2)-int(split2,2))
            
            double[p][k] = total
            #print(total)
            print("Quantum1 :", (abs(int(split,2)+int(split2,2)))/2, "     num1 :", int(num_1, 2))
            print ("count: ", count)
            count = count +1
            
        


# In[ ]:


double


# In[ ]:





# In[ ]:


for i in range(len(str(num_1))):
            if num_1[i] == str(1):
                qc.x(qr[i])


# In[83]:


x = []
for elem in '1000110010111010100101111010110000100010010101011100001010001100000101101100011110000100011100000000':
    x.append(elem)


# In[84]:


x


# In[85]:


arr2 =  np.asarray(x).reshape(shape)


# In[ ]:





# In[ ]:





# In[ ]:


for j in range(len(flat_arr)):
    qc.measure(qr[j], cr[j])


print("hello")
simulator = Aer.get_backend('qasm_simulator')
print("hello")
job = execute(qc, simulator, shots=5)
print("hello")
results = job.result()
print("hello")
stats = results.get_counts(qc)

print("hello")

vector = np.matrix(flat_arr)



# In[ ]:





# In[87]:



arr2 = np.asarray(vector).reshape(shape)


# In[88]:


arr2


# In[89]:


plt.imsave('filename1.jpeg',arr2, cmap=cm.gray)


# In[25]:


A1


# In[24]:


arr2


# In[94]:


x = []
for bitString in stats: # loop over all results
    for k in range(len(bitString)-1):
        x.append(int(bitString[k:k+1]))
x.append(1)
x = np.array(x)

x = x[0:2500]

vector = np.matrix(x)
shape = new_A.shape
arr2 = np.asarray(vector).reshape(shape)


# In[42]:


img = plt.imshow(double)
plt.show()


# In[43]:


img = plt.imshow(new_img)
plt.show()


# In[ ]:




