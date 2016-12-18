# TIS-TN-python

Hier staan python scripts en modules die kunnen helpen gedurende de studie TN bij de Haagse Hogeschool.

## TIS-TN-plot.py

Script om significante cijfers en gebruik van machten volgens het document Labjournaal, Meetrapport en Verslag weer te geven. \\
Punten zijn vervangen door komma's en X- en Y-as zijn afzonderlijk van precisie te voorzien.

### Gebruik
import matplotlib.pyplot as plt
import TIS-TN-plot as hhs
hhs.PRECISION_Y = 3 # zet y-as op 3 cijfes significant (standaard = 2)

fix_axis(plt.gca()) # zet de assen juist neer
plt.tight_layout() # zet de figuur margins goed
