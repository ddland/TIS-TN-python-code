import numpy as np
import time 

from TN_code.hardware import get_data
from TN_code.hardware import write_data

# importeer de ADCPi module
try:
    from ADCPi import ADCPi
except ImportError:
    print("Failed to import ADCPi from python system path")
    print("Importing from parent folder instead")
    try:
        import sys
        sys.path.append('..')
        from ADCPi import ADCPi
    except ImportError:
        raise ImportError(
            "Failed to import library from parent folder")


bitrate = 12  # 14, 16 of 18 bit
channel = 8   # welk kanaal wil je gebruiken?
adc = ADCPi(0x68, 0x69, bitrate)
adc.set_conversion_mode(1)  # meet continue

data = get_data.readADCpi(adc, channel)  # 1000 samples, t0=0

# sla de data op
# geef de file een beschrijvende naam (en een uniek deel, de timestamp)

filename = 'meting_test1_%s.txt' % (int(time.time()))

# schrijf data weg
write_data.saveArray(data, filename)
