#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import RPi.GPIO as GPIO
import time
 
IO_NO = 4
 
print("press ^C to exit program ...\n")
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(IO_NO, GPIO.IN)
 
try:
 while True:
  print(GPIO.input(IO_NO))
  time.sleep(1)
except KeyboardInterrupt:
 print("detect key interrupt\n")
 
GPIO.cleanup()
print("Program exit\n")