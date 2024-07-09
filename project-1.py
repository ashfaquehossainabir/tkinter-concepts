from tkinter import *

# Widgets = GUI Elements: buttons, textboxes, labels, images
# Windows = serves as a container to hold or contain these widgets

# window = Tk()  # Instantiate an instance of a window
# window.geometry("420x420")
# window.title("Abir Mamur Program")
# icon = PhotoImage(file="logo.png")
# window.iconphoto(True, icon)
# window.config(background="#5cfcff")
#
# window.mainloop()  # Place window on computer screen, listen for events


# ---------------------------------------------------------------------------------------------
# Label = an area widget that holds text and/or an image within a window
# window = Tk()
# photo = PhotoImage(file="logo.png")
#
# label = Label(window,
#               text="Bro, do you even code?",
#               font=('Arial', 40, 'bold'),
#               fg="#00FF00",
#               bg="black",
#               relief=RAISED,  # SUNKEN
#               bd="10",
#               padx="20",
#               pady="20",
#               image=photo,
#               compound="top")
# label.pack()
# --> label.place(x=10, y=10)

# window.mainloop()


# ---------------------------------------------------------------------------------------------
# Button - you click it, then it does stuff

# count = 0
#
#
# def click():
#     global count
#     count += 1
#     print(count)
#
#
# window = Tk()
#
# photo = PhotoImage(file="logo.png")
# button = Button(window,
#                 text="Click Me!",
#                 command=click,
#                 font=("Comic Sans", 30),
#                 fg="#00FF00",
#                 bg="black",
#                 activeforeground="#00FF00",
#                 activebackground="black",
#                 state=ACTIVE,  # DISABLED
#                 image=photo,
#                 compound="left")
# button.pack()
#
# window.mainloop()


# ---------------------------------------------------------------------------------------------
# Entry widget - textbox that accepts a single line of user input


# def submit():
#     username = entry.get()
#     print("Hello " + username)
#     entry.config(state=DISABLED)
#
#
# def delete():
#     entry.delete(0, END)  # Index 0 to END
#
#
# def backspace():
#     entry.delete(len(entry.get()) - 1, END)
#
#
# window = Tk()
#
# entry = Entry(window,
#               font=("Arial", 50),
#               fg="#00FF00",
#               bg="black",
#               # show="*"  # This property is only for password input
#               )
#
# entry.insert(0, "Type your name")
# entry.pack(side=LEFT)
#
# submit_button = Button(window,
#                        text="submit",
#                        command=submit)
# submit_button.pack(side=RIGHT)
#
# delete_button = Button(window,
#                        text="delete",
#                        command=delete)
# delete_button.pack(side=RIGHT)
#
# backspace_button = Button(window,
#                        text="backspace",
#                        command=backspace)
# backspace_button.pack(side=RIGHT)
#
# window.mainloop()


# ---------------------------------------------------------------------------------------------
# Check Button Concepts


# def display():
#     if(x.get() == 1):
#         print("You agree!")
#     else:
#         print("You don't agree :(")
#
#
# window = Tk()
#
# x = IntVar()  # BooleanVar(), StringVar()
#
# checkBtn_photo = PhotoImage(file="logo.png")
#
# check_button = Checkbutton(window,
#                            text="I agree to something.",
#                            variable=x,
#                            onvalue=1,
#                            offvalue=0,
#                            command=display,
#                            font=("Arial", 20),
#                            fg="#00FF00",
#                            bg="black",
#                            activeforeground="#00FF00",
#                            activebackground="black",
#                            padx=25,
#                            pady=10,
#                            image=checkBtn_photo,
#                            compound="left")
#
#
# check_button.pack()
# window.mainloop()
