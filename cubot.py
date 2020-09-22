# the main file to run for operating the CuBot robot

#initialize any variables associated with the robot
showDebugInfo = false

CuBot = cubot_lib.CuBotLib(showDebugInfo)

try:
  #receive scramble input and initialize camera

except Exception, e:
    print("Error: " + str(e))

CuBot.reset()