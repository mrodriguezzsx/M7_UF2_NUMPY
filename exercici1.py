import numpy as np

# Creacio de la matriu 49x49 amb la diagonal demanada
def diagonal():
    diagonal = np.diag(np.arange(50))
    print('Exercici 1')
    print(diagonal)
    print()
    print('Dimensio de la Matriu: ', diagonal.ndim)
    print('Tamany de la Matriu: ', diagonal.shape)
    print("Numero total d'elements: ", diagonal.size)
    print("Tipus d'elements interns: ", diagonal.dtype)
    np.save('exercici1.npy', diagonal)

