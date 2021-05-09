import Bot2
import time
from picamera import PiCamera

bot = Bot2.Control()
camera = PiCamera()

def sequence(angle, rate, first, last):
    if first < last:
        while first <= last:
            bot.servo[first].move(angle, rate)
            first += 1
    else:
        while first >= last:
            bot.servo[first].move(angle, rate)
            first -= 1
            
def clo():
    bot.servo[0].moveFast(42)

def cou():
    bot.servo[0].moveFast(222)

def cen():
    bot.servo[0].moveFast(132)

def rel():
    bot.servo[9].moveFast(167)

def gri():
    bot.servo[9].moveFast(50)
    
def mid():
    bot.servo[9].moveFast(135)

def dow():
    bot.servo[1].moveFast(190)
    
def up():
    bot.servo[1].moveFast(100)
    
def rotateTest():
    arm = bot.servo[0]
    arm.moveFast(42)
    time.sleep(1)
    arm.moveFast(222)
    time.sleep(1)
    arm.moveFast(132)
    time.sleep(1)

def gripTest():
    arm = bot.servo[9]
    #arm.moveFast(50) #min
    arm.moveFast(50) #3x3
    time.sleep(20)
    arm.moveFast(167) #max
    time.sleep(1)
    arm.moveFast(135)
    time.sleep(1)
    
def demoSequence():
    rel()
    dow()
    time.sleep(1)
    gri()
    time.sleep(1)
    up()
    time.sleep(1)
    clo()
    time.sleep(0.5)
    cen()
    time.sleep(0.5)
    cou()
    time.sleep(0.5)
    clo()
    time.sleep(0.8)
    cen()
    time.sleep(0.5)
    dow()
    time.sleep(1)
    rel()
    time.sleep(0.5)
    mid()
    up()
    time.sleep(1)
    

#demoSequence()
#dow()
#time.sleep(20)
#clo()
#time.sleep(1)
#cen()
#time.sleep(1)
#rel()
#time.sleep(10)
    
#arm0 = bot.servo[0]
#arm1 = bot.servo[1]
#arm2 = bot.servo[2]
#arm3 = bot.servo[3]
#arm4 = bot.servo[4]
#arm5 = bot.servo[5]
#arm6 = bot.servo[6]
#arm7 = bot.servo[7]
#arm8 = bot.servo[8]
#arm9 = bot.servo[9]
#currentarm = arm2

testall = 0 #0 or 1, enables the additional test at the end moving each servo
testone = 0 #0 or 1, enables the individual servo test
testcamera = 0 #0 or 1, whether to have the camera take a picture
testextended = 0 #0 or 1, tests additional angles between 180 and 270
testfull = 0 #0 or 1, enables additional full range angle test
testprecise = 0 #0 or 1, enables precise angle testing

#currentarm.moveFast(0)
#time.sleep(2)
#currentarm.moveFast(135)
#time.sleep(2)

imagelocation = '/home/pi/Desktop/mode5_'
extension = '.jpg'
#camera.rotation = 180 #flips the image upsidedown if the camera is
camera.sensor_mode = 5; #there are different modes with different FOV, 5 worked best

if testcamera == 1:
    try:
        camera.start_preview()
        time.sleep(1)
        for i in range (3):
            time.sleep(10)
            camera.capture(imagelocation + str(i) + extension)
            print('image saved at:')
            print(imagelocation + str(i) + extension)
    finally:
        camera.stop_preview()
        camera.close()
            

#print(arm1.servo.angle)
#print(arm1.currentAngle)

#arm4.moveFast(0)
#time.sleep(1)
#arm4.moveFast(270)
#time.sleep(2)


#currentarm.moveFast(135)
#time.sleep(1)
#currentarm.move(255, 0.005) #down max
#time.sleep(1)
#currentarm.move(75, 0.005) #up max
#time.sleep(1)
#currentarm.moveFast(270)
#time.sleep(2)
#currentarm.move(135, 0.005)
#time.sleep(1)

if testone == 1:
    currentarm.move(0, 0.001)
    print(currentarm.servo.angle)
    time.sleep(1)
    currentarm.move(45, 0.001)
    print(currentarm.servo.angle)
    time.sleep(1)
    currentarm.move(90, 0.001)
    print(currentarm.servo.angle)
    # Precise Angle testing section
    if testprecise == 1:
        time.sleep(1)
        currentarm.move(45, 0.001)
        print(currentarm.servo.angle)
        time.sleep(1)
        currentarm.move(55, 0.001)
        print(currentarm.servo.angle)
        time.sleep(1)
        currentarm.move(70, 0.001)
        print(currentarm.servo.angle)
        time.sleep(1)
        currentarm.move(75, 0.001)
        print(currentarm.servo.angle)
        time.sleep(1)
        currentarm.move(90, 0.001)
        print(currentarm.servo.angle)
    time.sleep(1)
    currentarm.move(135, 0.001)
    print(currentarm.servo.angle)
    time.sleep(1)
    currentarm.move(180, 0.001)
    print(currentarm.servo.angle)
    if testextended == 1:
        time.sleep(1)
        currentarm.move(225, 0.001)
        print(currentarm.servo.angle)
        time.sleep(1)
        currentarm.move(270, 0.001)
        print(currentarm.servo.angle)
    time.sleep(1)
    currentarm.move(0, 0.001)
    if testfull == 1:
        time.sleep(1)
        currentarm.move(270, 0.1)
        time.sleep(1)
        currentarm.move(0, 0.001)

if testall == 1:
    time.sleep(1)
    sequence(0, 0.001, 0, 3)
    time.sleep(1)
    sequence(180, 0.001, 0, 3)
    time.sleep(1)
    sequence(0, 0.001, 0, 3)

del bot