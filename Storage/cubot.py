import cubot_lib

#Create an instance, named 'bot', of object 'Control' from 'cubot_lib.py'
#    Object Control comes pre-initialized with 6 servos and 3 continuous servos
bot = cubot_lib.Control()

#The 6 servos are referenced in an array named 'servo'
#The 3 continuous servos are referenced in an array named 'cServo'
#You can assign these pre-defined servos to any variables
arm1Servo1 = bot.servo[0]
arm1Servo2 = bot.servo[1]
arm1cServo = bot.cServo[0]

arm2Servo1 = bot.servo[2]
arm2Servo2 = bot.servo[3]
arm2cServo = bot.cServo[1]

arm3Servo1 = bot.servo[4]
arm3Servo2 = bot.servo[5]
arm3cServo = bot.cServo[2]

#####There are 3 different move functions, listed below:#####

#Function move(int angle, double rate) //from Servo class
#    'angle' specifies the desired angle that the selected servo must move to (from 0 to 180)
#    'rate' specifies the amount of time (in seconds) the servo will pause between each angle
arm1Servo1.move(90,0.0001)
arm3Servo2.move(54,0.0005)

#Function move(double direction, double period) //from ContinuousServo class
#    'direction' specifes the rotational direction and speed (-1 to 1)
#    'period' specifies the period of time, in seconds, the cServo must spin
arm1cServo.move(1, 1)
arm2cServo.move(-0.3, 0.5)

#Function move(int angle0, int angle1, int angle2, int angle3, int angle4, int angle5) //from Control class
#     This function allows servos to move synchronously
#     Each on these values represent the angle that the respected servo must move to.
#     move(0, 0, 0, 180, 180, 180) //this statement will move servos 0-2 to 0 degrees and servos 3-5 to 180 degrees
bot.move(0, 0, 0, 180, 180, 180)

#Always collect your garbage!
#All servos are set to return to 90 degrees upon deletion
del bot
del arm1Servo1
del arm1Servo2
del arm2Servo1
del arm2Servo2
del arm3Servo1
del arm3Servo2
del arm1cServo
del arm2cServo
del arm3cServo