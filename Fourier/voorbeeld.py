import fourier_coeff as fc
from sympy import Symbol
t = Symbol('t')

f = fc.Heaviside(t+1) - fc.Heaviside(t-1)
T = 4 
N = 5
reeks, a, b = fc.fourreeks(f,T,N)
print(reeks)
