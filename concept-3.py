from tkinter import *


# Button - you click it, then it does stuff

count = 0


def click():
    global count
    count += 1
    print(count)


window = Tk()

photo = PhotoImage(file="logo.png")
button = Button(window,
                text="Click Me!",
                command=click,
                font=("Comic Sans", 30),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                state=ACTIVE,  # DISABLED
                image=photo,
                compound="left")
button.pack()

window.mainloop()
