from Global import *
from Sequence import *

def transformToRobot(scramble):
    moves = scramble.split(" ")
    size = 0
    if len(moves) < 15:
        size = 2
    elif len(moves) < 30:
        size = 3
    elif len(moves) < 59:
        size = 4
    elif len(moves) < 79:
        size = 5
    elif len(moves) < 99:
        size = 6
    else:
        size = 7
    newScramble = ""
    length = len(moves)
    i = 0
    while i < length:
        if "F" in moves[i][0] or "B" in moves[i][0]:
            j = length
            # Shift all the moves over to add the rotation in
            moves.append(moves[j-1])
            while (j > i):
                moves[j] = moves[j-1]
                j -= 1

            # Add the rotation
            moves[i] = "y"
            length += 1
            shiftclockwise(moves, i)
        elif "U" in moves[i][0]:
            if moves[i] == "U":
                moves[i] = str(size - 2) + "Dw"
                shiftcounterclockwise(moves, i)
            elif moves[i] == "U'":
                moves[i] = str(size - 2) + "Dw'"
                shiftclockwise(moves, i)
            elif moves[i] == "U2":
                moves[i] = str(size - 2) + "Dw2"
                shift180(moves, i)
            elif moves[i] == "Uw":
                moves[i] = str(size - 3) + "Dw"
                shiftcounterclockwise(moves, i)
            elif moves[i] == "Uw'":
                moves[i] = str(size - 3) + "Dw'"
                shiftclockwise(moves, i)
            elif moves[i] == "Uw2":
                moves[i] = str(size - 3) + "Dw2"
                shift180(moves, i)
            elif moves[i] == "2Uw":
                moves[i] = str(size - 4) + "Dw"
                shiftcounterclockwise(moves, i)
            elif moves[i] == "2Uw'":
                moves[i] = str(size - 4) + "Dw'"
                shiftclockwise(moves, i)
            elif moves[i] == "2Uw2":
                moves[i] = str(size - 4) + "Dw2"
                shift180(moves, i)

        newScramble = newScramble + moves[i] + " "
        i += 1
    return newScramble


def shiftclockwise(moves, i):
    k = i
    while (k < len(moves)):
        if 'R' in moves[k][0]:
            moves[k] = moves[k].replace('R', 'F')
        elif 'B' in moves[k][0]:
            moves[k] = moves[k].replace('B', 'R')
        elif 'L' in moves[k][0]:
            moves[k] = moves[k].replace('L', 'B')
        elif 'F' in moves[k][0]:
            moves[k] = moves[k].replace('F', 'L')
        k += 1


def shiftcounterclockwise(moves, i):
    k = i
    while (k < len(moves)):
        if 'R' in moves[k][0]:
            moves[k] = moves[k].replace('R', 'B')
        elif 'B' in moves[k][0]:
            moves[k] = moves[k].replace('B', 'L')
        elif 'L' in moves[k][0]:
            moves[k] = moves[k].replace('L', 'F')
        elif 'F' in moves[k][0]:
            moves[k] = moves[k].replace('F', 'R')
        k += 1


def shift180(moves, i):
    k = i
    while (k < len(moves)):
        if 'R' in moves[k][0]:
            moves[k] = moves[k].replace('R', 'L')
        elif 'B' in moves[k][0]:
            moves[k] = moves[k].replace('B', 'F')
        elif 'L' in moves[k][0]:
            moves[k] = moves[k].replace('L', 'R')
        elif 'F' in moves[k][0]:
            moves[k] = moves[k].replace('F', 'B')
        k += 1

# -----------------------------------------------------------
print("U2 R' F U' F' R2 F' U'")
input = transformToRobot("U2 R' F U' F' R2 F' U'")  # -> 0Dw2 L' y R 0Dw' y L' y L2 y R' 0Dw'  
print(input+'\n')

perform(input)

# Andrew after taking scamble input your function transformToRobot would return the pre processed input

# Dont forget The includes (Can be seen on lines 1 - 2)
# Take that preprocessed input and pass it my preform function. (Function can be found in Sequence.py)

# In the preform function all that should be needed to be done is just pluging in Stevens operations in correpsonding ifs

# In Global I have 

# Andrew Collects Input -> Process it so that moves are always in direction of arm -> Plug into Joshs Preform Function -> Within the Preform Function Stevens in depth robot operations take place
