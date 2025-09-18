#pip install numpy
import numpy as np
import matplotlib.pyplot as plt

at = np.array([(1,2,2,3),(1,0,-2,0),[3,-2,2,-2],(4,-3,8,2)])

y = np.trace(at) # encontrar la trace de  la matriz

print({y})
print("La traza de la matriz es la de arriba.")
#Multiplicacion de matrices

A = np.array([[4,3,2],[5,1,9]])
B = np.array([(5,4,1),(7,9,3),(2,1,2)])

C=np.matmul(A,B)

print(C)

print("-----------------------------------------------")

Lista= [31,28,29,19]
array = np.array(Lista)

#Propiedades

print(B.shape)
print(A.dtype)

print(A.size)

#Cambio de datos
D = np.array(B,dtype=np.int32)

Cero = np.zeros((3,2))
print(Cero)
print("-----------------------------------------------")
unos =np.ones((3,2))
print(unos)

nis = np.empty((3,2))#Valores muy pequenio
print("-----------------------------------------------")
print(nis)


#Crear arrlgos

F = np.arange(10)
print(F)

#Matric como crear una matriz
print("-----------------------------------------------")
G = np.arange(10).reshape(2,5)
print(G)

H=np.arange(10,20,2)

from numpy import pi

rad = np.linspace(0,2*pi,100)
print(rad)
#Como graficar funciones
seno = np.sin(rad)
coseno = np.cos(rad)
#plt.plot(seno,coseno)
#plt.show()

XX = np.arange(1,10)
#plt.plot(seno)
#plt.show()

a= np. linspace(10, 28,6)
b= np. linspace(5,25,6)
x =a+b
print(x)
d = np.concatenate((a,b))
x.sort
print("#####")
print(x)