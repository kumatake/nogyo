#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import RPi.GPIO as GPIO
import time
 
#使うGPIOピンの番号
IO_NO = 4
 
print("press ^C to exit program ...\n")
 
# GPIOピン番号を用いる
GPIO.setmode(GPIO.BCM)
# 基板上のピン番号を用いる
#GPIO.setmode(GPIO.BOARD)
 
GPIO.setup(IO_NO, GPIO.OUT)
 
try:
 while True:
  GPIO.output(IO_NO, True)
  time.sleep(0.5)
  GPIO.output(IO_NO, False)
  time.sleep(0.5)
except KeyboardInterrupt:
 print("detect key interrupt\n")
 
GPIO.cleanup()
print("Program exit\n")