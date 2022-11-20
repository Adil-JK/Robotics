#include <Servo.h>

#define SERVO1_PIN 3
#define SERVO2_PIN 5
#define SERVO3_PIN 6
#define SERVO4_PIN 10
#define SERVO5_PIN 11

Servo servos[5];
byte positions[5];
String receivedData;

void setup()
{
	Serial.begin(9600);
	servos[0].attach(SERVO1_PIN);
	servos[1].attach(SERVO2_PIN);
	servos[2].attach(SERVO3_PIN);
	servos[3].attach(SERVO4_PIN);
	servos[4].attach(SERVO5_PIN);
}

void loop()
{
	while (!Serial.available());

	receivedData = Serial.readString();
	receivedData.trim();
	parseData(positions, receivedData);
	driveServos(positions);
}

void driveServos(byte positions[5])
{
	for (byte counter = 0; counter < 5; counter++)
	{
		servos[counter].write(positions[counter]);
	}
}
