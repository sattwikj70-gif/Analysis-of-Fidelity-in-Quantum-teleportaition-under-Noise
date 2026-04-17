from qiskit.quantum_info import state_fidelity,partial_trace,DensityMatrix

def fidelity(out,y):
    final_state = DensityMatrix(out)
    reduced_state = partial_trace(final_state, [0,1])
    original_state = DensityMatrix(y)
    x=state_fidelity(original_state, reduced_state)
    return x