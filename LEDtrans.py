#!/usr/bin/python

import RPi.GPIO as GPIO, time
import time

def main():
   duration = 0.1
   
   def LED_setup():
      GPIO.setmode(GPIO.BOARD)
      GPIO.setwarnings(False)
      GPIO.setup(18, GPIO.OUT)

   def LED_ON():
      GPIO.output(18, GPIO.HIGH)
      time.sleep(duration)

   def LED_OFF():
      GPIO.output(18, GPIO.LOW)
      time.sleep(duration)

   def bB():
      LED_OFF()
      LED_OFF()
      LED_OFF()
      LED_ON()
   
   def bA():
      LED_OFF()
      LED_OFF()
      LED_ON()
      LED_OFF()

   def bC():
      LED_OFF()
      LED_OFF()
      LED_ON()
      LED_ON()

   def bO():
      LED_OFF()
      LED_ON()
      LED_OFF()
      LED_OFF()

   def bN():
      LED_OFF()
      LED_ON()
      LED_OFF()
      LED_ON()

   def bI():
      LED_OFF()
      LED_ON()
      LED_ON()
      LED_OFF()

   def bT():
      LED_OFF()
      LED_ON()
      LED_ON()
      LED_ON()

   def bS():
      LED_ON()
      LED_OFF()
      LED_OFF()
      LED_OFF()

   def bSpace():
      LED_ON()
      LED_OFF()
      LED_OFF()
      LED_ON()
   
   def bTest():
      LED_ON()
      LED_OFF()
      LED_ON()
      LED_OFF()

   LED_setup()

   number = 2
   while(number):
      print ("LED on")
      GPIO.output(18, GPIO.HIGH)
      time.sleep(1)
      print ("LED off")
      GPIO.output(18, GPIO.LOW)
      time.sleep(1)
      number -= 1

   time.sleep(1)
   
   number = 5
   LED_ON()
   time.sleep(0.02)
   LED_OFF()

   start = time.time()
   
   while(number):
      bB()
      bA()
      bC()
      bO()
      bN()
      bSpace()
      number -= 1

   end = time.time()
   duration = end - start
   print(duration)
   print (120/duration)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
   GPIO.cleanup()


if __name__ == '__main__':
    main()
