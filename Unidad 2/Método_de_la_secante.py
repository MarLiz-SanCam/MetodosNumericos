
import numpy as np

def secante_tabla(fx,xa,tolera):
    dx = 4*tolera
    xb = xa + dx
    tramo = dx
    tabla = []
    while (tramo>=tolera):
        fa = fx(xa)
        fb = fx(xb)
        xc = xa - fa*(xb-xa)/(fb-fa)
        tramo = abs(xc-xa)
        
        tabla.append([xa,xb,xc,tramo])
        xb = xa
        xa = xc

    tabla = np.array(tabla)
    return(tabla)

# ---------------------
# INGRESO
fx = lambda x: x**3 - np.exp(x)

a  = -1
b  = 2
xa = 1.5
tolera = 0.001
tramos = 100

# PROCEDIMIENTO
tabla = secante_tabla(fx,xa,tolera)
n = len(tabla)
raiz = tabla[n-1,2]

# SALIDA
np.set_printoptions(precision=4)
print('[xa ,  xb ,    xc ,    tramo]')
for i in range(0,n,1):
    print(tabla[i])
print('\nraiz en: ', raiz)


# ~ Mar Liz ~