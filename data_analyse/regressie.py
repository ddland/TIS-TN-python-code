# voorbeeld code om data in te lezen uit excel, een plotje te genereren met
# foutenvlaggen en datafit

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import TISTNplot as TN  # TISTNplot.py in huidige directory of in python path.

sigma = True # neem meetfout wel (True) of niet (False) mee in de datafit

sigma_plot = 3 # 3 sigma onzekerheid in model parameters

# fit functies
def fit_func_linear(x, a, b):
    ''' y = a*x + b '''
    return a*x + b


func = fit_func_linear

# testdata binnen python data
# x = np.arange(10)
# v = [7, 10, 14, 18, 22, 40, 25, 30, 33, 40]
# v_error = [1, 1, 1, 3, 3, 1, 3, 5, 5, 5] # +/- meetfout

# lees data in uit excel file:
data = pd.read_excel("data.xlsx")
x = data['x'].values
v = data['v'].values
v_error = data['v_err'].values*3

# plot data
plt.errorbar(x, v, yerr=v_error, fmt='ok', label='meetdata', capsize=5)
plt.grid()
TN.label_x('x', 'm', plt.gca())
TN.label_y('v', 'm/s', plt.gca())

# datafit
if sigma:
    p_opt, p_cov = curve_fit(func, x, v, sigma=v_error, absolute_sigma=True)
else:
    p_opt, p_cov = curve_fit(func, x, v, absolute_sigma=True)

fit_error = np.sqrt(np.diag(p_cov))
# plot datafit
fitlabel = 'fit: v=%5.2fx + %5.2f' % (p_opt[0], p_opt[1])
# komma's in plaats van punten als decimaal operator
fitlabel = fitlabel.replace('.', ',')
plt.plot(x, func(x, *p_opt), '-k', label=fitlabel)

# vul ymax/ymin in met behulp van sigma maal onzekerheid in fit parameters
ymax = func(x, *(p_opt+fit_error*sigma_plot))
ymin = func(x, *(p_opt-fit_error*sigma_plot))
ydata = func(x, *p_opt)

for ii in range(len(fit_error)):
    rc = p_opt[0] + sigma_plot*fit_error[0]
    fit_error[0] = -fit_error[0]
    for jj in range(len(fit_error)):
        offset = p_opt[1] + sigma_plot*fit_error[1]
        fit_error[1] = -fit_error[1]
        yerr = func(x, rc, offset)
        maxTrue = yerr > ymax
        minTrue = yerr < ymin
        ymax[yerr > ymax] = yerr[yerr > ymax]
        ymin[yerr < ymin] = yerr[yerr < ymin]

# maximum error
plt.plot(x, ymax, '-.k', label='maximale $3\sigma$ onzekerheid in model')
plt.plot(x, ymin, '-.k')
# just 3 sigma of error of all parameters added / substracted
#plt.plot(x, func(x, *(p_opt-fit_error*sigma_plot)), '--r', label='error in parameters')
#plt.plot(x, func(x, *(p_opt+fit_error*sigma_plot)), '--r')

# plot legenda
plt.legend(loc=0)

# gebruik TISTN plot om de assen netjes weer te geven
TN.fix_axis(plt.gca())
plt.tight_layout()

# geef figuur weer of sla het op!
plt.savefig("regressie.pdf", bbox_inches='tight', density=300)
plt.savefig("regressie.png", bbox_inches='tight', density=300)
plt.show()
