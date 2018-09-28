# voorbeeld code om een plotje te genereren met foutenvlaggen en datafit

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import TISTNplot as TN # TISTNplot.py in huidige directory of in python path.

sigma = True # neem meetfout wel (True) of niet (False) mee in de datafit

# fit functies
def fit_func_linear(x, a, b):
    ''' y = a*x + b '''
    return a*x + b

func = fit_func_linear

# data
x = np.arange(10)
y = [7, 10, 14, 18, 22, 40, 25, 30, 33, 40]
y_error = [1, 1, 1, 3, 3, 1, 3, 5, 5, 5] # +/- meetfout

# plot data
plt.errorbar(x, y, yerr=y_error, fmt='ok', label='meetdata', capsize=5)
plt.grid()
TN.label_x('x', 'm', plt.gca())
TN.label_y('v', 'm/s', plt.gca())

# datafit
p_start = [4,3] # helling, offset eerste schatting
if sigma: # 
    p_opt, p_cov = curve_fit(func, x, y, sigma=y_error, p0=p_start, absolute_sigma=True)
else:
    p_opt, p_cov = curve_fit(func, x, y, p0=p_start, absolute_sigma=True)

fit_error = np.sqrt(np.diag(p_cov))

# plot datafit
fitlabel = 'fit: y=%5.2fx + %5.2f'%(p_opt[0], p_opt[1])
fitlabel = fitlabel.replace('.',',')
plt.plot(x, func(x, *p_opt), '-k', label=fitlabel)
plt.plot(x, func(x, *(p_opt + 3*fit_error)), '-.k', label='$3\sigma$ onzekerheid in model')
plt.plot(x, func(x, *(p_opt - 3*fit_error)), '-.k')

# plot legenda
plt.legend(loc=0)

# fix axis
TN.fix_axis(plt.gca())
plt.tight_layout()

# geef figuur weer of sla het op!
plt.show()

