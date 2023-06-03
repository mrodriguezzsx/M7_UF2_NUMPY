import numpy as np

def matriuFinal():
    print('Exercici 4')
    matriu = np.array([np.random.randint(low=0, high=80, size=(4, 3))])
    print("Es crea la matriu amb valors aleatoris entre el 0 y el 80. "
          "Les dimensions d'aquesta matriu son de 4 files amb 3 valors a cada fila: ")
    print(matriu)
    print()
    matriu = np.transpose(matriu, (0, 2, 1))
    print("Es coloca la ultima fila de la matriu com una nova columa a la dreta: ")
    print(matriu)

