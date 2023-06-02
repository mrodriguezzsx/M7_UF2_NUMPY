import numpy as np

import exercici1
import exercici2
import exercici3
import exercici4_Matias

# Crida de la funcio del exercici 1
exercici1.diagonal()

# Crida de les funcions de l'exercici 2
exercici2.array1()
exercici2.array2()
exercici2.array3()

# Crida de les funcions de l'exercici 3
# Creacio de l'Array amb 100 valors Random
print('Exercici 3')
array = np.array([np.random.randn(100)],dtype='int32')
print(array)

exercici3.generacioMatriu(array)
exercici3.valorMax(array)
exercici3.valorMin(array)

# Crida de la funcio de l'exercici 4

exercici4_Matias.matriuFinal()