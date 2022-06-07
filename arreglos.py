
import numpy as np 
import numpy as rd
matriz = np .diag([1,1,1])#crea matriz de 3x3 llena de enteros 
print(matriz)

for i in range (3):
    for j in range (3):
        matriz[i][j] = rd.randint(0, 100)
        
print(matriz)
    