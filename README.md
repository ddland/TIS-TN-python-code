# TIS-TN-python

Hier staan python scripts en modules die kunnen helpen gedurende de studie TN bij de Haagse Hogeschool.

## TISTNplot.py

Script om significante cijfers en gebruik van machten volgens het document Labjournaal, Meetrapport en Verslag weer te geven. \\
Punten zijn vervangen door komma's en X- en Y-as zijn afzonderlijk van precisie te voorzien.

### Gebruik
import matplotlib.pyplot as plt
import TISTNplot as hhs
hhs.PRECISION_Y = 3 # zet y-as op 3 cijfes significant (standaard = 2)

plt.plot(range(10), range(10))
hhs.fix_axis(plt.gca()) # zet de assen juist neer
plt.tight_layout() # zet de figuur margins goed
plt.show()
