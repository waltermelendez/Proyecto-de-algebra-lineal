import numpy as np

#No dinamica
A = np.array([(-2,1,1),(1,-2,1),(1,1,-2)])

B = np.array([[(150)],[(200)],[(150)]])

#forma dinaminca
'''
print("Ingresa el orden de la matriz a calcular ")
filasA, columnasA = int(input()), int(input())
'''



'''
#Creando la matriz vacia de A
A =[]
for i in range(columnasA):
    A.append([0]*columnasA)

#Dar valores a la matriz
print("Ingrese los valores de la matriz A")
for fila in range(filasA):
    for columnas in range(columnasA):
        A[filasA][columnasA]=float(input(f'Ingrese un numero {fila}, {columna}: '))
'''

'''
#Creando la matriz vacia de B
print("Ingresa el orden de la matriz a crear ")
columnaB = int(input())

b=[]
for i in range(columnaB):
    b.append([0]*columnaB)

#Dar valores a la matriz B
for columna in range(columnaB):
        b[columna]=float(input(f'Ingrese un numero  {columna}: '))
B = np.vstack(b)
print(B)

'''



def Determinante(A):
    determinante = np.linalg.det(A);
    if(determinante==0.0):
        return False
    else:
        return True

if(Determinante(A)):
    print("")
else:
    print("")

 
#Calcular el determinante


