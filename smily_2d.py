import sys
sys.path.append("../../qiskit-sdk-py/")
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
import math
from qiskit import(
  QuantumCircuit,
  execute,
  Aer)

from qiskit import IBMQ

# set up registers and program
qr =  QuantumRegister(16, 'qr')
cr = ClassicalRegister(16,'cr')
qc = QuantumCircuit(qr, cr)

# rightmost eight (qu)bits have ')' = 00101001
qc.x(qr[0])
qc.x(qr[3])
qc.x(qr[5])

# second eight (qu)bits have superposition of
# '8' = 00111000
# ';' = 00111011
# these differ only on the rightmost two bits
qc.h(qr[9]) # create superposition on 9
qc.cx(qr[9],qr[8]) # spread it to 8 with a cnot
qc.x(qr[11])
qc.x(qr[12])
qc.x(qr[13])

# measure
for j in range(16):
    qc.measure(qr[j], cr[j])

# run and get results
simulator = Aer.get_backend('qasm_simulator')
job = execute(qc, simulator, shots=1024)
results = job.result()
stats = results.get_counts(qc)
characterDict = {}
for bitString in stats: # loop over all results
    char1 = chr(int( bitString[0:8] ,2)) # get string of leftmost 8 bits an convert to an ASCII character
    char2 = chr(int( bitString[8:16] ,2)) # same for string of leftmost 8 bits
    characterDict[ char1 + char2 ] = stats[bitString] / 1024
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