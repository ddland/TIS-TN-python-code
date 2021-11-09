 # TIS-TN-python-code

Hier staat de source code van de scripts die door de docenten van TN voor gebruik tijdens de studie gemaakt zijn.

De scripts helpen bij het [plotten](TN_code/plotten/) (standaard mooi opgemaakte figuren), [regressie](voorbeelden/regressie/), [fourier](TN_code/fourier/) volgens het wiskunde boek en het [uitlezen van sensoren](TN_code/hardware).

Zie verder het voorbeeld gebruik in de [voorbeelden](TN_code/voorbeelden) directorie. Deze directorie wordt niet met PyPi geïnstalleerd, hiervoor kan je het git-repository gebruiken. 

## Installatie en afhankelijkheden

### Afhankelijkheden (dependencies)
De scripts maken gebruik van (via pip worden ze automatisch meegeïnstalleerd):
* numpy
* matplotlib
* sympy

Voor de hardware-scripts zijn meer afhankelijkheden nodig (worden niet automatisch geïnstalleerd):
* adafruit_circuitpython-ads1x15
* adafruit-circuitpython-mcp3xxx
* sensehat

Om voor alle gebruikers deze afhankelijkheden te installeren is de volgende code nodig (Linux):
```console
sudo apt-get install sense-hat
sudo pip install adafruit_circuitpython-ads1x15 adafruit-circuitpython-mcp3xxx
```

### Raspberrypi 
De raspberrypi maakt standaard gebruik van python2. Om voor python3 (de Python versie die je voor je eigen code wilt gebruiken!) de modules te installeren moet de juiste python gebruikt worden om de modules te installeren. Het commando om bijvoorbeeld de adafruit libraries met pip te installeren wordt dan:
```console
sudo python3 -m pip install adafruit_circuitpython-ads1x15 adafruit-circuitpython-mcp3xxx
```

Door Python (python3) met de -m optie aan te roepen is het volgende argument de module die uitgevoerd moet worden. Zo weet je altijd dat de juiste python-interpreter gebruikt wordt om PyPi packages te installeren.

### Installatie via PyPi
Als PyPi aanwezig is kan via [PyPi](https://pypi.org/project/TN-code) de software voor de huidige gebruiker geïnstalleerd worden:
```console
python -m pip install tn_code
```
Om system-wide (voor alle gebruikers te installeren):
```console
sudo python -m pip install tn_code
```

Als virtual environment
```console
mkdir project-naam && cd project-naam
python -m venv .env
source .env/bin/activate
python -m install tn_code
```
Daarna moet, om gebruik te maken van het virtuele environment, bij het opstarten het environmet geactiveerd worden

### Upgrade via PyPi
Om het package TN-code te updaten moet de ```--upgrade``` optie toegevoed worden aan het pip installatie commando:
```console
sudo python -m pip install --upgrade tn_code
```

