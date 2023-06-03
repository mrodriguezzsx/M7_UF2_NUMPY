import numpy as np

# Creacio Array simple
def array1():
    array1 = np.array([88, 23, 39, 41])
    print('Exercici 2a')
    print(array1)
    print('Dimensio de la Matriu: ', array1.ndim)
    print('Tamany de la Matriu: ', array1.shape)
    print("Numero total d'elements: ", array1.size)
    print("Tipus d'elements interns: ", array1.dtype)
    print()

def array2():
    array2 = np.array([[76.4, 21.7, 38.4], [41.2, 52.8, 68.9]])
    print('Exercici 2b')
    print(array2)
    print('Dimensio de la Matriu: ', array2.ndim)
    print('Tamany de la Matriu: ', array2.shape)
    print("Numero total d'elements: ", array2.size)
    print("Tipus d'elements interns: ", array2.dtype)
    print()

def array3():
    array3 = np.array([12, 4, 9, 8]).reshape(4, 1)
    print('Exercici 2c')
    print(array3)
    print('Dimensio de la Matriu: ', array3.ndim)
    print('Tamany de la Matriu: ', array3.shape)
    print("Numero total d'elements: ", array3.size)
    print("Tipus d'elements interns: ", array3.dtype)
    print()