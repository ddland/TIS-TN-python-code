#!/usr/bin/env python3

"""
Voorbeeld code om de sensehat uit te lezen. Inclusief wegschrijven van de data.
"""

import time
import sys

try:
    from sense_hat import SenseHat
except ImportError:
    from sense_emu import SenseHat

    print("SenseHat emulator geimporteerd!")


if __name__ == "__main__":
    # geef de file een naam met de huidige tijd.
    filename = "ACC_%s.txt" % (time.strftime("%Y%m%d-%H%M%S", time.localtime()))
    # open de file in 'append' mode.
    stream = open(filename, "a")

    # maak het sense object aan en lees uit de RTIMULib file het
    # ingestelde span.

    sense = SenseHat()
    rtimulib_config = sense._get_settings_file("RTIMULib")
    accel_span = rtimulib_config.LSM9DS1AccelFsr

    # Geef het ingestelde span en de filenaam weer.
    sense.show_message(filename)
    sense.show_letter("%s" % (accel_span))

    # start de hoofd-lus.
    run = True
    try:  # bij CTRL-C breek dan de code af.
        while run:
            # lees de ACC data en schrijf die weg naar de stream.
            data = sense.get_accelerometer_raw()
            stream.write(
                "%s,%s,%s,%s\n" % (time.time(), data["x"], data["y"], data["z"])
            )
    except KeyboardInterrupt:
        # breek de while-loop af
        run = False

    # sluit het programma netjes af (na einde lus).
    stream.close()
    sense.clear()
    time.sleep(1)
    sys.exit()
