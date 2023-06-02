import numpy as np

# Creacio de la matriu 49x49 amb la diagonal demanada
def diagonal():
    diagonal = np.diag(np.arange(50))
    print(diagonal)
    np.save('exercici1.npy',diagonal)

