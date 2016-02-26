/*Move control
*Author:Sunchaothu@thu-skyworks
*All right reserved
*version 3.1
*/

/*====update version 3.1======
*2016/2/24 
*rewrite function
*news method to produce PWM
*/

//=============about movecontrol==========
// we use Corexy as basic structure
// the equations of Motion:
// x=1/2*(A+B),  y = 1/2*(A-B)
// A= x+y ,    B = x-y
//=======================

#include<Servo.h>
#define servo_pin1 4
#define servo_pin2 5
#define servo_pin3 6
#define servo_pin4 11

#define A_STEP_PIN         54
#define A_DIR_PIN          55
#define A_ENABLE_PIN       38
#define A_MIN_PIN           3
#define A_MAX_PIN           2

#define B_STEP_PIN         60
#define B_DIR_PIN          61
#define B_ENABLE_PIN       56
#define B_MIN_PIN          14
#define B_MAX_PIN          15

#define C_STEP_PIN         46
#define C_DIR_PIN          48
#define C_ENABLE_PIN       62
#define C_MIN_PIN          18
#define C_MAX_PIN          19

const int length=5;// the length of each check 
const int speed_ =10; //to be ascertain 
int  work_time=0;
Servo myservo1,myservo2,myservo3,myservo4;

void steering_on()
{
   myservo1.write(90);
   myservo2.write(90);
   myservo3.write(90);
   myservo4.write(90);
}
void steering_reset()
{
   myservo1.write(0);
   myservo2.write(0);
   myservo3.write(0);
   myservo4.write(0);
}

void A_enable()
{
   digitalWrite(A_ENABLE_PIN,LOW);
}
void B_enable()
{
    digitalWrite(B_ENABLE_PIN,LOW);
}
void C_enable()
{
    digitalWrite(C_ENABLE_PIN,LOW);
}
void A_disable()
{
   digitalWrite(A_ENABLE_PIN,HIGH);
}
void B_disable()
{
   digitalWrite(B_ENABLE_PIN,HIGH);
}
void C_disable()
{
  digitalWrite(C_ENABLE_PIN,HIGH);
}
void A_clockwise()
{
  digitalWrite(A_DIR_PIN,LOW);
}
void B_clockwise()
{
  digitalWrite(B_DIR_PIN,LOW);
}
void C_clockwise()
{
  digitalWrite(C_DIR_PIN,LOW);
}
void A_anticlockwise()
{
  digitalWrite(A_DIR_PIN,HIGH);
}
void B_anticlockwise()
{
   digitalWrite(B_DIR_PIN,HIGH);
}
void C_anticlockwise()
{
  digitalWrite(C_DIR_PIN,HIGH);
}


void  ele_magnet_on()
{
  digitalWrite(12,HIGH);
}
void  ele_magnet_off()
{
  digitalWrite(12,LOW);
}

void pulse_AB()
{
 digitalWrite(A_STEP_PIN,HIGH);digitalWrite(B_STEP_PIN,HIGH);delay(1);
 digitalWrite(A_STEP_PIN,LOW);digitalWrite(B_STEP_PIN,LOW); delay(1);
}
void pwmout(int t)
{
 while(t--)
 {
  pulse_AB();
 }
}

void pulse_A()
{
 digitalWrite(A_STEP_PIN,HIGH); delay(1);
 digitalWrite(A_STEP_PIN,LOW) ; delay(1);
}
void pwmout_A(int t)
{
 while(t--)
 {
  pulse_A();
 }
}


void pulse_B()
{
 digitalWrite(A_STEP_PIN,HIGH); delay(1);
 digitalWrite(A_STEP_PIN,LOW) ; delay(1);
}

void pwmout_B(int t)
{
 while(t--)
 {
  pulse_A();
 }
}
void pulse_C()
{
  digitalWrite(C_STEP_PIN,HIGH);delay(1);
  digitalWrite(C_STEP_PIN,LOW);delay(1);
}
void pwmout_C(int t)
{
  while(t--)
  {
    pulse_C();
  }
}
void x_go_move(int t)
{
 //x=1/2*(A+B)
  A_clockwise();B_clockwise();A_enable();B_enable();
  work_time=worktime(t);
  pwmout(work_time);
}

void x_back_move(int t)
{
 A_anticlockwise(); B_anticlockwise();A_enable();B_enable();
 work_time = worktime(t);
 pwmout(work_time);
}

void x_stop()
{
  A_disable();B_disable();
}

void y_go_move(int t)
{
// y = 1/2*(A-B)
 A_clockwise();B_anticlockwise();A_enable();B_enable();
 work_time = worktime(t);
 pwmout(work_time);
}
void y_back_move(int t)
{
 A_anticlockwise();B_clockwise();A_enable();B_enable();
 work_time = worktime(t);
 pwmout(work_time);
 
}

void y_stop()
{
  A_disable();B_disable();
}

void z_rise_move(int t)
{  C_clockwise();C_enable();
  work_time =worktime(t);// worktime(t);
  pwmout_C(work_time);
}
void z_fall_move(int t)
{
  C_anticlockwise();C_enable();
  work_time = worktime(t);
  pwmout_C(work_time);
}

void z_stop()
{
 C_disable();
}

