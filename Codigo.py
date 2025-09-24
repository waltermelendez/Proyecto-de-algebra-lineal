import numpy as np

#Matriz inicial a resolver
A = np.array([(-2,1,1),(1,-2,1),(1,1,-2)])

B = np.array([[(150)],[(200)],[(150)]])



#Unir las dos matrices
def Unir(A,B):
    unir =np.concatenate((A,B),axis=1)
    AB =np.copy(unir)


    tamanio = np.shape(unir)
    n = tamanio[0]
    m = tamanio[1]

    for i in range (0,n-1,1):
        columna = abs(AB[i:,i])
        maximo = np.argmax(columna)

        if (maximo != 0):
            temporal=np.copy(AB[i,:])
            AB =AB[maximo+i,:]
            AB[maximo+i,:]= temporal
    return AB
    
      


#Parte en donde se empieza a eliminar las filas del arreglo "AB"


#Imprimir resultados
print("Matriz, parte A")

print(A)

print("Matriz parte B")

print(B)

print("Matriz A mas B")
print(Unir(A,B))