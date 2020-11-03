# TIS-TN-python-code

Hier staat de source code van de scripts die door de docenten van TN voor gebruik tijdens de studie gemaakt zijn.

De scripts helpen bij het plotten (standaard mooi opgemaakte figuren), regressie, fourier volgens het wiskunde boek en het uitlezen van data.

## Installatie en afhankelijkheden

### Afhankelijkheden (dependencies)
De scripts maken gebruik van (via pip worden ze automatisch meegeinstalleerd):
* numpy
* matplotlib
* sympy

Voor de hardware-scripts zijn meer afhankelijkheden nodig (worden niet automatisch geinstalleerd):
* adafruit_circuitpython-ads1x15
* sensehat

### Installatie via PyPi
Als PyPi aanwezig is kan via [PyPi](https://pypi.org/project/TN-code) de software voor de huidge gebruiker geinstalleer worden:
```console
pip3 install tn_code
```
Om system-wide (voor alle gebruikers te installeren:
```console
sudo pip3 install tn_code`
```

Als virtual environment
```console
mkdir project-naam && cd project-naam
python3 -m venv .env
source .env/bin/activate
pip3 install tn_code
```

