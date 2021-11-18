#!/usr/bin/env python

from sympy import pi, cos, sin, sqrt, arg, exp, Abs, S
from sympy import integrate, Rational, nfloat, conjugate, Symbol
from sympy.functions.special.delta_functions import Heaviside
from sympy.plotting import plot
import matplotlib.pyplot as plt

t = Symbol("t", real=True)  # anders complexe tijd!


def ac(f, T, n, omega0):
    return (
        1
        / T
        * integrate(
            f * exp(-S.ImaginaryUnit * n * omega0 * t), (t, -T / 2, T / 2)
        ).nsimplify()
    )


def fourreeks(f, T, N):
    N += 1  # voor Maple
    a = (N - 1) * [0]
    b = (N - 1) * [0]
    omega0 = 2 * pi / T
    som = a0(f, T, omega0)
    for n in range(1, N):
        a[n - 1] = an(f, T, n, omega0)
        b[n - 1] = bn(f, T, n, omega0)
        som += (
            a[n - 1] * cos(n * omega0 * t) + b[n - 1] * sin(n * omega0 * t)
        ).nsimplify()
    return som, a, b


def cfourreeks(f, T, N):
    """Let op! Periode tussen -T/2 en T/2!"""
    N += 1
    omega0 = 2 * pi / T
    cp = (N - 1) * [0]
    cn = (N - 1) * [0]
    mag = (2 * N - 1) * [0]
    phase = (2 * N - 1) * [0]
    c0 = 1 / T * integrate(f, (t, -T / 2, T / 2)).nsimplify()
    mag[N - 1] = Abs(nfloat(c0))
    phase[N - 1] = 0
    som = c0
    for n in range(1, N):
        cp[n - 1] = ac(f, T, n, omega0)
        cn[n - 1] = conjugate(cp[n - 1])
        mag[N - n - 1] = 2 * Abs(nfloat(cn[n - 1]))
        mag[N + n - 1] = 2 * Abs(nfloat(cp[n - 1]))
        phase[N - n - 1] = arg(cn[n - 1])
        phase[N + n - 1] = arg(cp[n - 1])
        som += cp[n - 1] * exp(S.ImaginaryUnit * n * omega0 * t) + cn[n - 1] * exp(
            -S.ImaginaryUnit * n * omega0 * t
        )
    cp.insert(0, c0)
    return som, mag, phase


def periodiek(f, T, N):
    som = S(0)
    for n in range(N):
        som += (Heaviside(t - n * T) - Heaviside(t - (n + 1) * T)) * f.replace(
            t, t - n * T
        )
    return som


if __name__ == "__main__":
    f = (Heaviside(t + pi) - Heaviside(t)) * (t + pi)
    T = 2 * pi
    N = 5
    fr, mag, phase = cfourreeks(f, T, N)
    plot(f, (t, -2 * pi, 2 * pi), adaptive=False)
    plt.show()
    plt.figure()
    plt.subplot(2, 1, 1)
    plt.stem(range(-N, N + 1), mag, "r")
    plt.subplot(2, 1, 2)
    plt.stem(range(-N, N + 1), phase, "b")
    plt.show()
