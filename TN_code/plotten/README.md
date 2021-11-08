# TISTNplot.py

Script om significante cijfers en gebruik van machten volgens het document Labjournaal, Meetrapport en Verslag weer te geven. 
Punten zijn vervangen door komma's en X- en Y-as zijn afzonderlijk van precisie te voorzien.

## Gebruik
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

plt.set_ticks(ax)  # corrigeer de ticks met de aangemaakte labels

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

## Te weinig cijfers op de as
Met beulp van 
```python
TN.set_ticks(ax)
```
kunnen de assen opnieuw gerenderd worden om eventuele problemen door het afronden op te lossen. De code genereert opnieuw de tick-waarden bij de ticklabels die na het afronden zijn ontstaan. Vallen er ticklabels samen dan wordt er een waarschuwing gegeven. Bij het verplaatsen van ticklabels (bijvoorbeeld door een afronding van 7,5 naar 7) wordt alleen het grid opnieuw weergegeven.

