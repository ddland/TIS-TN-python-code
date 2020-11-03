#!/usr/bin/env python

from sympy import pi, cos, sin, sqrt, arg, exp, Abs, S
from sympy import integrate, Rational, nfloat, conjugate, Symbol
from sympy.functions.special.delta_functions import Piecewise

t = Symbol('t')


def Heaviside(arg):
    ''' Heaviside die ook op arg=0 gedefinieerd is '''
    return Piecewise((0, arg < 0), (1, arg >= 0))


# functies om de fourier-reeks coefficienten uit te rekenen
def an(f, T, n, omega0):
    return 2/T*integrate(f*cos(n*omega0*t), (t, 0, T))


def bn(f, T, n, omega0):
    return 2/T*integrate(f*sin(n*omega0*t), (t, 0, T))


def a0(f, T, omega0):
    return 1/T*integrate(f, (t, 0, T)).nsimplify()


def fourreeks(f, T, N):
    N += 1  # voor Maple
    a = (N-1)*[0]
    b = (N-1)*[0]
    omega0 = 2*pi/T
    som = a0(f, T, omega0)
    for n in range(1, N):
        a[n-1] = an(f, T, n, omega0)
        b[n-1] = bn(f, T, n, omega0)
        som += (a[n-1]*cos(n*omega0*t) + b[n-1]*sin(n*omega0*t)).nsimplify()
    return som, a, b


def spec(a, b, T):
    omega0 = 2*pi/T
    mag = [nfloat(sqrt(a[i]**2 + b[i]**2)) for i in range(len(a))]
    phi = len(a)*[0]
    for i in range(len(b)):
        if a[i] == S.Zero:
            phi[i] = 0
        else:
            phi[i] = nfloat(arg(a[i] - S.ImaginaryUnit*b[i]))
    mag.insert(0, a0(f, T, omega0))
    if mag[0] >= 0:
        phi.insert(0, 0)
    else:
        phi.insert(0, pi)
    return (mag, phi)


def periodiek(f, T, N):
    som = S(0)
    for n in range(N):
        som += (Heaviside(t-n*T) - Heaviside(t-(n+1)*T))*f.replace(t, t-n*T)
    return som


def plot_color(p):
    color = ['r', 'b', 'g', 'y', 'm']
    Nc = len(color)
    for i, pc in enumerate(p):
        pc.line_color = color[i % Nc]


if __name__ == '__main__':
    from sympy.plotting import plot
    import matplotlib.pyplot as plt

    f = Heaviside(t+1) - Heaviside(t-1)
    T = 4
    N = 5
    teind = 10
    som, a, b = fourreeks(f, T, N)
    mag, phase = spec(a, b, T)
    plot(som, (t, 0, teind))
    p = plot(periodiek(f, T, int(teind/T)+1), som, (t, 0, teind),
             adaptive=False, show=False)
    plot_color(p)
    p.show()
    phase, mag = spec(a, b, T)
    plt.figure()
    plt.subplot(2, 1, 1)
    plt.plot(range(len(phase)), phase)
    plt.subplot(2, 1, 2)
    plt.plot(range(len(mag)), mag)
    plt.show()
