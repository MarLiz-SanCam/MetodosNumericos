# Método de Jacobi

import numpy as np

# INGRESO
A =  np.array([[3., -1, -1],
               [-1, 3,-1],
               [2, 1, 4]])

B = [1, 3, 7]
xi = [1/3, 1, 7/4]
tolera = 0.01
iteramax = 50
# PROCEDIMIENTO
A = np.array(A, dtype= float)
B = np.array(B, dtype= float)
xi = np.array(xi,dtype= float)
# print(A)
# print(B)


tamano = np.shape(A)
n = tamano[0]
m = tamano[1]
Xin = np.zeros(n, dtype=float)
diferencia = np.ones(n, dtype=float)
errado = 2*tolera
itera = 0

while not(errado <= tolera or itera > iteramax ):
    for i in range(0,n,1):
        nuevo = B[i]
        for j in range(0,m,1):
            if(i != j):
                nuevo = nuevo - A[i,j]*xi[j]
        nuevo = nuevo/A[i, i]
        diferencia[i] = np.abs(nuevo - xi[i])
        Xin[i] = nuevo
    errado = np.max(diferencia)
    xi = np.copy(Xin)
    itera = itera + 1


# 
print(A)
print(B)
print(Xin)
print(diferencia)
print(errado)


# Mar Liz ~