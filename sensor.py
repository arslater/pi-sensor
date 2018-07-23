
## script to read sensor values from scale
from tkinter import *
import tkinter.font
import RPi.GPIO as gpio
import time

RS = 18
EN = 23
D4 = 24
D5 = 25
D6 = 8
D7 = 7

DT = 27
SCK = 17

m1 = 12
m2 = 1

def readCount():
  i = 0
  Count = 0
  gpio.setup(DT, gpio.OUT)
  gpio.output(DT,1)
  gpio.output(SCK,0)
  gpio.setup(DT, gpio.IN)

  while gpio.input(DT) == 1:
      i = 0
  for i in range(24):
        gpio.output(SCK,1)
        Count = Count<<1

        gpio.output(SCK,0)
        #time.sleep(0.001)
        if gpio.input(DT) == 0: 
            Count = Count + 1
        
  gpio.output(SCK,1)
  Count = Count^0x800000
  gpio.output(SCK,0)
  return Count 

def updateColor(val, threshold):

    if val < threshold:
        #flash red
        my_window.configure(bg = "red")
    else:
      my_window.configure(bg = "green")


my_window = Tk()
my_window.title ("Sensor Scale")
my_window.configure(background = "green")

my_window.mainloop()

threshold = 2 # will be some number

while 1:
	val = readCount()
	print(val)
	after(50, updateColor(val, threshold))
