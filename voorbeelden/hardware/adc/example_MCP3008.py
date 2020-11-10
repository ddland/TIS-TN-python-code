import numpy as np
import time

from TN_code.hardware import get_data
from TN_code.hardware import write_data

try:
    import board
    import busio
    import digitalio
    import adafruit_mcp3xxx.mcp3008 as MCP
    from adafruit_mcp3xxx.analog_in import AnalogIn
except ImportError:
    print("Failed to import piplates-DAQCplate from python system path")
    raise ImportError(
        "Failed to import library from parent folder")

#INPUT VARIABELEN
filename = 'test'
samples = 1000

###### configureer de MCP
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs = digitalio.DigitalInOut(board.D5)
mcp = MCP.MCP3008(spi, cs)

chan = AnalogIn(mcp, MCP.P0, MCP.P1)

###### Lees meerdere datapunten
data = get_data.readADS(chan,samples)

# maak een (unieke) filenaam aan
file_name = filename+'.txt'
#filename = 'meting_test1_%s.txt' %(int(time.time()))
write_data.saveArray(data, file_name)
