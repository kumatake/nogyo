#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import RPi.GPIO as GPIO
import time
 
#使うGPIOピンの番号
IO_NO = 4
IO_NO2 = 17
 
print("press ^C to exit program ...\n")
 
# GPIOピン番号を用いる
GPIO.setmode(GPIO.BCM)
# 基板上のピン番号を用いる
#GPIO.setmode(GPIO.BOARD)
 
GPIO.setup(IO_NO, GPIO.OUT)
GPIO.setup(IO_NO2, GPIO.OUT)

 
try:
	while True:
 		GPIO.output(IO_NO, True)
 		GPIO.output(IO_NO2, True)
 		time.sleep(10)
 		GPIO.output(IO_NO, False)
 		GPIO.output(IO_NO2, False)
 		time.sleep(10)
except KeyboardInterrupt:
 print("detect key interrupt\n")
 
GPIO.cleanup()
print("Program exit\n")