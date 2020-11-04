# TIS-TN-ONDZ
Hier vind je code om de hardware voor de onderzoeken projecten uit te lezen.

## Python
In de [voorbeelden](../../voorbeelden/hardware/) directory staan de voorbeelden om de data uit de arduino, ADS1x15, MCP3008,  PiPlates en ADC Pi Plus uit te lezen. 

Gebuik de voorbeeldcode (`example_`) om zelf je data uit te lezen. Kopieer de voorbeelden die je nodig hebt en zet ze op je eigen USB-stick om zo makkelijk je data en code bij elkaar te houden. Veranderingen in je code kan je via GitHub in je fork van het TN repository bijhouden. 

Het bestand `get_data.py` maakt het mogelijk om de hardware op een eenvoudige manier uit te lezen. Heb je meer geavanceerde opties nodig, pas dan de code aan! Het bestand `write_data.py` is een wrapper om `numpy.savetxt`. In `lees_data_numpy.py` staan voorbeelden van hoe je de data uit de weggeschreven bestanden weer kan inlezen. 

Voor hulp bij het aansluiten van de hardware op de Raspberrypi of voor aansluitschema's van de verschillende HATs is er de volgende website: [pinout](https://pinout.xyz/).
