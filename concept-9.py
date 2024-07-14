from tkinter import *
from tkinter import messagebox


def click():
    # messagebox.showinfo(title="Info message",
    #                     message="You are a batman")

    # messagebox.showwarning(title="Warning message",
    #                        message="You are a snake")

    # messagebox.showerror(title="Error!",
    #                      message="You are not a person")

    # if messagebox.askokcancel(title="Ask OK Cancel", message="Do you wanna marry a girl?"):
    #     print("Congratulations!")
    # else:
    #     print("Better luck next time :(")

    # if messagebox.askretrycancel(title="Ask Retry Cancel", message="Do you wanna retry marry a girl?"):
    #     print("Congratulations!")
    # else:
    #     print("Better luck next time :(")

    # if messagebox.askyesno(title="Ask yes or no", message="Do you want to go to a relationship?"):
    #     print("Welcome to hell!")
    # else:
    #     print("Congratulations!")

    # answer = messagebox.askquestion(title="Asking a question", message="Do you like a girl?")
    #
    # if answer == "yes":
    #     print("Omago Turu Love!")
    # else:
    #     print("Feeling sad for you :(")

    answer = messagebox.askyesnocancel(title="Ask yes no cancel", message="Do you like to code?", icon="info")

    if answer == True:
        print("You like to code :O")
    elif answer == False:
        print("You don't like to code :(")
    else:
        print("You canceled")


window = Tk()

button = Button(window,
                command=click,
                text="Click me!")
button.pack()

window.mainloop()

# Continue from 1:31:10
