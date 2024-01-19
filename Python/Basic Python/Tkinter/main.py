from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label.pack(side="left")
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)
my_label["text"] = "New text"
my_label.config(text="New Text")
my_label.config(padx=50, pady=50)


# Button
def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


button = Button(text="Click Me", command=button_clicked)
button2 = Button(text="New Button")
# button.pack(side="left")
button.grid(column=2, row=2)
button2.grid(column=3, row=0)

# Entry
input = Entry(width=10)
# input.pack(side="left")
input.grid(column=4, row=3)
# print(input.get())

window.mainloop()
