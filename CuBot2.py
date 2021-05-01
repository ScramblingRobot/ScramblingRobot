#Author: Anh (Steven) Nguyen
#Created: 09/12/2020
#Last modified: 04/29/2021 by Anh (Steven) Nguyen
import Cube
import Arms2
import time

#initialize cube object with cube's width and number of layers
cube = Cube.Cube(68, 7)

#initialize arms object with all 3 arms (9 servos)
arms = Arms2.AllArms(cube)

leftArm = arms.leftArm
rightArm = arms.rightArm
centerArm = arms.centerArm

#setting the cube to solved state and printing it
cube.solvedState()
cube.printCube()

#prints the entire grip dictionary for each arm
#print(leftArm.gripDictionary)
#print(rightArm.gripDictionary)
#print(centerArm.gripDictionary)

# SO (Starting Operation) - takes cube from the user and manipulate it to the correct operating position
## Orientation: cube will rotate 90 degrees wrt the Y axis
def acceptCube():
    centerArm.rotate(-1)
    time.sleep(0.5)
    centerArm.grip(centerArm.gripCubeAngle)
    time.sleep(0.5)
    centerArm.moveRelative(40, 0)
    rightArm.moveRelative(90, 0)
    time.sleep(0.5)
    rightArm.grip(rightArm.gripCubeAngle)
    time.sleep(0.5)
    centerArm.grip(centerArm.gripInitAngle)
    time.sleep(0.5)
    rightArm.moveSmooth(rightArm.moveMinAngle, 0.01)
    centerArm.grip(centerArm.gripMaxAngle)
    time.sleep(0.5)
    centerArm.rotate(0)
    leftArm.grip(leftArm.gripMaxAngle)
    time.sleep(0.1)
    centerArm.moveRelative(-10, 0)
    rightArm.moveSmooth(rightArm.moveInitAngle, 0.01)
    time.sleep(0.5)
    centerArm.grip(centerArm.gripCubeAngle)
    time.sleep(0.5)
    rightArm.grip(rightArm.gripInitAngle)
    time.sleep(0.5)
    centerArm.moveSmooth(centerArm.moveInitAngle, 0.02)
    time.sleep(0.5)
    leftArm.grip(leftArm.gripCubeAngle)
    rightArm.grip(rightArm.gripCubeAngle)
    time.sleep(0.5)

# CO (Consistency Operation) - brings the cube to the correct operating height
## Orientation: no change
def checkHeight():
    leftArm.grip(leftArm.gripMaxAngle)
    rightArm.grip(rightArm.gripMaxAngle)
    time.sleep(0.5)
    centerArm.moveRelative(-20, 0.01)
    rightArm.rotate(1)
    time.sleep(0.5)
    centerArm.moveRelative(50, 0.01)
    time.sleep(0.1)
    rightArm.grip(rightArm.gripCubeAngle)
    time.sleep(0.5)
    rightArm.grip(rightArm.gripMaxAngle)
    centerArm.moveRelative(-50, 0.01)
    rightArm.rotate(0)
    time.sleep(0.5)
    centerArm.moveRelative(20, 0.01)
    time.sleep(0.1)
    leftArm.grip(leftArm.gripCubeAngle)
    rightArm.grip(rightArm.gripCubeAngle)
    time.sleep(1)
    
# EO (Ending Operation) - brings cube back to the starting starting position
## Orientation: cube will rotate -90 degrees wrt the Y axis
def presentCube():
    leftArm.grip(leftArm.gripMaxAngle)
    rightArm.grip(rightArm.gripMaxAngle)
    time.sleep(0.5)
    rightArm.move(rightArm.moveMinAngle)
    centerArm.move(centerArm.moveInitAngle)
    time.sleep(0.5)
    centerArm.moveRelative(40, 0.02)
    centerArm.rotate(-1)
    time.sleep(0.5)
    rightArm.move(rightArm.moveInitAngle)
    time.sleep(0.5)
    rightArm.grip(rightArm.gripCubeAngle)
    time.sleep(1.5)
    centerArm.grip(centerArm.gripInitAngle)
    time.sleep(0.5)
    rightArm.moveRelative(90, 0.02)
    time.sleep(0.5)
    centerArm.grip(centerArm.gripCubeAngle)
    time.sleep(0.5)
    rightArm.grip(rightArm.gripInitAngle)
    time.sleep(0.5)
    rightArm.move(rightArm.moveInitAngle)
    centerArm.move(centerArm.moveInitAngle)
    time.sleep(0.5)
    centerArm.rotate(0)
    time.sleep(0.5)
    centerArm.grip(centerArm.gripMaxAngle)

# PO (Primary Operation) - rotate left layer 90 degrees (1) or -90 degrees (-1)
## Orientation: no change
def L(self, numLayers, direction):
    leftArm.grip(leftArm.gripMaxAngle)
    rightArm.grip(rightArm.gripMaxAngle)
    time.sleep(0.5)
    centerArm.moveRelative(23, 0.02)
    leftArm.moveRelative(20, 0.02)
    time.sleep(0.11)
    rightArm.grip(rightArm.gripCubeAngle)
    time.sleep(1.5)
    leftArm.grip(leftArm.gripCubeAngle)
    time.sleep(0.5)
    leftArm.rotate(direction)
    time.sleep(0.5)
    leftArm.grip(leftArm.gripMaxAngle)
    rightArm.grip(rightArm.gripMaxAngle)
    time.sleep(0.5)
    centerArm.moveRelative(40, 0.02)
    time.sleep(0.1)
    leftArm.rotate(0)
    leftArm.move(leftArm.moveInitAngle)
    centerArm.moveSmooth(centerArm.moveInitAngle, 0.02)
    time.sleep(0.1)
    leftArm.grip(leftArm.gripCubeAngle)
    rightArm.grip(rightArm.gripCubeAngle)
    time.sleep(1)
    
