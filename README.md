# TIS-TN-python

Hier staan python scripts en modules die kunnen helpen gedurende de studie TN bij de Haagse Hogeschool.

## TISTNplot.py

Script om significante cijfers en gebruik van machten volgens het document Labjournaal, Meetrapport en Verslag weer te geven. 
Punten zijn vervangen door komma's en X- en Y-as zijn afzonderlijk van precisie te voorzien.

### Gebruik
Een minimaal voorbeeld is hieronder gegeven:
```python
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
```

De matplotlib formatter voor de assen wordt afzonderlijk voor de x- en y-as aangemaakt. Hierin geef je aan hoeveel significante cijfers op de assen geplaatst moeten worden.

Als de x-as (of de y-as) uit tijd-data bestaat en je wilt bijvoorbeeld data-time labels op de assen, kan je de formatter voor die as niet aanpassen. Door bijvoorbeeld de regel 
```python
formatterY = TN.TNFormatter(2) # zet de y-as op 2 cijfers significant
``` 
weg te laten wordt alleen de x-as opgemaakt.

## Fourier
Functies om Fouriercoefficienten analytisch uit te rekenen. De module gebruikt sympy om de integralen van willekeurige (periodieke) functies uit te voeren en geeft uiteindelijk de reeksontwikkeling of de $a_n$ en $b_n$ coefficienten terug.

## Data analyse
Een voorbeeld script om vanuit een Excel dataset via panda, matplotlib en scipy een figuur te genereren met daarin een model aan de data gefit. De fouten in de afhankelijke waarden zijn meegenomen in het bepalen van de coefficienten van het model.
