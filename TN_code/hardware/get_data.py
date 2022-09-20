import time
import os
import numpy as np

"""
Module waarin voor verschillende DACs code staat om de DAC uit te lezen.
De functies geven een array terug met data (voltage), standaard 1000
meetpunten, zo snel mogelijk na elkaar gemeten.


    functies:
        readMCP3008: lees data van een MSP3008
                   https://learn.adafruit.com/mcp3008-spi-adc/python-circuitpython
        readADS:   lees data van de ADS1015 en ADS1115 van adafruit.
                   https://learn.adafruit.com/adafruit-4-channel-adc-breakouts/
        readADCpi: lees data van de ADC Pi Plus
                   https://www.abelectronics.co.uk/kb/article/1044/adc-pi
        readPiPlate: lees analoge data van de PiPlate: DAQCplate en DAQ2plate
                   https://pi-plates.com
        readArduino: lees data van een arduino
                   (met standaard AnalogReadSerial.ino geladen)

"""


def readMCP3008(channel, N=1000, t0=0):
    """
    lees de MCP3008 op kanaal=channel uit voor N samples

    argumenten:
        channel: AnalogIn object met het juiste kanaal of een lijst van
                 objecten voor meerdere kanalen.
        N: aantal samples om te lezen, standaard 10000
        t0: begintijd. Als t=0 begint de tijd hiermee, anders met de opgegeven
           waarde.

    return:
        data: 2d of n-d numpy array met N data- en tijd samples.
    """
    return readADS(channel, N, t0)


def readADS(channel, N=1000, t0=0):
    """
    lees de ADS op kanaal=channel uit voor N samples

    argumenten:
        channel: AnalogIn object met het juiste kanaal of een lijst van
                 objecten voor meerdere kanalen.
        N: aantal samples om te lezen, standaard 10000
        t0: begintijd. Als t=0 begint de tijd hiermee, anders met de opgegeven
           waarde.

    return:
        data: 2d of n-d numpy array met N data- en tijd samples.
    """

    if np.size(channel) == 1:
        data = np.zeros((2, N))
        if t0 == 0:
            t0 = time.time()
        for i in range(N):
            data[:, i] = (time.time() - t0, channel.voltage)
    else:
        channels = len(channel)
        data = np.zeros((channels + 1, N))
        samples = np.zeros(channels)
        if t0 == 0:
            t0 = time.time()
        for i in range(N):
            for sample in range(channels):
                samples[sample] = channel[sample].voltage
            data[:, i] = time.time() - t0, *samples
    return data


def readADCpi(adc, channel, N=1000, t0=0):
    """
    lees de ADCpi op kanaal=channel uit voor N samples

    argumenten:
        adc: ADCpi object
        channel: kanaal waarop de sensor aangesloten is (of lijst met
                 meerdere kanelen)
        N: aantal samples om te lezen, standaard 10000
        t0: begintijd. Als t=0 begint de tijd hiermee, anders met de opgegeven
           waarde.

    return:
        data: 2d of n-d numpy array met N data- en tijd samples.
    """

    if np.size(channel) == 1:
        data = np.zeros((2, N))
        if t0 == 0:
            t0 = time.time()
        for i in range(N):
            data[:, i] = (time.time() - t0, adc.read_voltage(channel))
    else:
        channels = len(channel)
        data = np.zeros((channels + 1, N))
        samples = np.zeros(channels)
        if t0 == 0:
            t0 = time.time()
        for i in range(N):
            for sample in range(channels):
                samples[sample] = adc.read_voltage(channel[sample])
            data[:, i] = time.time() - t0, *samples
    return data


def readPiPlate(plate, channel, N=1000, t0=0, ADC=0):
    """
    lees de PiPlate op kanaal=channel uit voor N samples

    argumenten:
        adc: PiPlate (DAQ1 of DAQ2) object
        channel: kanaal waarop de sensor aangesloten is (of lijst met
                 meerdere kanelen)
        N: aantal samples om te lezen, standaard 10000
        t0: begintijd. Als t=0 begint de tijd hiermee, anders met de opgegeven
           waarde.
        ADC: 0 voor eerste DAQ, ander getal indien meerdere DAQ

    return:
        data: 2d of n-d numpy array met N data- en tijd samples.
    """

    if np.size(channel) == 1:
        data = np.zeros((2, N))
        if t0 == 0:
            t0 = time.time()
        for i in range(N):
            data[:, i] = (time.time() - t0, plate.getADC(ADC, channel))
    else:
        channels = len(channel)
        data = np.zeros((channels + 1, N))
        samples = np.zeros(channels)
        if t0 == 0:
            t0 = time.time()
        for i in range(N):
            for sample in range(channels):
                samples[sample] = plate.getADC(ADC, channel[sample])
            data[:, i] = time.time() - t0, *samples
    return data


def readArduino(ser, N=1000, t0=0, Ndata=1, seperator=";"):
    """
    Lees de arduino voor N datapunten uit.

    argumenten:
       ser: serial object
        N: aantal samples om te lezen, standaard 10000
        t0: begintijd. Als t=0 begint de tijd hiermee, anders met de
           opgegeven waarde.
        Ndata: aantal sensorvalues in de arduino stream.
        seperator: scheidingstekens voor het uitlezen van meerdere sensor
           waarden uit de stream. Standaard de :

    return:
        data: 2d of n-d numpy array met N data- en tijd samples.
    """

    data = np.zeros((Ndata + 1, N))
    if Ndata == 1:
        if t0 == 0:
            t0 = time.time()
        for i in range(N):
            try:  # mocht de data niet (goed) aankomen
                # ga dan verder met het volgende datapunt
                data[:, i] = (
                    time.time() - t0,
                    float(ser.readline().decode().strip("\r\n")),
                )
            except Exception:
                pass
    else:
        samples = np.zeros(Ndata)
        if t0 == 0:
            t0 = time.time()
        for i in range(N):
            try:  # mocht de data niet (goed) aankomen
                # ga dan verder met het volgende datapunt
                ardata = ser.readline().decode().strip("\r\n")
                ardata = ardata.split(seperator)
                ardata = [float(i) for i in ardata]
                data[:, i] = (time.time() - t0, *ardata)
            except Exception:
                pass
    return data
