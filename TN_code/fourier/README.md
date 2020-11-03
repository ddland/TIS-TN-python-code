# Fourier analyse met Python

De code in dit repository is functioneel dezelfde code als de Maple code in het
wiskunde boek gebruikt bij de Fourier-Wiskunde lessen.

##  Voorbeeld gebruik

```python
import fourier_coeff as fc

from sympy import Symbol
t = Symbol('t')

from sympy.plotting import plot
import matplotlib.pyplot as plt
    
f = fc.Heaviside(t+1) - fc.Heaviside(t-1)
T = 4 
N = 5
reeks, a, b = fc.fourreeks(f,T,N)
p=plot(fc.periodiek(f,T,10), reeks, (t,0,10), adaptive=False)
fc.plot_color(p)
plt.show()
print(reeks)
```
