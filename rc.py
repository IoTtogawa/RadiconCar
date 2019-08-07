# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import pigpio
import time

LeftMotor =  [13, 27]
RightMotor = [12, 22]

pi = pigpio.pi()

M = 1000000
FREQ = 1000

def setup():

	#プログラム内でGPIO番号でピンを指定するための宣言
	GPIO.setmode(GPIO.BCM)

	#出力ピンとして設定
	GPIO.setup(LeftMotor, GPIO.OUT)
	GPIO.setup(RightMotor, GPIO.OUT)

	#この二つは HIGH or LOW
	GPIO.output(LeftMotor[1], GPIO.LOW)
	GPIO.output(RightMotor[1], GPIO.LOW)

	#この二つはハードウェアPWMで出力電圧をコントロール
	#最低でも50%くらいで出力しないと電流不足でモーターが回らないので注意
	pi.set_mode(LeftMotor[0], pigpio.OUTPUT)
	pi.set_mode(RightMotor[0], pigpio.OUTPUT)

	#pi.hardware_PWM(GPIOピン番号, 周波数[Hz], duty比[100% = 1M])で出力
	#例: pi.hardware_PWM(LeftMotor[0], FREQ, 0.6*M) => 左タイヤを60%出力で前進

#juliustest.pyの終了時にこの関数を実行しないと，次回以降正常に動かなくなる(かも)
def destroy():
	pi.set_mode(LeftMotor[0], pigpio.INPUT)
	pi.set_mode(RightMotor[0], pigpio.INPUT)
	pi.stop()

def stop():
	GPIO.output(LeftMotor[1], GPIO.LOW)
	GPIO.output(RightMotor[1], GPIO.LOW)
	pi.hardware_PWM(LeftMotor[0], FREQ, 0)
	pi.hardware_PWM(RightMotor[0], FREQ, 0)

def forward():
	GPIO.output(LeftMotor[1], GPIO.LOW)
	GPIO.output(RightMotor[1], GPIO.LOW)
	pi.hardware_PWM(LeftMotor[0], FREQ, 1.0*M)
	pi.hardware_PWM(RightMotor[0], FREQ, 1.0*M)

def back():
	GPIO.output(LeftMotor[1], GPIO.HIGH)
	GPIO.output(RightMotor[1], GPIO.HIGH)
	pi.hardware_PWM(LeftMotor[0], FREQ, 0)
	pi.hardware_PWM(RightMotor[0], FREQ, 0)

def leftTurn():
	GPIO.output(LeftMotor[1], GPIO.LOW)
	GPIO.output(RightMotor[1], GPIO.LOW)
	pi.hardware_PWM(LeftMotor[0], FREQ, 0.5*M)
	pi.hardware_PWM(RightMotor[0], FREQ, 1*M)

def leftRoll():
	GPIO.output(LeftMotor[1], GPIO.HIGH)
	GPIO.output(RightMotor[1], GPIO.LOW)
	pi.hardware_PWM(LeftMotor[0], FREQ, 0)
	pi.hardware_PWM(RightMotor[0], FREQ, 1*M)

def rightTurn():
	GPIO.output(LeftMotor[1], GPIO.LOW)
	GPIO.output(RightMotor[1], GPIO.LOW)
	pi.hardware_PWM(LeftMotor[0], FREQ, 1*M)
	pi.hardware_PWM(RightMotor[0], FREQ, 0.5*M)

def rightRoll():
	GPIO.output(LeftMotor[1], GPIO.LOW)
	GPIO.output(RightMotor[1], GPIO.HIGH)
	pi.hardware_PWM(LeftMotor[0], FREQ, 1*M)
	pi.hardware_PWM(RightMotor[0], FREQ, 0)
