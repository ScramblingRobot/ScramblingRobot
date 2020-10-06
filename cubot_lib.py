class Servo:
    'Servo object'
    
#    from adafruit_servokit import ServoKit
#    import adafruit_motor.servo
    import time
    
    def __init__(self, ind, kit, pin, pulseMin, pulseMax, angle):
        self.index = ind
#        self.servo = kit.servo[pin]
#        self.servo.set_pulse_width_range(pulseMin, pulseMax)
#        self.servo.angle = angle
        self.currentAngle = angle
        self.currentDirection = 0
        print (self.__class__.__name__, "instance", self.index, "created")
        
    def __del__(self):
        self.move(90,0.0001)
        print (self.__class__.__name__, "instance", self.index, "has been garbage collected")
        
    def move(self, angle, rate):
        while self.currentAngle != angle:
            if self.currentAngle < angle:
                self.currentAngle += 1
#                self.servo.angle = self.currentAngle
                Servo.time.sleep(rate)
                
            else:
                self.currentAngle -= 1
#                self.servo.angle = self.currentAngle
                Servo.time.sleep(rate)
        print ("Servo", self.index, "moved to angle", self.currentAngle)

class ContinuousServo:
    'Continuous Servo object'
    
#    from adafruit_servokit import ServoKit
#    import adafruit_motor.servo
    import time
    
    def __init__(self, ind, kit, pin):
        self.index = ind
#        self.servo = kit.continuous_servo[pin]
        print (self.__class__.__name__, "instance", self.index, "created")
        
    def __del__(self):
        print (self.__class__.__name__, "instance", self.index, "has been garbage collected")
        
    def move(self, direction, period):
#        self.servo.throttle = direction
        Servo.time.sleep(period)
#        self.servo.throttle = 0
        if direction > 0:
            text = "forward"
        else:
            text = "backward"
        print ("Continuous servo", self.index, "moved", text, "for", period, "seconds")

class Control:
    'Control all servos via I2C communication to PCA9685 controller'
#    from adafruit_servokit import ServoKit
#    import adafruit_motor.servo
    import time

    kit = 0 #mock value for 'kit'
#    kit = ServoKit(channels = 16)
    
    def __init__(self):
        class_name = self.__class__.__name__
        print (class_name, "instance created")
        self.servo = []
        self.cServo = []
        self.servo.append(Servo(0, Control.kit, 0, 500, 2500, 90))
        self.servo.append(Servo(1, Control.kit, 1, 500, 2500, 90))
        self.servo.append(Servo(2, Control.kit, 3, 500, 2500, 90))
        self.servo.append(Servo(3, Control.kit, 5, 500, 2500, 90))
        self.servo.append(Servo(4, Control.kit, 7, 500, 2500, 90))
        self.servo.append(Servo(5, Control.kit, 9, 500, 2500, 90))
        self.cServo.append(ContinuousServo(0, Control.kit, 11))
        self.cServo.append(ContinuousServo(1, Control.kit, 13))
        self.cServo.append(ContinuousServo(2, Control.kit, 15))
    
    def __del__(self):
        print (self.__class__.__name__, "instance has been garbage collected")
    
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
#                    self.servo[i].servo.angle = self.servo[i].currentAngle
                    if self.servo[i].currentAngle == angle[i]:
                        self.servo[i].currentDirection = 0
                        print ("Servo", i, "moved to angle", self.servo[i].currentAngle)