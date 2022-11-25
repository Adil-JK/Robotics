#include <Servo.h>

#define SERVO1_PIN 3
#define SERVO2_PIN 5
#define SERVO3_PIN 6
#define SERVO4_PIN 10
#define SERVO5_PIN 11

Servo servos[5];
String receivedData;
byte servoCounter = 0;

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
	while (Serial.available())
    {
        if (servoCounter == 5) {
            servoCounter = 0;
        }

        receivedData = Serial.readStringUntil(',');
        receivedData.trim();
        servos[servoCounter].write(receivedData.toInt());
        servoCounter++;
    };
}