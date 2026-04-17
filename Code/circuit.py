from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
def teleportation_circuit(y):
    cr = ClassicalRegister(3)
    qr = QuantumRegister(3)
    qc=QuantumCircuit(qr,cr)
    qc.initialize(y, 0)
    qc.barrier()
    qc.h(qr[1])
    qc.cx(qr[1],qr[2])
    qc.barrier()

    qc.cx(qr[0],qr[1])
    qc.h(qr[0])
    qc.barrier()

    qc.measure(qr[0],cr[0])
    qc.measure(qr[1],cr[1])
    qc.barrier()
    with qc.if_test((cr[1],1)):
        qc.x(qr[2])
    with qc.if_test((cr[0],1)):
        qc.z(qr[2])
    return qc