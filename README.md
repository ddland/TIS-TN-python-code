# TIS-TN-python

Hier staan python scripts en modules die kunnen helpen gedurende de studie TN bij de Haagse Hogeschool.

## TISTNplot.py

Script om significante cijfers en gebruik van machten volgens het document Labjournaal, Meetrapport en Verslag weer te geven. 
Punten zijn vervangen door komma's en X- en Y-as zijn afzonderlijk van precisie te voorzien.

### Gebruik
Een minimaal voorbeeld is hieronder gegeven:
```python
import matplotlib.pyplot as plt
import TISTNplot as hhs
hhs.PRECISION_Y = 3 # zet y-as op 3 cijfes significant (standaard = 2)

plt.plot(range(10), range(10))
hhs.fix_axis(plt.gca()) # zet de assen juist neer
plt.tight_layout() # zet de figuur margins goed
plt.show()
```

De TISTNplot module heeft twee variabelen die aangepast kunnen worden om de precisie van de x- en y-as weer te geven (PRECISION_Y en PRECISION_X). Daarna kunnen, na het aanmaken van het plot-object, de asses goed gezet worden (`hhs.fix_axis(plt.gca())`). De matplotlib functie `tight_layout` verwijdert eventuele witruimte rond het figuur (of voegt het toe) en `plt.show` geeft het figuur weer. 
