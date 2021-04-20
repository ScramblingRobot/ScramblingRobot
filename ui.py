import tkinter as tk
from tkinter import filedialog
import os

root = tk.Tk()

root.title("CuBot")

scramble_file = None
file_name = tk.StringVar()
file_name.set("No File Selected")
lines = []


def get_scramble_file():
    global scramble_file
    scramble_file = filedialog.askopenfile()
    global lines
    lines = scramble_file.readlines()
    global file_name
    file_name.set(os.path.basename(scramble_file.name))


file_name_label = tk.Label(root, textvariable=file_name)
file_name_label.pack()

open_round = tk.Button(
    root, text="Choose Current Round File", command=get_scramble_file
)
open_round.pack()


def send(scramble):
    print(len(scramble.split(" ")))
    print(transformToRobot(scramble))


def send_1():
    if scramble_file is not None:
        send(lines[0])


def send_2():
    if scramble_file is not None:
        send(lines[1])


def send_3():
    if scramble_file is not None:
        send(lines[2])


def send_4():
    if scramble_file is not None:
        send(lines[3])


def send_5():
    if scramble_file is not None:
        send(lines[4])


def send_e1():
    if scramble_file is not None:
        send(lines[5])


def send_e2():
    if scramble_file is not None:
        send(lines[6])


tk.Button(root, text="1", command=send_1).pack()
tk.Button(root, text="2", command=send_2).pack()
tk.Button(root, text="3", command=send_3).pack()
tk.Button(root, text="4", command=send_4).pack()
tk.Button(root, text="5", command=send_5).pack()
tk.Button(root, text="e1", command=send_e1).pack()
tk.Button(root, text="e2", command=send_e2).pack()


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


root.mainloop()
