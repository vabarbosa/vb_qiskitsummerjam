from PIL import Image
from numpy import*
import matplotlib.cm as cm
import numpy as np
import matplotlib.pyplot as plt
#flat_arr = new_A.ravel()
#print(sum(flat_arr), len(flat_arr))



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


from PIL import Image
from numpy import*
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

file_1 = "download.png"
size = 10
A1, A2 = pixelate(file_1, file_1, size)


img = np.asarray(A1)
new_img = img.reshape((img.shape[0]*img.shape[1]), img.shape[2])
new_img = new_img.transpose()


img = np.asarray(A1)
new_img = img.reshape((img.shape[0]*img.shape[1]), img.shape[2])
new_img = new_img.transpose()

# set up registers and program
qr =  QuantumRegister(15, 'qr')
cr = ClassicalRegister(15,'cr')
qc = QuantumCircuit(qr, cr)



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


# IMPORT IMAGE AS new_img and new_img2



im1 = im1.resize(3, 100)
im2 = im2.resize(3, 100)

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
        num_2 = bin(new_img2[p][k])
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
img = plt.imshow(double)
plt.show()