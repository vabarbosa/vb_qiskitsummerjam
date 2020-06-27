from PIL import Image
import cv2
from numpy import*
import matplotlib.cm as cm
import numpy as np
import matplotlib.pyplot as plt
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


# make a 1-dimensional view of arr
flat_arr = new_A.ravel()
print(sum(flat_arr), len(flat_arr))


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
qr =  QuantumRegister(len(flat_arr), 'qr')
cr = ClassicalRegister(len(flat_arr),'cr')
qc = QuantumCircuit(qr, cr)

# rightmost eight (qu)bits have ')' = 00101001

for num, k in enumerate(flat_arr):
    if (k == 1):

        qc.x(qr[num])

# second eight (qu)bits have superposition of
# '8' = 00111000
# ';' = 00111011
# these differ only on the rightmost two bits

# measure
for j in range(len(flat_arr)):
    qc.measure(qr[j], cr[j])

# run and get results
simulator = Aer.get_backend('qasm_simulator')
job = execute(qc, simulator, shots=1024)
results = job.result()

stats = results.get_counts(qc)
characterDict = {}
import matplotlib.pyplot as plt
plt.rc('font', family='monospace')
for char in characterDict.keys():
    # plot all characters on top of each other with alpha given by how often it turned up in the output
    plt.annotate( char, (0.5,0.5), va="center", ha="center", color = (0,0,0,characterDict[char]), size = 300)
plt.axis('off')
plt.show()

for char in characterDict.keys():
    if (characterDict[char]>0.05):
        print(characterDict[char],char)



vector = np.matrix(flat_arr)
arr2 = np.asarray(vector).reshape(shape)

print(arr2)