# PO (Primary Operation) - rotate right layer 90 degrees (1) or -90 degrees (-1)
## Orientation: no change
def R(self, numLayers, direction):
    rightArm.grip(rightArm.gripMaxAngle)
    leftArm.grip(leftArm.gripMaxAngle)    
    time.sleep(0.5)
    centerArm.moveRelative(-20, 0.02)
    rightArm.moveRelative(20, 0.02)
    time.sleep(0.11)
    leftArm.grip(leftArm.gripCubeAngle)
    time.sleep(0.5)
    rightArm.grip(rightArm.gripCubeAngle)
    time.sleep(1.5)
    rightArm.rotate(direction)
    time.sleep(0.5)
    rightArm.gripRelative(80, 0)
    leftArm.grip(leftArm.gripMaxAngle)
    time.sleep(0.5)
    centerArm.moveRelative(-40, 0.02)
    time.sleep(0.1)
    rightArm.rotate(0)
    rightArm.move(rightArm.moveInitAngle)
    centerArm.moveSmooth(centerArm.moveInitAngle, 0.02)
    time.sleep(0.1)
    leftArm.grip(leftArm.gripCubeAngle)
    rightArm.grip(rightArm.gripCubeAngle)
    time.sleep(1)

# PO (Primary Operation) - rotate cube 90 degrees (1) or -90 degrees (-1)
## Orientation: cube will rotate 90 degrees (1) or -90 degrees (-1) wrt the Y axis
def Y(self, direction):
    centerArm.grip(centerArm.gripMaxAngle)
    time.sleep(0.5)
    arms.moveSideArms(-50, 0.01)
    centerArm.rotate(-direction)
    time.sleep(0.5)
    arms.moveSideArms(50, 0.01)
    centerArm.grip(centerArm.gripCubeAngle)
    time.sleep(1)
    rightArm.grip(rightArm.gripMaxAngle)
    leftArm.grip(leftArm.gripMaxAngle)
    time.sleep(0.5)
    arms.moveSideArms(-50, 0)
    centerArm.rotate(0)
    centerArm.moveRelative(15 * -direction, 0)
    time.sleep(0.5)
    arms.moveSideArms(50, 0)
    rightArm.grip(rightArm.gripCubeAngle)
    leftArm.grip(leftArm.gripCubeAngle)
    time.sleep(1)
    centerArm.grip(centerArm.gripMaxAngle)
    time.sleep(0.5)
    centerArm.moveRelative(30 * direction, 0)
    time.sleep(0.5)
    centerArm.move(centerArm.moveInitAngle)
    time.sleep(0.5)
    centerArm.grip(centerArm.gripCubeAngle)
    time.sleep(1)
    
# PO (Primary Operation) - rotate Down layer 90 degrees (1) or -90 degrees (-1)
## Orientation: no change
def D(self, numLayers, direction):
    centerArm.grip(centerArm.gripMaxAngle)
    time.sleep(0.5)
    arms.moveSideArms(-25, 0.01)
    centerArm.grip(centerArm.gripCubeAngle)
    time.sleep(1)
    centerArm.rotate(direction)
    time.sleep(1)
    centerArm.grip(centerArm.gripMaxAngle)
    arms.moveSideArms(-20, 0.01)
    centerArm.rotate(0)
    time.sleep(0.5)
    arms.moveSideArms(45, 0.01)
    
    centerArm.grip(centerArm.gripCubeAngle)
    time.sleep(1)
    
# # PO (Primary Operation) - rotate Up layer 90 degrees (1) or -90 degrees (-1)
# ## Orientation: cube will rotate -90 degrees (1) or 90 degrees (-1) wrt the Y axis
# def U(layers, direction):
#     #yet to be implemented
#     time.sleep(1)

############## Begin Testing ##############
#centerArm.move(centerArm.moveMaxAngle)
#time.sleep(1)
#leftArm.gripTest()
#leftArm.grip3by3Test()
#leftArm.rotateTest(1)
#leftArm.moveTest(1)
#leftArm.test()
#centerArm.move(centerArm.moveInitAngle)

#centerArm.move(centerArm.moveMinAngle)
#time.sleep(1)
#rightArm.gripTest()
#rightArm.grip3by3Test()
#rightArm.rotateTest(1)
#rightArm.moveTest(1)
#rightArm.test()
#centerArm.move(centerArm.moveInitAngle)

#time.sleep(1)
#centerArm.rotate(1)
#time.sleep(2)
#centerArm.gripTest()
#centerArm.grip3by3Test()
#centerArm.rotateTest(1)
#centerArm.moveTest(1)
#centerArm.test()
    
#acceptCube()
#L(1)
#R(1)
#Y(1)
#L(1)
#R(1)
#Y(1)
#Y(1)
#L(-1)
#R(-1)
#Y(1)
#L(-1)
#R(-1)

#L(1)
#B(1)
#R(1)

#checkHeight()

#presentCube()
    
#leftArm.grip(leftArm.gripMinAngle)
#time.sleep(5)
#leftArm.grip(leftArm.gripMaxAngle)
#time.sleep(5)
    
#rightArm.grip(rightArm.gripCubeAngle)
#time.sleep(5)
#rightArm.grip(rightArm.gripInitAngle)
#print(rightArm.gripCubeAngle)


############# Begin Execution ##############


########### Garbage Collection #############
del leftArm
del rightArm
del centerArm
del arms
del cube