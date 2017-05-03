#!/usr/bin/env python

def to_precision(x,p):
    """
    returns a string representation of x formatted with a precision of p
    Based on the webkit javascript implementation taken from here:
    https://code.google.com/p/webkit-mirror/source/browse/JavaScriptCore/kjs/number_object.cpp
    """
    import math
    x = float(x)

    if x == 0.:
        if (p-1) > 0:
            return '$0,' + '0'*(p-1) +'$'
        else:
            return '$0$'
    out = []

    if x < 0:
        out.append("-")
        x = -x

    e = int(math.log10(x))
    tens = math.pow(10, e - p + 1)
    n = math.floor(x/tens)

    if n < math.pow(10, p - 1):
        e = e -1
        tens = math.pow(10, e - p+1)
        n = math.floor(x / tens)

    if abs((n + 1.) * tens - x) <= abs(n * tens -x):
        n = n + 1

    if n >= math.pow(10,p):
        n = n / 10.
        e = e + 1
        
    m = "%.*g" % (p, n)

    if e < -2 or e >= p:
        out.append(m[0])
        if p > 1:
            out.append(",")
            out.extend(m[1:p])
        out.append('\cdot 10^{')
        out.append(str(e))
        out.append('}')
    elif e == (p -1):
        out.append(m)
    elif e >= 0:
        out.append(m[:e+1])
        if e+1 < len(m):
            out.append(",")
            out.extend(m[e+1:])
    else:
        out.append("0,")
        out.extend(["0"]*-(e+1))
        out.append(m)
    outstr = "".join(out)
    return '$' + outstr + '$'

PRECISION_Y = 2 # toegang tot variabele buiten module
def funcy(data, pos):
    return to_precision(data,PRECISION_Y)

PRECISION_X = 2 # toegang tot variabele buiten module
def funcx(data, pos):
    return to_precision(data,PRECISION_X)

from matplotlib.ticker import FuncFormatter
def fix_axis(ax):
	formattery = FuncFormatter(funcy)
	formatterx = FuncFormatter(funcx)
	ax.yaxis.set_major_formatter(FuncFormatter(formattery))
	ax.xaxis.set_major_formatter(FuncFormatter(FuncFormatter(formatterx)))

def label_x(grootheid, eenheid, ax,haak='[]'):
    ax.xaxis.set_label_text('$%s \, %s\mathrm{%s}%s$'%(grootheid, haak[0], eenheid, haak[1])) 

def label_y(grootheid, eenheid, ax,haak='[]'):
    ax.yaxis.set_label_text('$%s \, %s\mathrm{%s}%s$'%(grootheid, haak[0], eenheid, haak[1])) 

def test_to_precision():
    numbers = [0, 0.1, 0.4, 0.232, 0.0, 1.242323, 9.999, -1343213.234]
    for number in numbers:
        print(number, 3, to_precision(number, 3))
        print(number, 7, to_precision(number, 7))
        print(number, 1, to_precision(number, 1))
		


if __name__ == '__main__':
    test_to_precision()
    