void xy_go_move(int t)
{
 A_clockwise();A_enable();
 work_time = worktime(t);
 pwmout_A(work_time);
} 

void xy_back_move(int t)
{
  A_anticlockwise();A_enable();
 work_time = worktime(t);
 pwmout_A(work_time);
}

void xy_stop()
{
  A_disable(); B_disable(); 
}

int worktime(int t)
{
 return  (t-(int)'0')*1000;
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
      myservo1.attach(servo_pin1);
      myservo2.attach(servo_pin2);
      myservo3.attach(servo_pin3);
      myservo4.attach(servo_pin4);
      pinMode(A_DIR_PIN,OUTPUT);
      pinMode(A_ENABLE_PIN,OUTPUT);
      pinMode(A_STEP_PIN,OUTPUT);
      pinMode(B_DIR_PIN,OUTPUT);
      pinMode(B_ENABLE_PIN,OUTPUT);
      pinMode(B_STEP_PIN,OUTPUT);
      pinMode(C_DIR_PIN,OUTPUT);
      pinMode(C_ENABLE_PIN,OUTPUT);
      pinMode(C_STEP_PIN,OUTPUT);
      pinMode(12,OUTPUT);
//      digitalWrite(A_ENABLE_PIN,LOW);
 //     digitalWrite(B_ENABLE_PIN,LOW);
//     
      attachInterrupt(2, attach_stop_x, CHANGE);  // pin 21
      attachInterrupt(3, attach_stop_y, CHANGE);  // pin 19
      attachInterrupt(4, attach_stop_z, CHANGE);  // pin 18
      Serial.begin(9600);

 }

int x_co=48,y_co=48,z_co=48, flag = 48;
void loop()
{
     while(Serial.available())
  {
   flag = Serial.read();delay(2);Serial.println(flag);delay(2);
   if( flag == (int)'1')
      {
        x_co=Serial.read();delay(2);
        Serial.println(x_co);delay(2);
        y_co=Serial.read();delay(2);
        Serial.println(y_co);delay(2);
        z_co=Serial.read();delay(2);
        Serial.println(z_co);delay(2);
        
        z_rise_move(z_co);z_stop();

        steering_on(); delay(500);//steering engine work
        z_rise_move(50); z_stop();//wait to ascertain, '2'!
         
         if(y_co>x_co)
            { 
               xy_go_move(x_co); xy_stop(); 
               y_go_move(y_co-x_co);  y_stop();
             }
         else if (y_co==x_co)
             {
               xy_go_move(y_co);  xy_stop();
             }
           else
           {
               xy_go_move(y_co); xy_stop(); 
                x_go_move(x_co-y_co);  x_stop();
           }
           
           ele_magnet_on();
           z_fall_move(49);z_stop();  // to be ascertain
           
           z_rise_move(49);z_stop();
            

          if(y_co>x_co)
            { 
               xy_back_move(x_co); xy_stop(); 
               y_back_move(y_co-x_co);  y_stop();
             }
         else if (y_co==x_co)
             {
               xy_back_move(y_co);  xy_stop();
             }
           else
           {
               xy_back_move(y_co); xy_stop(); 
                x_back_move(x_co-y_co);  x_stop();
           }
           

            z_fall_move(50); z_stop();
          
            steering_reset();
            delay(500);

            z_fall_move(z_co);
            z_stop();
      
            ele_magnet_off();
      
            //add limit switch
            x_go_move(100);
            y_go_move(100);
            z_fall_move(100);
               
        }
      else 
         {   
        //  Serial.println('a');delay(2);
          x_co=Serial.read();delay(2);
          Serial.println(x_co);delay(2);
          y_co=Serial.read();delay(2);
          Serial.println(y_co);delay(2);
          z_co=Serial.read();delay(2);
          Serial.println(z_co);delay(2);
         
           ele_magnet_on();
           z_rise_move(z_co);z_stop();

            steering_on(); delay(500);//steering engine work
            z_rise_move(50); delay(2000);//wait to ascertain,'2'
       
            if(y_co>x_co)
            { 
               xy_go_move(x_co); xy_stop(); 
               y_go_move(y_co-x_co);  y_stop();
             }
           else if (y_co==x_co)
             {
               xy_go_move(y_co);  xy_stop();
             }
           else
           {
               xy_go_move(y_co); xy_stop(); 
                x_go_move(x_co-y_co);  x_stop();
           }
            
            z_fall_move(49); z_stop();  // to  be ascertain
            ele_magnet_off();

            z_rise_move(49);z_stop();
        
            if(y_co>x_co)
            { 
               xy_back_move(x_co); xy_stop(); 
               y_back_move(y_co-x_co);  y_stop();
             }
         else if (y_co==x_co)
             {
               xy_back_move(y_co);  xy_stop();
             }
           else
           {
               xy_back_move(y_co); xy_stop(); 
                x_back_move(x_co-y_co);  x_stop();
           }
  

            z_fall_move(50);  z_stop();
            steering_reset();delay(500);
            
            z_fall_move(z_co);
            z_stop();
  

           
            //add limit switch
            x_go_move(100);
            y_go_move(100);
            z_fall_move(100);
          }
             
      }
}
