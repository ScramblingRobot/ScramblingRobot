from CuBot2 import CuBot
import time

cuBot = CuBot()
cuBot.updateCube(60, 4)
#7x7: 69mm
#5x5, 4x4: 60mm
#3x3: 54mm

def testAcceptCube():
    cuBot.acceptCube()
    
def testPresentCube():
    cuBot.presentCube()

def testCheckHeight():
    cuBot.checkHeight()

def testL(numLayers, direction):
    cuBot.L(numLayers, direction)
    
def testR(numLayers, direction):
    cuBot.R(numLayers, direction)

def testD(numLayers, direction):
    cuBot.D(numLayers, direction)

def testY(numlayers, direction):
    cuBot.Y(direction)
    
def testGrip(arm, position, waitTime):
    if position == "max":
        arm.grip(arm.gripMaxAngle)
    elif position == "min":
        arm.grip(arm.gripMinAngle)
    else:
        arm.grip(arm.gripDictionary[position])
    time.sleep(waitTime)

def testMove(arm, position, waitTime):
    if position == "max":
        arm.moveSmooth(arm.moveMaxAngle, 0.01)
    elif position == "min":
        arm.moveSmooth(arm.moveMinAngle, 0.01)
    else:
        arm.moveSmooth(arm.moveDictionary[position], 0.01)
    time.sleep(waitTime)
    
def unitTestAcceptCube(moveNumber):
    if moveNumber == 1:
        cubeWidth = 54
        targetPosition = 90
        
        cuBot.centerArm.grip(cuBot.centerArm.gripDictionary[cubeWidth])
        time.sleep(1)
        cuBot.centerArm.rotate(-1)
        time.sleep(1)
        testMove(cuBot.centerArm, targetPosition - round(cubeWidth / 2), 2)
        time.sleep(2)
        cuBot.centerArm.grip(cuBot.centerArm.gripDictionary[cubeWidth + 15])
        time.sleep(2)
        cuBot.centerArm.grip(cuBot.centerArm.gripDictionary[cubeWidth])
        time.sleep(1)
        cuBot.centerArm.rotate(0)
        time.sleep(1)
        cuBot.centerArm.grip(cuBot.centerArm.gripInitAngle)
    
    elif moveNumber == 2:
        cubeWidth = 54
        c = 25

        testMove(cuBot.centerArm, 15, 1)
        testMove(cuBot.rightArm, 93 - round(cubeWidth / 2) + c, 2)
        testMove(cuBot.rightArm, 46, 1)
        testMove(cuBot.centerArm, 31, 1)
        
######### Begin Testing ##########
testAcceptCube()
#time.sleep(10)
#testCheckHeight()
testL(1, 1)
#testL(2, 1)
testL(1, -1)
#testL(2, -1)
testCheckHeight()
testR(1, 1)
#testR(2, 1)
testR(1, -1)
#testR(2, -1)
testCheckHeight()
#testD(1, 1)
#testY(1, 1)
testPresentCube()

#testGrip(cuBot.centerArm, 54, 3)
#testMove(cuBot.rightArm, 46, 1)
#unitTestAcceptCube(1)
#unitTestAcceptCube(2)

############## Finished ###############
# gripDictionary calibration for all 3 arms
# moveDictionary calibration for center and right arm
# primary operating-functions acceptCube() and presentCube() calibration to support variability in cube width and order

del cuBot
