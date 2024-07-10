from tkinter import *


# Radio Buttons - similar to checkbox, but you can only select one from a group

food = ["pizza", "hamburger", "hotdog"]


def order():
    if(x.get() == 0):
        print("You ordered pizza!")
    elif(x.get()==1):
        print("You ordered hamburger!")
    elif(x.get()==2):
        print("You ordered hotdog!")
    else:
        print("huh?")


window = Tk()

pizzaImage = PhotoImage(file="logo.png")
hamburgerImage = PhotoImage(file="logo.png")
hotdogImage = PhotoImage(file="logo.png")

foodImages = [pizzaImage, hamburgerImage, hotdogImage]

x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index],
                              variable=x,
                              value=index,
                              padx=25,
                              font=("Impact", 50),
                              image=foodImages[index],
                              compound="left",
                              indicatoron=False,
                              width=475,
                              command=order)
    radiobutton.pack(anchor=W)

window.mainloop()
