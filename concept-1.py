from tkinter import *

# Widgets = GUI Elements: buttons, textboxes, labels, images
# Windows = serves as a container to hold or contain these widgets

window = Tk()  # Instantiate an instance of a window
window.geometry("420x420")
window.title("Abir Mamur Program")
icon = PhotoImage(file="logo.png")
window.iconphoto(True, icon)
window.config(background="#5cfcff")

window.mainloop()  # Place window on computer screen, listen for events
