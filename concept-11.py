from tkinter import *

# Text widget concept = functions like a text area, you can enter multiple lines of text.


def submit():
    inputText = text.get("1.0", END)
    print(inputText)


window = Tk()
text = Text(window,
            bg="lightyellow",
            font=("Ink Free", 25),
            height=8,
            width=20,
            padx=20,
            pady=20,
            fg="darkblue")
text.pack()
button = Button(window,
                text="submit",
                command=submit)
button.pack()

window.mainloop()

# Continue from 1:42:50
