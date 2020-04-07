# TIS-TN-python

Hier staan python scripts en modules die kunnen helpen gedurende de studie TN bij de Haagse Hogeschool.

## TISTNplot.py

Script om significante cijfers en gebruik van machten volgens het document Labjournaal, Meetrapport en Verslag weer te geven. 
Punten zijn vervangen door komma's en X- en Y-as zijn afzonderlijk van precisie te voorzien.

### Gebruik
Een minimaal voorbeeld is hieronder gegeven:
```python

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
