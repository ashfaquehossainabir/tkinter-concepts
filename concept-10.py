from tkinter import *
from tkinter import colorchooser

# Changing window background color concept


def click():
    color = colorchooser.askcolor()
    window.config(bg=color[1])  # ColorHex = color[1]


window = Tk()
window.geometry("420x420")

button = Button(text="Click me!", command=click)
button.pack()

window.mainloop()
