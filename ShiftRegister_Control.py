# Title:        Shift Register Output Control with Micropython (for Raspberry Pi Pico)
# 
# Description:  This shows how to use a shift out bits to a shift register in Micropython.
# Date:         12/04/2021
# Author:       Azam Fahmy

from machine import Pin
import utime

dataPin = Pin(4,Pin.OUT) #dont change the name of this pin! (used in shiftOut)
latchPin = Pin(3,Pin.OUT)
clockPin = Pin(2,Pin.OUT)

def shiftOut(data):
    for k in range(8):
        dataPin.value((data >> k) & 1)
        clockPin.value(1)
        clockPin.value(0)
        
        
while True: 
    for i in range(255):
        latchPin.value(0)
        shiftOut(i)         #similar to arduino's shiftOut function
        latchPin.value(1)
        
        utime.sleep(0.5)

