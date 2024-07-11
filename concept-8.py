from tkinter import *

# List Box Concept


def submit():
    food = []

    for index in listbox.curselection():
        food.insert(index, listbox.get(index))

    for index in food:
        print("You have ordered: " + index)

    # print("You have ordered: " + listbox.get(listbox.curselection()))


def add():
    listbox.insert(listbox.size(), entryBox.get())
    listbox.config(height=listbox.size())


def delete():
    # listbox.delete(listbox.curselection())

    for index in reversed(listbox.curselection()):
        listbox.delete(index)

    listbox.config(height=listbox.size())


window = Tk()
listbox = Listbox(window,
                  bg="#f7ffde",
                  font=("Constantia", 35),
                  width=15,
                  selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1, "Pizza")
listbox.insert(2, "Burger")
listbox.insert(3, "Meatbox")
listbox.insert(4, "Sausage")
listbox.insert(5, "Kacchi Biriyani")

listbox.config(height=listbox.size())

entryBox = Entry(window)
entryBox.pack()

addButton = Button(window,
                      text="add",
                      command=add)
addButton.pack()

deleteButton = Button(window,
                      text="delete",
                      command=delete)
deleteButton.pack()

submitButton = Button(window,
                      text="submit",
                      command=submit)
submitButton.pack()

window.mainloop()
