#Author: Anh (Steven) Nguyen
#Created: 09/12/2020
#Last modified: 04/29/2021 by Anh (Steven) Nguyen
import Bot2
import time

class Arm:
    'Arm object'
    
    def __init__(self, cube, moveServo, gripServo, rotateServo, moveMaxAngle, moveMinAngle, moveMaxPosition, moveMinPosition, gripMaxAngle, gripMinAngle, gripMaxPosition, rotateClAngle, rotateCcAngle):
        self.moveServo = moveServo
        self.gripServo = gripServo
        self.rotateServo = rotateServo
        self.hasCube = False
        self.moveInitAngle = round(moveServo.currentAngle * 1.5) #int - initial angle of move servo
        self.gripInitAngle = round(gripServo.currentAngle * 1.5) #int - initial angle of grip servo
        self.rotateInitAngle = round(rotateServo.currentAngle * 1.5) #int - initial angle of rotate servo
        self.moveMaxAngle = moveMaxAngle
        self.moveMinAngle = moveMinAngle
        self.gripMaxAngle = gripMaxAngle
        self.gripMinAngle = gripMinAngle
        self.rotateClAngle = rotateClAngle
        self.rotateCcAngle = rotateCcAngle
        self.gripDictionary = {-1 : -1}
        self.moveDictionary = {-1 : -1}
        self.populateDictionary(gripMinAngle, 54, gripMaxAngle, gripMaxPosition, self.gripDictionary)
        self.populateDictionary(moveMinAngle, moveMinPosition, moveMaxAngle, moveMaxPosition, self.moveDictionary)
        self.gripCubeAngle = self.gripDictionary[cube.width]
        self.gripReleaseAngle = self.gripDictionary[cube.width + 15]
        self.gripClearanceAngle = self.gripDictionary[cube.width + 25]
        
    def __del__(self):
        self.moveServo.moveFast(self.moveInitAngle)
        del self.moveServo
        self.gripServo.moveFast(self.gripInitAngle)
        del self.gripServo
        self.rotateServo.moveFast(self.rotateInitAngle)
        del self.rotateServo
        
    def updateAngles(self, cube):
        self.gripCubeAngle = self.gripDictionary[cube.width]
        self.gripReleaseAngle = self.gripDictionary[cube.width + 15]
        self.gripClearanceAngle = self.gripDictionary[cube.width + 25]
            
    def populateDictionary(self, minAngle, minPosition, maxAngle, maxPosition, dictionary):
        currentPosition = minPosition
        m = (maxAngle - minAngle) / (maxPosition - minPosition)
        b = 0
        while currentPosition <= maxPosition:
            if maxAngle - minAngle > 0:
                b = minAngle
                x = currentPosition - minPosition
            else:
                b = maxAngle
                x = currentPosition - maxPosition
            dictionary[currentPosition] = round(m * x + b)
            currentPosition = currentPosition + 1
        
    def move(self, angle):
        self.moveServo.moveFast(angle)
        
    def moveSmooth(self, angle, rate):
        self.moveServo.move(angle, rate)
        
    def moveRelative(self, angle, rate):
        if self.moveMaxAngle - self.moveMinAngle > 0:
            direction = -1
        else:
            direction = 1
        angle = (self.moveServo.currentAngle * 1.5) - (angle * direction)
        
        if rate == 0:
            self.moveServo.moveFast(angle)
        else:
            self.moveServo.move(angle, rate)
    
    #angle: 0 is closed all the way, 180 is open all the way
    def grip(self, angle):
        self.gripServo.moveFast(angle)
    
    def gripSmooth(self, angle, rate):
        self.gripServo.move(angle, rate)
        
    def gripRelative(self, angle, rate):
        if self.gripMaxAngle - self.gripMinAngle > 0:
            direction = -1
        else:
            direction = 1
        angle = (self.gripServo.currentAngle * 1.5) - (angle * direction)
        
        if rate == 0:
            self.gripServo.moveFast(angle)
        else:
            self.gripServo.move(angle, rate)        
    
    #position: -1 = 0 degrees, 0 = 90 degrees(center), 1 = 180 degrees 
    def rotate(self, position):
        if position == -1:
            self.rotateServo.moveFast(self.rotateCcAngle)
        if position == 1:
            self.rotateServo.moveFast(self.rotateClAngle)
        if position == 0:
            self.rotateServo.moveFast(self.rotateInitAngle)
            
    def rotateSimple(self, angle):
        self.rotateServo.moveFast(angle)
            
    def giveCube(self, anotherArm):
        self.release()
        self.hasCube = False
        anotherArm.hasCube = True
        
    def test(self):
        self.rotate(0)
        self.release()
        #time.sleep(5)
        self.grip3by3()
        #time.sleep(2)
        
        self.rotate(-1)
        self.move(1, 0.5)
        self.rotate(1)
        self.move(-1, 0.5)
        self.rotate(0)
        self.move(1, 0.5)
        
        self.rotate(-1)
        self.rotate(1)
        self.rotate(-1)
        self.rotate(1)

        self.rotate(-1)
        self.move(-1, 0.5)
        self.rotate(1)
        self.move(1, 0.5)
        self.rotate(0)
        
        #time.sleep(5)
        self.release()
        #time.sleep(1)
        
        
    def gripTest(self):
        self.grip(self.gripMaxAngle)
        time.sleep(1)
        self.grip(self.gripMinAngle)
        time.sleep(1)
        self.grip(self.gripInitAngle)
        time.sleep(1)
    
    def grip3by3Test(self):
        self.rotate(0)
        self.release()
        time.sleep(5)
        self.grip3by3()
        time.sleep(5)
        self.release()
        time.sleep(1)
        
    def rotateTest(self, wait):
        self.rotate(-1)
        time.sleep(wait)
        self.rotate(1)
        time.sleep(wait)
        self.rotate(0)
        time.sleep(wait)
        
    def moveTest(self, wait):
        self.move(self.moveMaxAngle)
        time.sleep(wait)
        self.move(self.moveMinAngle)
        time.sleep(wait)
        self.move(self.moveInitAngle)
        time.sleep(wait)
        
