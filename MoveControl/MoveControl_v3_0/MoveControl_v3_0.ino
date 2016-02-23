/*Move control
*Author:Sunchaothu@thu-skyworks
*All right reserved
*version 3.0
*/

/*====update version 3.0======
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

const int length=5;// the length of each check 
const int speed_ =10; //to be ascertain 
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
void z_stop()
{
  C_disable();
}

void xy_go_move()
{
  analogWrite(10,0);
  A_clockwise();A_enable();
} 

void xy_back_move()
{
   analogWrite(10,0);
   A_anticlockwise();A_enable();
}

void xy_stop_move()
{
  A_disable(); B_disable(); analogWrite(10,127);
}

unsigned long worktime(char ch)
{
  return (unsigned long)(ch-'0')*length/speed_;
}

void attach_stop_x()
{
  x_stop();
}

void attach_stop_y()
{
  y_stop();
}

void attach_stop_z()
{
 z_stop(); 
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
      attachInterrupt(2, attach_stop_x, CHANGE);  // pin 21
      attachInterrupt(3, attach_stop_y, CHANGE);  // pin 19
      attachInterrupt(4, attach_stop_z, CHANGE);  // pin 18
      Serial.begin(9600);
 }

char x_='0',y_='0',z_='0', flag = '0';
unsigned long work_time;
void loop()
{
   analogWrite(8,127);
   analogWrite(9,127);
   analogWrite(10,127);
   while(Serial.available())
   {
     flag = Serial.read();
     if( flag == '1')
        {
           x_=Serial.read();
           y_=Serial.read();
           z_=Serial.read();
           work_time=worktime(z_);
           z_rise_move(); delay(work_time);z_stop();
      
            steering_on(); delay(500);//steering engine work
            z_rise_move(); delay(2000);//wait to ascertain
       
            if(y_>x_)
               { 
                  work_time = worktime(x_);
                  xy_go_move(); delay(work_time); xy_stop_move();
      
                  work_time = worktime(y_-x_); 
                  y_go_move();  delay(work_time); y_stop();
                }
            else if (y_==x_)
                {
                  work_time = worktime(y_);
                  xy_go_move(); delay(work_time); xy_stop_move();
                }
             else
             {
                  work_time = worktime(y_);
                  xy_go_move(); delay(work_time); xy_stop_move();
      
                  work_time = worktime(x_-y_);
                  x_go_move();  delay(work_time); x_stop();
             }
            
            //eletromagnet work
            ele_magnet_on();
            z_fall_move();
            delay(2000); // wait to ascertain
            z_stop();
      
            z_rise_move();
            delay(2000);
            z_stop();
        
            if(y_>x_)
               { 
                  work_time = worktime(x_);
                  xy_back_move(); delay(work_time); xy_stop_move();
      
                  work_time = worktime(y_-x_);
                  y_back_move();  delay(work_time); y_stop();
                }
            else if (y_==x_)
                {
                  work_time = worktime(y_);
                  xy_back_move(); delay(work_time); xy_stop_move();
                }
             else
             {
                  work_time = worktime(y_);
                  xy_back_move(); delay(work_time); xy_stop_move();
      
                  work_time = worktime(x_-y_);
                  x_back_move();  delay(work_time); x_stop();
             }
            z_fall_move();
            delay(1000);//wait to correct
            z_stop();
            steering_reset();
            delay(500);
            
            work_time=worktime(z_);
            z_fall_move();
            delay(work_time);
            z_stop();
      
            ele_magnet_off();
      
            //add limit switch
            x_go_move();
            y_go_move();
            z_fall_move();
        }
        
       // fang hui
      else
       {
           x_=Serial.read();
           y_=Serial.read();
           z_=Serial.read();

           ele_magnet_on();
            work_time=worktime(z_);
            z_rise_move();
            delay(work_time);
            z_stop();

            steering_on(); delay(500);//steering engine work
            z_rise_move(); delay(2000);//wait to ascertain
       
            if(y_>x_)
               { 
                  work_time = worktime(x_);
                  xy_go_move(); delay(work_time); xy_stop_move();
      
                  work_time = worktime(y_-x_);
                  y_go_move();  delay(work_time); y_stop();
                }
            else if (y_==x_)
                {
                  work_time = worktime(y_);
                  xy_go_move(); delay(work_time); xy_stop_move();
                }
             else
             {
                  work_time = worktime(y_);
                  xy_go_move(); delay(work_time); xy_stop_move();
      
                  work_time = worktime(x_-y_);
                  x_go_move();  delay(work_time); x_stop();
             }
            
            z_fall_move();delay(2000); z_stop();  // delay wait to ascertain
            ele_magnet_off();

            z_rise_move();
            delay(2000);
            z_stop();
        
            if(y_>x_)
               { 
                  work_time = worktime(x_);
                  xy_back_move(); delay(work_time); xy_stop_move();
      
                  work_time = worktime(y_-x_);
                  y_back_move();  delay(work_time); y_stop();
                }
            else if (y_==x_)
                {
                  work_time = worktime(y_);
                  xy_back_move(); delay(work_time); xy_stop_move();
                }
             else
             {
                  work_time = worktime(y_);
                  xy_back_move(); delay(work_time); xy_stop_move();
      
                  work_time = worktime(x_-y_);
                  x_back_move();  delay(work_time); x_stop();
             }
            z_fall_move();delay(1000);//wait to correct
            z_stop();
            steering_reset();
            delay(500);
            
            work_time=worktime(z_);
            z_fall_move();
            delay(work_time);
            z_stop();
      
            ele_magnet_off();
      
            //add limit switch
            x_go_move();
            y_go_move();
            z_fall_move();
        
         }
  }


}
//it'sok

