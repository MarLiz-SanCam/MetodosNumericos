# Método de Newton Raphson para sistemas de ecuaciones 

import numpy as np


F = lambda x1, x2: [x1**2 - x2**2 + 2*x2, 2*x1 + x2**2 - 6]
J = lambda x1, x2: [[2*x1, -2*x2 + 2],[2,2*x2]]

# Procedimiento

def newton_raphson(F, j, x0, tolera):
    x = x0
    error = 1e3
    n = 0
    while error > tolera:
        dx = -np.linalg.solve(J(*x),F(*x))
        error = np.linalg.norm(dx)/np.linalg.norm(x)
        x += dx;
        n += 1
    print("Iteraciones: ",n)
    # return x
    print(x)

newton_raphson(F, J, [1,5], 1e-5)

# Mar Liz ~