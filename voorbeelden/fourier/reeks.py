import fourier_coeff as fc
from sympy.plotting import plot
from sympy import Symbol
from matplotlib import pyplot as plt

t = Symbol("t")


f = fc.Heaviside(t + 1) - fc.Heaviside(t - 1)
T = 4
N = 5
teind = 10
reeks, a, b = fc.fourreeks(f, T, N)
p = plot(
    fc.periodiek(f, T, teind),
    reeks,
    (t, 0, teind),
    show=False,
)
fc.plot_color(p)
print("reeks:\n", reeks)
p.show()

phase, mag = fc.spec(f, a, b, T)

plt.figure()

plt.subplot(2, 1, 1)
plt.plot(range(len(phase)), phase)

plt.subplot(2, 1, 2)
plt.plot(range(len(mag)), mag)

plt.show()
