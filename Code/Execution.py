from qiskit import transpile
from qiskit_aer import AerSimulator
from qiskit.quantum_info import random_statevector
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import sqrtm

from fidelity import fidelity
from circuit import teleportation_circuit
from Noise import noise_creation
from math import sqrt,floor
noise=np.linspace(0,1,101)
fidelities=[]
y=[1/sqrt(2),1/sqrt(2)]
for p in noise:
    noise_model=noise_creation(p)
    qc=teleportation_circuit(y)
    qc.save_density_matrix()
    backend = AerSimulator(method='density_matrix', noise_model=noise_model)
    compiled_circuit = transpile(qc, backend)
    result = backend.run(compiled_circuit)
    out = result.result().data(0)['density_matrix']
    fid=fidelity(out,y)
    fidelities.append(fid)
    print('fidelity=',fid,'noise=',round(p*100),'%')
plt.plot(noise,fidelities)
plt.xlabel('Noise strength')
plt.ylabel('fidelity')
plt.title("Teleportation Fidelity vs Noise")
plt.show()
