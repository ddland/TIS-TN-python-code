import fourier_coeff as fc
from sympy import Symbol
from sympy.plotting import plot

t = Symbol('t')
f = fc.Heaviside(t+1) - fc.Heaviside(t-1)
T = 4
N = 5
reeks, a, b = fc.fourreeks(f, T, N)
p = plot(fc.periodiek(f, T, 10), reeks, (t, 0, 10), adaptive=False, show=False)
fc.plot_color(p)
p.show()
print(reeks)
