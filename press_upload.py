#-*-coding:utf-8-*-
import RPi.GPIO as GPIO  #导入RPi.GPIO模块
import time   #导入时间模块，用于延时
import os
GPIO.setwarnings(False)  #屏蔽警告信息
#---第一步：设置引脚编码模式
GPIO.setmode(GPIO.BCM)  #设置引脚为BCM编码
#---第二步：设置引脚方向----
KEY = 18
GPIO.setup(KEY,GPIO.IN)  #设置按键为输入
#----第三步：循环判断按键是否按下
while 1:
    if GPIO.input(KEY)==1:#按下（该按键模块，当松开的时候是低电平，按下时高电平）
       time.sleep(0.02)  #延时20ms  绕过抖动区间，为了防抖
       if(GPIO.input(KEY)==1):    #再次判断是否在按下的状态(判断是否在稳定区间)
          while(GPIO.input(KEY)==1): #等待松手
               pass   #占位行
          #实现按键要做的事情
          print('button precessed')
          os.system("sudo /home/stevek/run_camera_upload.sh")
          time.sleep(0.5)
          print('photo uploaded')

