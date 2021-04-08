from tkinter import *
import ast

root = Tk()

config = {
    "t": 4,
    "l0": 0,
    "l1": 1,
    "l2": 2,
    "l3": 3
}

selected = 0
buttons = []

root.title("Calibration")

entryLabel = Label(root, text="Paste config:")
entryLabel.grid(row=0, column=0)

entryField = Entry(root, width=50)
entryField.grid(row=1, column=0, columnspan=5, padx=10, pady=10)

def loadConfig():
    global config
    config = ast.literal_eval(entryField.get())
    global selected
    selected = 0
    updateButtons()
    entryField.delete(0, END)

loadButton = Button(root, text="Load Config", command=loadConfig)
loadButton.grid(row=4, column=0)

def printConfig():
    print(config)
    root.clipboard_clear()
    root.clipboard_append(config)


configButton = Button(root, text="Print Config", command=printConfig)
configButton.grid(row=5, column=0)

def updateButtons():
    global selected
    global buttons
    for button in buttons:
        button.destroy()
    for i in range(config["t"]):
        addButton(i, selected == i)

def addButton(num, isSelected):
    global buttons
    if isSelected:
        color = "blue"
    else:
        color = "gray"
    newButton = Button(root, text=str(num), highlightbackground=color, command=lambda: buttonClicked(num))
    newButton.grid(row=7, column=num)
    buttons.append(newButton)

def buttonClicked(num):
    global selected
    selected = num
    print(num)
    updateButtons()

def clockwise():
    config["l" + str(selected)] += 1
    moveServo(selected, config["l" + str(selected)])

def counterclockwise():
    config["l" + str(selected)] -= 1
    moveServo(selected, config["l" + str(selected)])

def moveServo(num, toLocation):
    pass

clockwiseButton = Button(root, text="↻", command=clockwise)
clockwiseButton.grid(row=8, column=1)

counterclockwiseButton = Button(root, text="↺", command=counterclockwise)
counterclockwiseButton.grid(row=8, column=3)

root.mainloop()
