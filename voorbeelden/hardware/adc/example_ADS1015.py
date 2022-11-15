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
    raise ImportError("Failed to import library from parent folder")

# INPUT VARIABELEN
samples = 1000
sample_rate = 250
gain = 1
mode = "single"
filename = "test"

# ----- configureer de ADC

ads = ADS.ADS1015(i2c)

if mode == "cont":
    ads.mode = ADS.Mode.CONTINUOUS  # snel
elif mode == "single":
    ads.mode = ADS.Mode.SINGLE  # langzaam

ads.gain = gain
print(ads.gains)  # voor alle opties
ads.data_rate = sample_rate
print(ads.rates)  # voor alle opties

chan = AnalogIn(ads, ADS.P0, ADS.P1)  # pin 0 verbonden

# ----- Lees meerdere datapunten
data = get_data.readADS(chan, samples)

# maak een (unieke) filenaam aan
file_name = filename + ".txt"
write_data.saveArray(data, file_name)
