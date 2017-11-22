# Fourier analyse met Python

De code in dit repository is functioneel dezelfde code als de Maple code in het
wiskunde boek gebruikt bij de Fourier-Wiskunde lessen.

##  Voorbeeld gebruik

```python
import four_coeff as fc
from sympy import Symbol
t = Symbol('t')

f = fc.Heaviside(t+1) - Heaviside(t-1)
T = 4 
N = 5
reeks, a, b = fc.fourreeks(f,T,N)
print(reeks)
```
