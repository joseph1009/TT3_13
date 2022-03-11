///* LED Blink, Teensyduino Tutorial #1
//   http://www.pjrc.com/teensy/tutorial.html
// 
//   This example code is in the public domain.
//*/
//
//// Teensy 2.0 has the LED on pin 11
//// Teensy++ 2.0 has the LED on pin 6
//// Teensy 3.x / Teensy LC have the LED on pin 13
//const int ledPin = 13;
//
//// the setup() method runs once, when the sketch starts
//
//void setup() {
//  // initialize the digital pin as an output.
//  pinMode(ledPin, OUTPUT);
//}
//
//// the loop() methor runs over and over again,
//// as long as the board has power
//
//void loop() {
//  digitalWrite(ledPin, HIGH);   // set the LED on
//  delay(1000);                  // wait for a second
//  digitalWrite(ledPin, LOW);    // set the LED off
//  delay(1000);                  // wait for a second
//}


#include <CapacitiveSensor.h>


CapacitiveSensor Sensor = CapacitiveSensor(4, 6); //sending resistor: 150k //receiving resistor: 800ohm 

long val;
int pos;
//#define led 13
const int ledPin = 13;

void setup()
{
//Serial.begin(9600);
pinMode(ledPin, OUTPUT);
}

void loop()
{

val = Sensor.capacitiveSensor(10);
Serial.println(val);
if (val >= 1000 && pos == 0)
{
digitalWrite(ledPin, HIGH);
pos = 1;
delay(500);
}

else if (val >= 1000 && pos == 1)
{
digitalWrite(ledPin, LOW);
pos = 0;
delay(500);
}

delay(10);
}
