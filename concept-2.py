from tkinter import *


# Label = an area widget that holds text and/or an image within a window
window = Tk()
photo = PhotoImage(file="logo.png")

label = Label(window,
              text="Bro, do you even code?",
              font=('Arial', 40, 'bold'),
              fg="#00FF00",
              bg="black",
              relief=RAISED,  # SUNKEN
              bd="10",
              padx="20",
              pady="20",
              image=photo,
              compound="top")
label.pack()
# --> label.place(x=10, y=10)

window.mainloop()
