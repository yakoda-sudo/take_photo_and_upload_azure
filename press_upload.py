#-*-coding:utf-8-*-
import RPi.GPIO as GPIO  
import time
import os
GPIO.setwarnings(False)  #set alarm as false

GPIO.setmode(GPIO.BCM)  #config GPIO ports mode as BCM
#---configure the target port for button---
KEY = 18
GPIO.setup(KEY,GPIO.IN)  
#----check if the button pressed or not
while 1:
    if GPIO.input(KEY)==1:#press
       time.sleep(0.02)  #delay 20ms to bypass the unstable state
       if(GPIO.input(KEY)==1):    #check if its in pressed 
          while(GPIO.input(KEY)==1): #waiting for loose
               pass
          #do your work below
          print('button precessed')
          os.system("sudo /home/stevek/run_camera_upload.sh")
          time.sleep(0.5)
          print('photo uploaded')
          os.system("sudo /home/stevek/run_ephoto1.sh")
