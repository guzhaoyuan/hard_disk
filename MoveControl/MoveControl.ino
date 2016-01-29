/*Move control
*Author:Sunchaothu
*All right reserved
*2016/1/29
*version 2.0
*/
//==============readme=========
//define pin:
//int steering=2;
//int ele_magnet=12;
//int stepping_z=11,stepping_y=10,stepping_x=9; //PWM output
//int dir_z=8,dir_y=7,dir_x=6;
//int offline_z=5  ,offline_y=4,offline_x=3;
//
//=======================
#include<Servo.h>
Servo myservo;
void steering_on()
{
    myservo.write(90);
}
 void steering_reset()
{
    myservo.write(0);
}

void x_enable()
{
    digitalWrite(3,LOW);
}
void y_enable()
{
    digitalWrite(4,LOW);
}
void z_enable()
{
    digitalWrite(5,LOW);
}
void x_disenable()
{
    digitalWrite(3,HIGH);
}
void y_disenable()
{
    digitalWrite(4,HIGH);
}
void z_disenable()
{
   digitalWrite(5,HIGH);
}
void x_clockwise()
{
   digitalWrite(6,LOW);
}
void y_clockwise()
{
   digitalWrite(7,LOW);
}
void z_clockwise()
{
   digitalWrite(8,LOW);
}
void x_anticlockwise()
{
   digitalWrite(6,HIGH);
}
void y_anticlockwise()
{
    digitalWrite(7,HIGH);
}
void z_anticlockwise()
{
   digitalWrite(8,HIGH);
}
//
void  ele_magnet_on()
{
   digitalWrite(12,HIGH);
}
void  ele_magnet_off()
{
   digitalWrite(12,LOW);
}


void setup() 
{
      myservo.attach(2);
      pinMode(3,OUTPUT);
      pinMode(4,OUTPUT);
      pinMode(5,OUTPUT);
      pinMode(6,OUTPUT);
      pinMode(7,OUTPUT);
      pinMode(8,OUTPUT);
      pinMode(9,OUTPUT);
      pinMode(10,OUTPUT);
      pinMode(11,OUTPUT);
      pinMode(12,OUTPUT);
      Serial.begin(9600);
 }

char ch1='0',ch2='0',ch3='0';
void loop()
{
   x_disenable();
   y_disenable();
   z_disenable();
   analogWrite(8,127);
   analogWrite(9,127);
   analogWrite(10,127);
   while(Serial.available())
   {
     ch1=Serial.read();
     ch2=Serial.read();
     ch3=Serial.read();

      z_enable();
      z_clockwise();
      delay(1000*(ch3-'0'));//wait to correct
      z_disenable();

      steering_on();delay(500);//steering engine work
      z_enable();
      z_clockwise();
      delay(1000);//wait to correct
      z_disenable();

      x_enable();y_enable();
      x_clockwise();y_clockwise();
      if(ch2>ch1)
          { delay(1000*(ch1-'0'));x_disenable();
           delay(1000*(ch2-ch1));y_disenable();
          }
      else
          {
           delay(1000*(ch2-'0'));y_disenable();
           delay(1000*(ch1-ch2));x_disenable();
          }

      z_anticlockwise();
      z_enable();
      ele_magnet_on();//eletromagnet work
      delay(1000);
      z_disenable();

      z_clockwise();
      z_enable();
      delay(1000);
      z_disenable();
  
      x_enable();y_enable();
      x_anticlockwise();y_anticlockwise();
      if(ch2>ch1)
          { delay(1000*(ch1-'0'));x_disenable();
           delay(1000*(ch2-ch1));y_disenable();
          }
      else
          {
           delay(1000*(ch2-'0'));y_disenable();
           delay(1000*(ch1-ch2));x_disenable();
          }

      z_anticlockwise(); 
      z_enable();
      delay(1000);//wait to correct
      z_disenable();
      steering_reset();
      delay(500);

      z_anticlockwise();
      z_enable();
      delay(1000*(ch3-'0'));
      z_disenable();
      ele_magnet_off();
      delay(1000);
   }
}
//it's ok

