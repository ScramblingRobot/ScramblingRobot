#Author: Anh (Steven) Nguyen
#Created: 09/12/2020
#Last modified: 04/29/2021 by Anh (Steven) Nguyen

import time

class Servo:
    'Servo object'
    
    from adafruit_servokit import ServoKit
    
    def __init__(self, ind, kit, pin, pulseMin, pulseMax, angle):
        self.index = ind
        self.servo = kit.servo[pin]
        self.servo.set_pulse_width_range(pulseMin, pulseMax)
        self.servo.angle = angle
        self.currentAngle = angle
        self.currentDirection = 0
        print ("CREATED:", self.__class__.__name__, self.index)
        
    def __del__(self):
        print ("DELETED:", self.__class__.__name__, self.index)
        
    def move(self, visualangle, rate):
        angle = round(visualangle/1.5)
        
        while self.currentAngle != angle:
            if self.currentAngle < angle:
                self.currentAngle += 1
                self.servo.angle = self.currentAngle
                time.sleep(rate)
                
            else:
                self.currentAngle -= 1
                self.servo.angle = self.currentAngle
                time.sleep(rate)
        #print ("Servo", self.index, "moved to angle", self.currentAngle*1.5)
        
    def moveFast(self, visualangle):
        self.currentAngle = round(visualangle/1.5)
        self.servo.angle = self.currentAngle
        #print ("Servo", self.index, "moved to angle", round(self.servo.angle*1.5))

class Control:
    'Control all servos via I2C communication to PCA9685 controller'
    from adafruit_servokit import ServoKit
    import adafruit_motor.servo

    kit = ServoKit(channels = 16)
    
    def __init__(self):
        class_name = self.__class__.__name__
        print ("CREATED:", self.__class__.__name__, "object")
        self.servo = []
        self.cServo = []
        self.servo.append(Servo(0, Control.kit, 0, 445, 2355, round(135/1.5 - 2))) #center Rotate
        self.servo.append(Servo(1, Control.kit, 1, 445, 2375, round(135/1.5 - 45))) #center Move
        self.servo.append(Servo(2, Control.kit, 2, 435, 2360, round(135/1.5 - 2))) #right Rotate
        self.servo.append(Servo(3, Control.kit, 3, 500, 2400, round(135/1.5))) #broken servo :(
        
        self.servo.append(Servo(4, Control.kit, 4, 450, 2385, round(135/1.5))) #left Rotate
        self.servo.append(Servo(5, Control.kit, 5, 480, 2400, round(135/1.5 - 5))) #left Move
        self.servo.append(Servo(6, Control.kit, 6, 485, 2420, round(135/1.5 + 8))) #right Move
        self.servo.append(Servo(7, Control.kit, 7, 510, 2405, round(135/1.5))) #left Grip
        self.servo.append(Servo(8, Control.kit, 8, 520, 2430, round(135/1.5))) #right Grip
        self.servo.append(Servo(9, Control.kit, 9, 520, 2430, round(135/1.5 + 30))) #center Grip
    
    def __del__(self):
        print ("DELETED:", self.__class__.__name__, "object")
    
    def move(self, a0, a1, a2, a3, a4, a5):
        angle = [a0, a1, a2, a3, a4, a5]
        for i in range (6):
            if self.servo[i].currentAngle == angle[i]:
                self.servo[i].currentDirection = 0
            if self.servo[i].currentAngle < angle[i]:
                self.servo[i].currentDirection = 1
            if self.servo[i].currentAngle > angle[i]:
                self.servo[i].currentDirection = -1
        flag = True
        while flag:
            flag = False
            for i in range (6):
                if self.servo[i].currentDirection != 0:
                    flag = True
                    self.servo[i].currentAngle += self.servo[i].currentDirection
                    self.servo[i].servo.angle = self.servo[i].currentAngle
                    if self.servo[i].currentAngle == angle[i]:
                        self.servo[i].currentDirection = 0
                        print ("Servo", i, "moved to angle", self.servo[i].currentAngle)
                    
        
    
    
        