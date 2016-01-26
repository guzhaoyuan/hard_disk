/*
*control three
*2016/1/26
*/
int stepping_1=11,stepping_2=10,stepping_3=9; //PWM output
int dir_1=8,dir_2=7,dir_3=6;
int offline_1=5  ,offline_2=4,offline_3=3;

int a=127;
//封装控制步进电机顺时针转
void clockwise(int stepping_pin,int gpio_pin,int dir_pin,int delays)
{
  digitalWrite(gpio_pin,LOW);//on-line ,脱机负
  digitalWrite(dir_pin, LOW);  //clockwise 方向负
  analogWrite(stepping_pin,a);
   delay(delays);
   stop_hold(gpio_pin);
}

//封装控制步进电机逆时针转
void anticlockwise(int stepping_pin,int gpio_pin,int dir_pin,int delays)
{
  digitalWrite(gpio_pin,LOW);//on-line ,脱机负
  digitalWrite(dir_pin, HIGH);  //clockwise 方向+
  analogWrite(stepping_pin,a);
   delay(delays);
   stop_hold(gpio_pin);
}

//封装控制步进电机停
void stop_hold(int gpio_pin)
{
  digitalWrite(gpio_pin,HIGH);//off-line ,脱机正
}
void setup() 
{
      pinMode(stepping_1,OUTPUT);
      pinMode(dir_1,OUTPUT);
      pinMode(offline_1,OUTPUT);
      pinMode(stepping_2,OUTPUT);
      pinMode(dir_2,OUTPUT);
      pinMode(offline_2,OUTPUT);
      pinMode(stepping_3,OUTPUT);
      pinMode(dir_3,OUTPUT);
      pinMode(offline_3,OUTPUT);
      Serial.begin(9600);
 }


char ch1=0,ch2=0,ch3=0;
//int delay1,delay2,delay3;
void loop()
{
  while(Serial.available()){
   ch1=Serial.read();//delay(2);//Serial.println(ch1);
   ch2=Serial.read();//delay(2);//Serial.println(ch2);
   ch3=Serial.read();//delay(2);//Serial.println(ch3);
  }
   
   if(ch3!='0')
   {//Serial.println(ch3);
   clockwise(stepping_3,offline_3,dir_3,1000*(ch3-'0'));   
}
else
{
  stop_hold(offline_3);
}
  if(ch2!='0')
  {//Serial.println(ch2);
   clockwise(stepping_2,offline_2,dir_2,1000*(ch2-'0'));
   //Serial.println(ch1);Serial.println(ch2);Serial.println(ch3);
   }
   if(ch1!='0')
   {Serial.println(ch1);
   anticlockwise(stepping_1,offline_1,dir_1,1000*(ch1-'0'));
     //Serial.println(ch1);Serial.println(ch2);Serial.println(ch3);
     stop_hold(offline_2);
   }
   else
   {
     stop_hold(offline_1);
   }
}
//it's ok

