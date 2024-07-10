from tkinter import *


# Entry widget - textbox that accepts a single line of user input


def submit():
    username = entry.get()
    print("Hello " + username)
    entry.config(state=DISABLED)


def delete():
    entry.delete(0, END)  # Index 0 to END


def backspace():
    entry.delete(len(entry.get()) - 1, END)


window = Tk()

entry = Entry(window,
              font=("Arial", 50),
              fg="#00FF00",
              bg="black",
              # show="*"  # This property is only for password input
              )

entry.insert(0, "Type your name")
entry.pack(side=LEFT)

submit_button = Button(window,
                       text="submit",
                       command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window,
                       text="delete",
                       command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window,
                       text="backspace",
                       command=backspace)
backspace_button.pack(side=RIGHT)

window.mainloop()
