from Global import *
from Instruction import *

# [Temporary] will be from file
input = "U2 R' F U' F' R2 F' U'" #"Bw2 F Uw' D2 Rw' F2 Uw2 Fw F Bw2 Lw2"

Instructions = []   # Keeps track of all instructions needed
Faces = [Dir.South, Dir.West, Dir.North, Dir.East, Dir.Above, Dir.Below] # where each cube face is pointing, the index are: Front, Left, Back, Right, Up, Down

# [Temporary] used to output instructions
def printFaces():
    print("[Front = {}, Left = {}, Back = {}, Right = {}, Up = {}, Down = {}]".format( d[Faces[0]], d[Faces[1]],d[Faces[2]],d[Faces[3]],d[Faces[4]],d[Faces[5]] ))

# Flip cube 180 degrees using west arm, Cord is on y Axis
def FlipCube(CurFace,Cord):  
    # Arms[Dir.West].Rotate(180)
    Faces[Face.Up], Faces[Face.Down] = Faces[Face.Down], Faces[Face.Up]
    # Arms[Dir.West].Move(Cord)
    printFaces()

# Rotate Cube Faces 90 degrees (one rotation) using bottom arm, Shift the Faces array, Move Arm to be changed cord units, cord is on x axis
def ShiftCube(CurFace,Cord):    
    # Arms[Dir.Below].Rotate() # Shift cube faces 90 degrees
    Faces[Face.Front], Faces[Face.Left], Faces[Face.Back], Faces[Face.Right] = Faces[Face.Right], Faces[Face.Front], Faces[Face.Left], Faces[Face.Back]
    #Arms[ Faces[CurFace] ].Move(Cord)
    printFaces()

for instruction in input.split():   # Could possible move into main loop
    Instructions.append( translate(instruction) )

for instruction in Instructions:
    printFaces()

    if ( (instruction.Face == Face.Up  or instruction.Face == Face.Down) and Faces[instruction.Face] != Dir.Below ): # Check if Face to rotate is Up/Down and pointing towards Below Arm
        print("Flip Cube!") #Function to flip cube upside down so face is in below arm
        FlipCube(instruction.Face, instruction.Cord)
    elif ( ( Faces[instruction.Face] != Dir.West ) and ( Faces[instruction.Face] != Dir.East ) ): # Check if Face to rotate is pointing towards West/East Arm
       print("We need to rotate!") # Function to rotate the cube 90 degrees once so face is in west or east arm, and shift face array, should also position arm according to cord
       ShiftCube(instruction.Face, instruction.Cord)
    
    print("Face to Rotate:",f[instruction.Face])
    print("Direction of Face:",d[Faces[instruction.Face]])

    print( Arms[ Faces[instruction.Face] ], "\n" ) #.Rotate(instruction.Degree) 
