import numpy as np

# Funcio per redimensionar l'Array
def generacioMatriu(array):
    print("Has de tenir en compte que hi ha 100 valors a l'array")
    # Peticio reshape per consola
    dimensio = input("Afegeix un valor per a la dimesio del Array: ")
    dimensio = int(dimensio)

    quantitat = input("Afegeix un valor per a la quantitat d'elements per array: ")
    quantitat = int(quantitat)
    # Apliquem la peticio
    array = array.reshape(dimensio, quantitat)
    print(array)

# Funcio per trobar el valor mes alt
def valorMax(array):
    maxNum = np.max(array)
    print("El valor màxim de l'array es: ", maxNum)

def valorMin(array):
    minNum = np.min(array)
    print("El valor minim de l'array es: ", minNum)
