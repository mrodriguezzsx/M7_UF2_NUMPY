import numpy as np

# Creacio de la matriu 49x49 amb la diagonal demanada
def diagonal():
    diagonal = np.diag(np.arange(50))
    print('Exercici 1')
    print(diagonal)
    print()
    np.save('exercici1.npy',diagonal)

