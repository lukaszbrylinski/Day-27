from tkinter import *

def button_clicked():
    # my_label["text"] = input.get()
    km_value_label.config(text=round(float(entry.get())*1.609))



window = Tk()
window.minsize(width=300, height=100)
window.title("Miles to Km Converter")

entry = Entry(width=5)
entry.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

km_value_label = Label(text="0")
km_value_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate",command=button_clicked)
calculate_button.grid(column=1, row=2)


window.mainloop()