class AllArms:
    'Object with all 3 arms'
    
    def __init__(self, cube):
        self.bot = Bot2.Control()
        #move servo, grip servo, rotate servo, moveMax, moveMin, moveMaxPos, moveMinPos, gripMax, gripMin, gripMaxPos, rotateCl, rotateCc     
        self.leftArm   = Arm(cube, self.bot.servo[5], self.bot.servo[7], self.bot.servo[4], 160,  45, 90, 0,   0, 245, 127, 225, 45)
        self.rightArm  = Arm(cube, self.bot.servo[6], self.bot.servo[8], self.bot.servo[2],  60, 230, 90, 0,   0, 245, 127, 227, 45)
        self.centerArm = Arm(cube, self.bot.servo[1], self.bot.servo[9], self.bot.servo[0], 190,  12, 90, 0, 270,  81, 110, 220, 40)
        
    def __del__(self):
        del self.leftArm
        del self.rightArm
        del self.centerArm
        
    def updateAngles(self, cube):
        self.leftArm.updateAngles(cube)
        self.rightArm.updateAngles(cube)
        self.centerArm.updateAngles(cube)
        
    #move all arms to their staring position, centerArm takes cube
    def startPosition(self):
        self.leftArm.rotate(0)
        self.leftArm.release()
        self.rightArm.rotate(0)
        self.leftArm.release()
        self.centerArm.rotate(0)
        self.centerArm.release()
        
    #move both left and right arms simultaneously (sort of)
    def moveSideArms(self, distance, rate):
        if distance > 0:
            step = 1
        else:
            step = -1
            distance = distance * -1
        for i in range (distance):
            self.leftArm.moveRelative(step, rate)
            self.rightArm.moveRelative(step, rate)        
        
    def sideArmsRelease(self):
        self.bot.move(180, self.bot.servo[1].currentAngle, 180, self.bot.servo[3].currentAngle, self.bot.servo[4].currentAngle, self.bot.servo[5].currentAngle)
    
    def sideArmsRotate(self, angle):
        if (angle == 1):
            left = 170
            right = 2
        if (angle == -1):
            left = 4
            right = 178
        if (angle == 0):
            left = 74
            right = 84
        self.bot.move(self.bot.servo[0].currentAngle, left, self.bot.servo[2].currentAngle, right,self.bot.servo[4].currentAngle, self.bot.servo[5].currentAngle)
        
    #Turn left face backwards 90 degrees
    def leftcc(self):
        self.centerArm.move(1, 0.166)
        self.leftArm.rotate(1)
        self.leftArm.move(1,0.13)
        time.sleep(0.1)
        self.centerArm.move(-1, 0.1662)
        time.sleep(0.1)
        self.sideArmsGrip()
        time.sleep(0.2)
        self.leftArm.rotateSimple(self.leftArm.rotateCenter - 9)
        time.sleep(0.1)
        self.sideArmsRelease()
        self.leftArm.rotate(0)
        time.sleep(0.1)
        
        self.leftArm.move(-1,0.133)
        time.sleep(0.1)
        
    #Turn left face forwards 90 degrees
    def leftcl(self):
        self.centerArm.move(1, 0.166)
        time.sleep(0.1)
        self.leftArm.rotate(-1)
        self.leftArm.move(1,0.11)
        time.sleep(0.1)
        self.centerArm.move(-1, 0.166)
        time.sleep(0.1)
        self.sideArmsGrip()
        time.sleep(0.2)
        self.leftArm.rotateSimple(self.leftArm.rotateCenter + 7)
        time.sleep(0.1)
        self.sideArmsRelease()
        self.leftArm.rotate(0)
        time.sleep(0.1)
        
        self.leftArm.move(-1,0.125)
        time.sleep(0.1)
        
    def rightcl(self):
        self.sideArmsGrip()
        self.centerArm.release()
        time.sleep(0.1)
        self.centerArm.move(-1, 0.16)
        time.sleep(0.1)
        self.centerArm.grip3by3()
        self.sideArmsRelease()
        time.sleep(0.1)
        
        self.leftArm.move(-1, 0.2)
        self.centerArm.move(-1, 0.166)
        time.sleep(0.1)
        self.rightArm.rotate(-1)
        self.rightArm.move(-1, 0.12)
        time.sleep(0.1)
        self.centerArm.move(1, 0.166)
        time.sleep(0.1)
        self.sideArmsGrip()
        time.sleep(0.2)
        self.rightArm.rotateSimple(self.rightArm.rotateCenter + 9)
        time.sleep(0.1)
        self.sideArmsRelease()
        self.rightArm.rotate(0)
        time.sleep(0.1)
        self.rightArm.move(1, 0.15)
        self.leftArm.move(1, 0.196)
        
        self.sideArmsGrip()
        self.centerArm.release()
        time.sleep(0.1)
        self.centerArm.move(1, 0.123)
        time.sleep(0.1)
        self.centerArm.grip3by3()
        self.sideArmsRelease()
        time.sleep(0.1)
        self.centerArm.move(1, 0.045)
        time.sleep(0.1)
        
    def rightcc(self):
        self.sideArmsGrip()
        self.centerArm.release()
        time.sleep(0.1)
        self.centerArm.move(-1, 0.16)
        time.sleep(0.1)
        self.centerArm.grip3by3()
        self.sideArmsRelease()
        time.sleep(0.1)
        
        self.leftArm.move(-1, 0.2)
        self.centerArm.move(-1, 0.166)
        time.sleep(0.1)
        self.rightArm.rotate(1)
        self.rightArm.move(-1, 0.12)
        time.sleep(0.1)
        self.centerArm.move(1, 0.166)
        time.sleep(0.1)
        self.sideArmsGrip()
        time.sleep(0.2)
        self.rightArm.rotateSimple(self.rightArm.rotateCenter - 9)
        time.sleep(0.1)
        self.sideArmsRelease()
        self.rightArm.rotate(0)
        time.sleep(0.1)
        self.rightArm.move(1, 0.122)
        self.leftArm.move(1, 0.199)
        
        self.sideArmsGrip()
        self.centerArm.release()
        time.sleep(0.1)
        self.centerArm.move(1, 0.126)
        time.sleep(0.1)
        self.centerArm.grip3by3()
        self.sideArmsRelease()
        time.sleep(0.1)
        self.centerArm.move(1, 0.0387)
        time.sleep(0.1)
        
    def topcc(self):
        self.sideArmsMove(-1, 0.47)
        time.sleep(0.1)
        self.centerArm.rotate(1)
        time.sleep(0.3)
        self.centerArm.move(1, 0.05)
        self.sideArmsMove(1, 0.23)
        time.sleep(0.1)
        self.sideArmsGrip()
        time.sleep(0.1)
        self.centerArm.release()
        time.sleep(0.1)
        self.sideArmsMove(-1, 0.2)
        time.sleep(0.1)
        self.centerArm.grip3by3()
        time.sleep(0.1)
        self.centerArm.rotateSimple(self.centerArm.rotateCenter - 15)
        time.sleep(0.1)
        self.centerArm.release()
        self.centerArm.rotateSimple(self.centerArm.rotateCenter - 4)
        self.centerArm.move(-1, 0.05)
        self.sideArmsMove(1, 0.192)
        time.sleep(0.1)
        self.centerArm.grip3by3()
        self.sideArmsRelease()
        time.sleep(0.3)
#        self.centerArm.rotate(0)
        
        self.sideArmsMove(1, 0.215)
        
#    def topcl(self):
        
#    def bottomcl(self):
        
#    def bottomcc(self):
        
    def cubecc(self):
        self.sideArmsMove(-1, 0.47)
        time.sleep(0.1)
        self.centerArm.rotate(1)
        time.sleep(0.5)
        self.centerArm.move(1, 0.05)
        time.sleep(0.1)
        self.sideArmsMove(1, 0.65)
        self.sideArmsGrip()
        time.sleep(0.1)
        self.centerArm.release()
        self.sideArmsMove(-1, 0.7)
        self.centerArm.rotate(0)
        self.centerArm.move(-1, 0.048)
        self.sideArmsMove(1, 0.6)
        self.sideArmsRelease()
        time.sleep(0.1)
        self.centerArm.grip3by3()
        
        self.sideArmsMove(-1, 0.12)
        
    
    
