import numpy as np

def matriuFinal():
    matriu = np.array([np.random.randint(low=0,high=80, size=(4,3))])
    print(matriu)
    print()
    matriu = np.transpose(matriu, (0, 2, 1))
    print(matriu)