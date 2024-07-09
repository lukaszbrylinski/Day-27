from tkinter import *

def button_clicked():
    # my_label["text"] = input.get()
    my_label.config(text=input.get())

window = Tk()
window.title("MY First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

#Label

my_label = Label(text="I Am A Label", font=("Arial", 24, "normal"))
## Alternate ways to alter properties of particular components
my_label.config(text=("New Text"))
# my_label.place(x=100, y=200) # Precise positioning
my_label.grid(column=0, row=0) # Defining columns and rows, inbetween pack() and place()
my_label.config(padx=50, pady=50)
# my_label.pack() # Reasonably logical placing of widgets automatically



button = Button(text="Click Me",command=button_clicked)
button.grid(column=1, row=1)
# button.pack()
new_button = Button(text="Click Me",command=button_clicked)
new_button.grid(column=2, row=0)
#Entry

input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)
# input.pack()


window.mainloop()