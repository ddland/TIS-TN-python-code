import matplotlib.pyplot as plt
import TISTNplot as TN

formatterX = TN.TNFormatter(3) # zet de x-as op 3 cijfers significant
formatterY = TN.TNFormatter(2) # zet de y-as op 2 cijfers significant

fig,ax = plt.subplots() # maak 1 figuur aan

ax.yaxis.set_major_formatter(formatterY) # as opmaak volgens eerder 
ax.xaxis.set_major_formatter(formatterX) # gedefinieerde formatter

plt.plot(range(10), range(10)) # plot 10 getallen (0-9 uitgezet tegen 0-9)

plt.tight_layout() # plaats (net) voldoende witruimte rond het figuur

plt.savefig('fig.pdf', bbox_inches='tight') # maak figuur niet groter dan 
					    # nodig is
plt.show()
