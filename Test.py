from CuBot2 import CuBot

cuBot = CuBot()

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
    

######### Begin Testing ##########
#testAcceptCube()
#testPresentCube()
#testCheckHeight()
#testL(2, -1)
#testR(1, 1)
#testD(1, 1)
#testY(1, 1)
del cuBot
