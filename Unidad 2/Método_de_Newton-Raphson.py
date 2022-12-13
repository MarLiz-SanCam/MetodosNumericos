# Método de Newton-Raphson

import numpy as np

# INGRESO
fx  = lambda x: np.exp(-x) - x
dfx = lambda x: - np.exp(-x) - 1

x0 = 0
tolera = 0.001

# PROCEDIMIENTO
tabla = []
tramo = abs(2*tolera)
xi = x0
while (tramo>=tolera):
    xnuevo = xi - fx(xi)/dfx(xi)
    tramo  = abs(xnuevo-xi)
    tabla.append([xi,xnuevo,tramo])
    xi = xnuevo

# convierte la lista a un arreglo.
tabla = np.array(tabla)
n = len(tabla)

# SALIDA
print("[  xi   xnuevo  tramo ]")
np.set_printoptions(precision = 4)
print(tabla)
print('\nraiz en: ', xi)
print('con error de: ',tramo)

# ~ Mar Liz ~