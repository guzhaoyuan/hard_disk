/*Move control
*Author:Sunchaothu@thu-skyworks
*All right reserved
*2016/1/29
*version 2.0
*/

/*====update version 2.1======
*2016/2/22  
*add reset-function
* add inverse process 
* change move function
*/

//==============readme=========
//define pin:
//int steering=2;
//int ele_magnet=12;
//int stepping_C=11,stepping_B=10,stepping_A=9; //PWM output
//int dir_C=8,dir_B=7,dir_A=6;
//int offline_C=5  ,offline_B=4,offline_A=3;
//
//=======================

//=============about movecontrol==========
// we use Corexy as basic structure
// the equations of Motion:
// x=1/2*(A+B),  y = 1/2*(A-B)
// A= x+y ,    B = x-y
//=======================

const int length=5;// the lenth of each check 
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

void A_enable()
{
    digitalWrite(3,LOW);
}
void B_enable()
{
    digitalWrite(4,LOW);
}
void C_enable()
{
    digitalWrite(5,LOW);
}
void A_disable()
{
    digitalWrite(3,HIGH);
}
void B_disable()
{
    digitalWrite(4,HIGH);
}
void C_disable()
{
   digitalWrite(5,HIGH);
}
void A_clockwise()
{
   digitalWrite(6,LOW);
}
void B_clockwise()
{
   digitalWrite(7,LOW);
}
void C_clockwise()
{
   digitalWrite(8,LOW);
}
void A_anticlockwise()
{
   digitalWrite(6,HIGH);
}
void B_anticlockwise()
{
    digitalWrite(7,HIGH);
}
void C_anticlockwise()
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

void reset_func()
{
  
}

void x_go_move()
{
  //x=1/2*(A+B)
   A_clockwise();B_clockwise();
   A_enable();B_enable();
}

void x_back_move()
{
  A_anticlockwise(); B_anticlockwise();
  A_enable();B_enable();
}

void x_stop()
{
  A_disable();B_disable();
}

void y_go_move()
{
 // y = 1/2*(A-B)
  A_clockwise();B_anticlockwise();
  A_enable();B_enable();
}
void y_back_move()
{
  A_anticlockwise();B_clockwise();
  A_enable();B_enable();
}

void y_stop()
{
  A_disable();B_disable();
}
void z_rise_move()
{  C_clockwise();
  C_enable();
}
void z_fall_move()
{
   C_anticlockwise();
   C_enable();
}

void xy_go_move()
{
  analogWrite(10,0);
  A_clockwise();A_enable();
} 

void xy_back_move()
{
   
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
   A_disable();
   B_disable();
   C_disable();
   analogWrite(8,127);
   analogWrite(9,127);
   analogWrite(10,127);
   while(Serial.available())
   {
     ch1=Serial.read();
     ch2=Serial.read();
     ch3=Serial.read();

      C_enable();
      C_clockwise();
      delay(1000*(ch3-'0'));//wait to correct
      C_disable();

      steering_on();delay(500);//steering engine work
      C_enable();
      C_clockwise();
      delay(1000);//wait to correct
      C_disable();

      A_enable();B_enable();
      A_clockwise();B_clockwise();
      if(ch2>ch1)
         { delay(1000*(ch1-'0'));A_disable();
           delay(1000*(ch2-ch1));B_disable();
          }
      else
          {
           delay(1000*(ch2-'0'));B_disable();
           delay(1000*(ch1-ch2));A_disable();
          }

      C_anticlockwise();
      C_enable();
      ele_magnet_on();//eletromagnet work
      delay(1000);
      C_disable();

      C_clockwise();
      C_enable();
     delay(1000);
      C_disable();
  
      A_enable();B_enable();
      A_anticlockwise();B_anticlockwise();
      if(ch2>ch1)
          { delay(1000*(ch1-'0'));A_disable();
           delay(1000*(ch2-ch1));B_disable();
          }
      else
          {
           delay(1000*(ch2-'0'));B_disable();
           delay(1000*(ch1-ch2));A_disable();
          } 
      C_anticlockwise(); 
      C_enable();
      delay(1000);//wait to correct
      C_disable();
      steering_reset();
      delay(500);

      C_anticlockwise();
     C_enable();
     delay(100*(ch3-'0'));
     C_disable();
      ele_magnet_off();
      delay(1000);
  }
}
//it'sok

