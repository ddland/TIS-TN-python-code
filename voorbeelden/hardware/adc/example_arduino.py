import serial

from TN_code.hardware import get_data
from TN_code.hardware import write_data

ser = serial.Serial("/dev/ttyACM0", 9600)  # arduino

"""
AnalogReadSerial.ino -> 1 datapunt

/*
  AnalogReadSerial
  Reads an analog input on pin 0, prints the result to the serial monitor.
  Attach the center pin of a potentiometer to pin A0, and the outside pins
  to +5V and ground.

 This example code is in the public domain.
 */

// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}

// the loop routine runs over and over again forever:
void loop() {
  // read the input on analog pin 0:
  int sensorValue = analogRead(A0);
  // print out the value you read:
  Serial.println(sensorValue);
  delay(1);        // delay in between reads for stability
}
"""

# data = get_data.readArduino(ser)

"""
AnalogReadSerial.ino -> 2 datapunten
/*
  AnalogReadSerial
  Reads an analog input on pin 0, prints the result to the serial monitor.
  Attach the center pin of a potentiometer to pin A0, and the outside pins
  to +5V and ground.

  This example code is in the public domain.
 */

String semicolumn, values2;

// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  semicolumn = ";";
}

// the loop routine runs over and over again forever:
void loop() {
  // read the input on analog pin 0:
  int sensorValue1 = analogRead(A0);
  int sensorValue2 = analogRead(A1);
  // print out the value you read:
  values2 = sensorValue1 + semicolumn;
  values2 = values2 + sensorValue2;
  Serial.println(values2);
  delay(1);        // delay in between reads for stability
}
"""

data = get_data.readArduino(ser, Ndata=2)
print(data)
