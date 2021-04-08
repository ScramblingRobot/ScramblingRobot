from Global import *
from Sequence import *

# [Temporary] will be from file
input = "U2 R' F U' F' R2 F' U'" #"Bw2 F Uw' D2 Rw' F2 Uw2 Fw F Bw2 Lw2"

ScrambleSequences = []   # Keeps track of all instructions needed
Faces = [Dir.South, Dir.West, Dir.North, Dir.East, Dir.Above, Dir.Below] # where each cube face is pointing, the index are: Front, Left, Back, Right, Up, Down
Current = {Dir.West: 0, Dir.East: 0, Dir.Below: 0}  # 0 -1 2 1 0

# [Temporary] used to output instructions
def printFaces():
    print("[Front = {}, Left = {}, Back = {}, Right = {}, Up = {}, Down = {}]".format( d[Faces[0]], d[Faces[1]],d[Faces[2]],d[Faces[3]],d[Faces[4]],d[Faces[5]] ))

# Shift the Faces array
def ShiftCube(degree): 
    if degree == 180:
        Faces[Face.Front], Faces[Face.Left], Faces[Face.Back], Faces[Face.Right] = Faces[Face.Back], Faces[Face.Right], Faces[Face.Front], Faces[Face.Left]
    elif degree == 90:
        Faces[Face.Front], Faces[Face.Left], Faces[Face.Back], Faces[Face.Right] = Faces[Face.Right], Faces[Face.Front], Faces[Face.Left], Faces[Face.Back]
    else:
        Faces[Face.Front], Faces[Face.Left], Faces[Face.Back], Faces[Face.Right] = Faces[Face.Left], Faces[Face.Back], Faces[Face.Right], Faces[Face.Front]

for sequence in input.split():   # Could possible move into main loop
    ScrambleSequences.append( translate(sequence) )

for sequence in ScrambleSequences:
    if sequence.Face == Face.Up:    #Bottom Arm will always be facing bottom face
        sideOffset = (Boundary - sequence.Width) * GridUnit
        print(f"Left Arm: Open -> Move  +{sideOffset} -> Close")
        print(f"Right Arm: Open -> Move +{sideOffset} -> Close\n")
        
        lowerOffset = Dimension - 1 - ( sequence.Width + 1 )    # -1 is to account that the bottom arm is holding cube at edge (Change formula later but logic is consitent), +1 becuase width starts at 0
        print("Bottom Arm: Open")
        print(f"Left Arm: Move -{lowerOffset}")
        print(f"Right Arm: Move -{lowerOffset}")
        print(f"Bottom Arm: Close -> Rotate -{sequence.Degree} degrees\n")
        ShiftCube(sequence.Degree)

        print("Bottom  Arm: Open")
        print(f"Left Arm: Move +{lowerOffset}")
        print(f"Right Arm: Move +{lowerOffset}")
        print("Bottom Arm: Close\n")

        print(f"Left Arm: Open -> Move  -{sideOffset} -> Close")
        print(f"Right Arm: Open -> Move -{sideOffset} -> Close\n")
    elif sequence.Face == Face.Down:
        sideOffset = sequence.Width - Boundary + 1
        print(f"Left Arm: Open -> Move  {sideOffset} -> Close")
        print(f"Right Arm: Open -> Move {sideOffset} -> Close\n")

        lowerOffset = -lowerOffset - (Boundary -1)
        print("Bottom Arm: Open")
        print(f"Left Arm: Move {lowerOffset}")
        print(f"Right Arm: Move {lowerOffset}")
        print("Bottom Arm: Close\n")

        print(f"Bottom Arm: Rotate {sequence.Degree} degrees")
        if sequence.Degree != 180:
            print("Bottom Arm: Open -> Rotate {sequence.Degree} degrees -> Close")
        print("\n")

        print("Bottom Arm: Open")
        print(f"Left Arm: Move +{lowerOffset}")
        print(f"Right Arm: Move +{lowerOffset}")
        print("Bottom Arm: Close\n")

        print(f"Left Arm: Open -> Move  +{sideOffset} -> Close")
        print(f"Right Arm: Open -> Move +{sideOffset} -> Close\n")
    else:
        if (Faces[sequence.Face] != Dir.West) and (Faces[sequence.Face] != Dir.East):  # The face to be turned is not in position of an arm
            print("Left Arm: Open")
            print("Right Arm: Open")
            print("Bottom Arm: Rotate 90 degrees")
            ShiftCube(90)
            print("Left Arm: Close")
            print("Right Arm: Close")
            print("Bottom Arm: Open -> Rotate 90 degrees -> Close")
        
        bottomOffSet = sequence.Width - Current[Faces[sequence.Face]]   # Put an if to hande if its West or East arm -> for now named Side arm
        print("Left Arm: Open")
        print("Right Arm: Open")
        print("Bottom Arm: Move {bottomOffset}")
        print("Left Arm: Close")
        print("Right Arm: Close\n")

        print("Side arm: Rotate {sequence.Degree} degrees")
        if sequence.Degree != 180:
            print("Side Arm: Open -> Rotate {sequence.Degree} degrees -> Close")

        print("Left Arm: Open")
        print("Right Arm: Open")
        print("Bottom Arm: Move -{bottomOffset}")
        print("Left Arm: Close")
        print("Right Arm: Close\n")
