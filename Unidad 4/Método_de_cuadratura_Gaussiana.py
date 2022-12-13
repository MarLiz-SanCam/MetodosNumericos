# Método de la cuadratura de Gauss (de dos puntos)

import numpy as np
import matplotlib.pyplot as plt

def CuadraturaGauss(funcionx,a,b):
    x0 = -1/np.sqrt(3)
    x1 = -x0
    xa = (b+a)/2 + (b-a)/2*(x0)
    xb = (b+a)/2 + (b-a)/2*(x1)
    area = ((b-a)/2)*(funcionx(xa) + funcionx(xb))
    return(area)

# INGRESO
fx = lambda x: np.sqrt(x)*np.sin(x)

a = 1
b = 3
tramos = 4

# PROCEDIMIENTO
muestras = tramos+1
xi = np.linspace(a,b,muestras)
area = 0
for i in range(0,muestras-1,1):
    deltaA = CuadraturaGauss(fx,xi[i],xi[i+1])
    area = area + deltaA

# SALIDA
print('Integral: ', area)
# Mar Liz ~