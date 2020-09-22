# This code is a library of support functions for the CuBot scrambling robot

class CuBotLib(object):
#define variables

  def debug():
  #debug issues

  def reset():
  #set the robot to a starting position

  def move(self, position):
  #move the arm over to the position

  def rotate(self, degree):
  #rotate the arm the specified degrees

  def clamp(self, size):
  #set the arm's clamp to the given size

  def release(self):
  #set the arm's clamp to open

  def orient(self, face):
  #perform a clamp, rotation, and release to show the desired face

  def execute(self, cmd):
  #execute a movement command

  def read(self):
  #reads the current cube's face with the camera

  def readcube(self):
  #reads all of the cube's faces with the camera
