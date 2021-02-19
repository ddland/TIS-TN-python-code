# TIS-TN-python-code

Hier staat de source code van de scripts die door de docenten van TN voor gebruik tijdens de studie gemaakt zijn.

De scripts helpen bij het [plotten](TN_code/plotten/) (standaard mooi opgemaakte figuren), [regressie](voorbeelden/regressie/), [fourier](TN_code/fourier/) volgens het wiskunde boek en het [uitlezen van sensoren](TN_code/hardware).

Zie verder het voorbeeld gebruik in de [voorbeelden](TN_code/voorbeelden) directorie. Deze directorie wordt niet met PyPi geinstalleerd, hiervoor kan je het git-repository gebruiken. 

## Installatie en afhankelijkheden

### Afhankelijkheden (dependencies)
De scripts maken gebruik van (via pip worden ze automatisch meegeinstalleerd):
* numpy
* matplotlib
* sympy

Voor de hardware-scripts zijn meer afhankelijkheden nodig (worden niet automatisch geinstalleerd):
* adafruit_circuitpython-ads1x15
* adafruit-circuitpython-mcp3xxx
* sensehat

Om voor alle gebruikers deze afhankelijkheden te installeren is de volgende code nodig (Linux):
```console
sudo apt-get install sense-hat
sudo pip install adafruit_circuitpython-ads1x15 adafruit-circuitpython-mcp3xxx
```

### Installatie via PyPi
Als PyPi aanwezig is kan via [PyPi](https://pypi.org/project/TN-code) de software voor de huidge gebruiker geinstalleer worden:
```console
pip install tn_code
```
Om system-wide (voor alle gebruikers te installeren:
```console
sudo pip install tn_code
```

Als virtual environment
```console
mkdir project-naam && cd project-naam
python -m venv .env
source .env/bin/activate
pip install tn_code
```
