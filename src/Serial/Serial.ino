#include <Servo.h>
Servo myservo;
Servo base;
Servo arm;
Servo waist;
Servo wrist_base;
Servo wrist ;
Servo gripper;
int pos = 0;
//


void setup()

{
  ////////////////////////////////////
base.attach(12);
arm.attach(11);
waist.attach(10);
wrist_base.attach(9);
wrist_base.write(170);
wrist.attach(8);
gripper.attach(7);
gripper.write(150);
waist.write(170);

//////////////////////////////////////////////////
Serial.begin(9600);
while (!Serial);
Serial.println("-------------------------");
Serial.println("ARos is loading....");
delay(1000);
Serial.println("ARos loaded succesfully");
Serial.println("-------------------------");
myservo.attach(servo);
Serial.println("calibrating servo...");
for(pos = 0; pos <= 180; pos += 1)
myservo.write(0);
delay(1000);
myservo.write(180);
delay(1000);
myservo.write(90);
delay(1000);
Serial.println("servo calibrated");
Serial.println("-------------------------");
Serial.println("Comand input online, write command to perform action");
Serial.println("-------------------------");


}

void loop() {
/////////////////////////////////////////////////
delay(150);
wrist.write(80);
delay(150);
base.write(30);
delay(150);
//wrist.write(50);
delay(150);
waist.write(180);
delay(150);
arm.write(50);
delay(1500);
gripper.write(150);
delay(1500);
wrist.write(80);
delay(1500);
gripper.write(20);
delay(1500);
arm.write(90);
delay(1500);
waist.write(150);
delay(1500);


base.write(170);
 delay(1500);


wrist.write(50);
delay(150);
waist.write(180);
delay(150);
arm.write(50);
delay(1500);
gripper.write(130);
delay(1500);

arm.write(90);
delay(150);
waist.write(110);
delay(1500);
base.write(30);
delay(30);

  ////////////////////////////////////////
  
for(pos = 0; pos <= 180; pos += 1)
if (Serial.available())


{
  int state1 = Serial.parseInt();
    
if (state1 < 10)

{
Serial.print(">");
Serial.println(state1);
Serial.println("cannost execute command, too low number");

}

if (state1 >= 10 && state1 <= 170)
{
  Serial.print(">");
  Serial.println(state1);
  Serial.print("turning servo to ");
  Serial.print(state1);

  Serial.println(" degrees");
  myservo.write(state1);
  
}

}

}



  
