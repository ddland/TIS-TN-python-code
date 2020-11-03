import numpy as np
import time 

from TN_code.hardware import get_data
from TN_code.hardware import write_data

try:
    import piplates.DAQCplate as DAQC
except ImportError:
    print("Failed to import piplates-DAQCplate from python system path")
    raise ImportError(
        "Failed to import library from parent folder")


###### Afstandsmeting 
'''
Extra hardware:
    HC-SR04
Aansluitschema:
    5V: Digital-Output socket 10
    Ground: Digital-Input socket 10
    Trigger: Digital-Output socket 0
    Echo: Digital Input socket 0

Zie voor details:
    https://pi-plates.com/daqc-users-guide/#Distance_Measurement_with_the_HC-SR04
'''

#### werkt alleen als de hardware is aangesloten
# distance = DAQC.getRANGE(0,0,'c') # geeft afstand in cm
# print(distance)

####### Lees data van Analoge Input

val = DAQC.getADC(0, 1) # DAQC 0, adres Analog-Input 1
print(val)
val8 = DAQC.getADCall(0) # lees alle 8 Analog-Inputs
print(val8)


######## Lees meerdere data punten

data = get_data.readPiPlate(DAQC, [0,1,2]) # kanaal [0,1,2], 1000 punten, ADC 0

# maak een (unieke) filenaam aan
filename = 'meting_test1_%s.txt' % (int(time.time()))
write_data.saveArray(data, filename)
