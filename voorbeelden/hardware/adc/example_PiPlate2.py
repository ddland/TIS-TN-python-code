import numpy as np
import time

from TN_code.hardware import get_data
from TN_code.hardware import write_data

try:
    import piplates.DAQC2plate as DAQC
except ImportError:
    print("Failed to import piplates-DAQCplate from python system path")
    raise ImportError(
        "Failed to import library from parent folder")

# ----- zet de LED uit
DAQC.setLED(0, 'off')

# ----- stuur de analoge output aan
DAQC.setDAC(0, 1, 2.64)  # DAQ 0, adres analog-output 1, voltage 2.64 V

# ----- stuur 0, 1, 2, 3 volt naar analog-output 1
for i in range(10):
    volt = i % 4  # i modulo 4
    DAQC.setDAC(0, 1, volt)
    time.sleep(0.1)


# ----- Lees data van Analoge Input

val = DAQC.getADC(0, 1)  # DAQC 0, adres Analog-Input 1
print(val)
val8 = DAQC.getADCall(0)  # lees alle 8 Analog-Inputs
print(val8)

# ----- Lees meerdere data punten

data = get_data.readPiPlate(DAQC, 3)  # kanaal 0, 1000 punten, ADC 0

# maak een (unieke) filenaam aan
filename = 'meting_test1_%s.txt' % (int(time.time()))
write_data.saveArray(data, filename)
