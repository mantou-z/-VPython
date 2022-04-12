# -*- coding: utf-8 -*-
from prompt_toolkit import prompt
from vpython import *
import cv2

# 单摆物理量
L = 5
theta = pi/6
theta_ref = pi/4
g = 10

# 确定是否施加外力  并且输入KP KD数值
str1 = input("give a force?(y or n)")
if str1 == "y":
	KP = input("KP = ")
	print ("your KP is " + KP)
	KD = input("KD = ")
	print ("your KD is " + KD)
	scene.title = "单摆测试！ 初始角度："+ str(int(theta/pi*360))+ "   期望角度："+ str(int(theta_ref/pi*360))+ "   KP:"+ KP + "  KD:" + KP
else:
	KP = 0
	KD = 0
	scene.title = "单摆测试！ 初始角度："+ str(int(theta/pi*360))+ "   期望角度："+ str(int(theta_ref/pi*360))+ "   KP:0   KD:0"
KI = 200 #数值给大一点？
F = 0

# 单击鼠标切换F
run = False
def runnning(ev):
	global run
	run = not run
scene.bind('mousedown',runnning)

# 创建单摆
base = box(pos=vector(0, 0, 0), size=vector(2, 0.5, 1), color=color.white)
ball = sphere(pos=vector(L*sin(theta), -L*cos(theta), 0), radius=0.25, color=color.white)
line = cylinder(pos=base.pos, axis=(ball.pos-base.pos), radius=0.05, color=color.white)
 
vel = 0
dt = 0.005
t = 0
while True:
	rate(50) #改变rate可以改变动画速率
	if run and str1 == "y":
		F = int(KP) * (theta_ref - theta) + int(KD) * (0 - vel) + KI* (theta_ref - theta)*dt# -*- coding: utf-8 -*-
from prompt_toolkit import prompt
from vpython import *
import cv2

# 单摆物理量
L = 5
theta = pi/3
theta_ref = pi/2
g = 10

# 确定是否施加外力  并且输入KP KD数值
str1 = input("give a force?(y or n)")
if str1 == "y":
	KP = input("KP = ")
	print ("your KP is " + KP)
	KD = input("KD = ")
	print ("your KD is " + KD)
	scene.title = "单摆测试！ 初始角度："+ str(int(theta/pi*180))+ "   期望角度："+ str(int(theta_ref/pi*180))+ "   KP:"+ KP + "  KD:" + KP
else:
	KP = 0
	KD = 0
	scene.title = "单摆测试！ 初始角度："+ str(int(theta/pi*180))+ "   期望角度："+ str(int(theta_ref/pi*180))+ "   KP:0   KD:0"
KI = 200 #数值给大一点？
F = 0

# 单击鼠标切换F
run = False
def runnning(ev):
	global run
	run = not run
scene.bind('mousedown',runnning)

# 创建单摆
base = box(pos=vector(0, 0, 0), size=vector(2, 0.5, 1), color=color.white)
ball = sphere(pos=vector(L*sin(theta), -L*cos(theta), 0), radius=0.25, color=color.white)
line = cylinder(pos=base.pos, axis=(ball.pos-base.pos), radius=0.05, color=color.white)
 
vel = 0
dt = 0.005
t = 0
while True:
	rate(50) #改变rate可以改变动画速率
	if run and str1 == "y":
		F = int(KP) * (theta_ref - theta) + int(KD) * (0 - vel) + KI* (theta_ref - theta)*dt
	else:
		F = 0
	acc = - g / L * sin(theta) + F
	vel = vel + acc * dt
	theta = theta + vel * 180/pi * dt
	if str1 == "y":
		scene.caption="单击鼠标切换是否施加外力\ntheta:   "+ str(int(theta/pi*180))
	else:
		scene.caption="theta:   "+ str(int(theta/pi*180))
	ball.pos = vector(L*sin(theta), -L*cos(theta), 0)
	line.axis = ball.pos - vector(0, 0, 0)
	t = t + dt
	print (theta/pi*180)

	else:
		F = 0
	acc = - g / L * sin(theta) + F
	vel = vel + acc * dt
	theta = theta + vel * 180/pi * dt
	if str1 == "y":
		scene.caption="单击鼠标切换是否施加外力\ntheta:   "+ str(int(theta/pi*360))
	else:
		scene.caption="theta:   "+ str(int(theta/pi*360))
	ball.pos = vector(L*sin(theta), -L*cos(theta), 0)
	line.axis = ball.pos - vector(0, 0, 0)
	t = t + dt
	print (theta/pi*360)
