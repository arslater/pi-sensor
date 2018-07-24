import RPi.GPIO as gpio
import time

RS =18
EN =23
D4 =24
D5 =25
D6 =8
D7 =7

DT =27
SCK=17

m1=12
m2=1

def readCount():
  i=0
  Count=0
  gpio.setup(DT, gpio.OUT)
  gpio.output(DT,1)
  gpio.output(SCK,0)
  gpio.setup(DT, gpio.IN)

  while gpio.input(DT) == 1:
      i=0
  for i in range(24):
        gpio.output(SCK,1)
        Count=Count<<1

        gpio.output(SCK,0)
        #time.sleep(0.001)
        if gpio.input(DT) == 0: 
            Count=Count+1
        
  gpio.output(SCK,1)
  Count=Count^0x800000
  gpio.output(SCK,0)

while 1:
  count= readCount()
  w=0
  w=(count-sample)/106
  print w,"g"
  if w>100:  
    setCursor(0,0)
    lcdprint("Gate Opened ")
    if flag == 0:
      gpio.output(m1, 1)
      gpio.output(m2, 0)
      time.sleep(1.3)
      gpio.output(m1, 0)
      gpio.output(m2, 0)
      time.sleep(1.5)
      flag=1;
      lcdclear()
  elif w<100:
    setCursor(0,0)
    lcdprint("Gate Closed ")
    if flag==1:
      gpio.output(m1, 0)
      gpio.output(m2, 1)
      time.sleep(1.3)
      gpio.output(m1, 0)
      gpio.output(m2, 0)
      time.sleep(2)
      flag=0
  time.sleep(0.5)  

return Count 
