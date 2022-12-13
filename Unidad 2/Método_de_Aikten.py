#Método de Aikten

from math import exp, factorial
from numpy import cumsum

def aitken(s0, s1, s2):
    return s2 - (s2 - s1)**2/(s2 - 2*s1 + s0)

def exp_parcial(x, N):
    terms = [x**n/factorial(n) for n in range(N)]
    return cumsum(terms)

x, N = 0.3, 6
partial = exp_parcial(x, N)

p = partial[-1]
a = aitken( partial[-3], partial[-2], partial[-1] )

# análisis del error 
error_p = exp(x) - p
error_a = exp(x) - a
print(error_p, error_a, error_p/error_a)

# Mar Liz ~