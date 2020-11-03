import numpy as np
import time

from TN_code.hardware import get_data
from TN_code.hardware import write_data

try:
    import board
    import busio
    i2c = busio.I2C(board.SCL, board.SDA)

    import adafruit_ads1x15.ads1015 as ADS
    from adafruit_ads1x15.analog_in import AnalogIn

except ImportError:
    print("Failed to import piplates-DAQCplate from python system path")
    raise ImportError(
        "Failed to import library from parent folder")


###### configureer de ADC

ads = ADS.ADS1015(i2c)

ads.mode = ADS.Mode.CONTINUOUS    #snel
# ads.mode = ADS.Mode.SINGLE      #langzaam

ads.gain = 1 
print(ads.gains)  # voor alle opties
ads.rate = 3300
print(ads.rates)  # voor alle opties

chan = AnalogIn(ads, ADS.P0)  # pin 0 verbonden

###### Lees meerdere datapunten
data = get_data.readADS(chan)

# maak een (unieke) filenaam aan
filename = 'meting_test1_%s.txt' %(int(time.time()))
write_data.saveArray(data, filename)
