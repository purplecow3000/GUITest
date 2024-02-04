import tkinter as tk
from tkinter import ttk

#set up
window = tk.Tk()
window.title('Buttons')
window.geometry('600x400')

#button
def button_func():
    print('A basic button')
    print(radio_var.get())

button_string = tk.StringVar(value = 'A button with string var')
button = ttk.Button(window, text = 'A basic button', command = button_func, textvariable = button_string)
button.pack()

#check button
check_var = tk.IntVar(value = 10)
check1 = ttk.Checkbutton(
    window,
    text = 'checkbox 1',
    command = lambda: print(check_var.get()),
    variable = check_var,
    onvalue = 10,
    offvalue = 5)
check1.pack()

check2 = ttk.Checkbutton(
    window,
    text = 'Checkbox 2',
    command = lambda: check_var.set(5))
check2.pack()

#radio buttons
radio_var = tk.StringVar()
radio1 = ttk.Radiobutton(
    window,
    text = "Radiobutton 1",
    value = 'radio 1',
    variable = radio_var,
    command = lambda: print(radio_var.get()))
radio1.pack()
radio2 = ttk.Radiobutton(window, text = "Radiobutton 2", value = 2, variable = radio_var)
radio2.pack()

#exercise
check_var2 = tk.BooleanVar(value = True)
check3 = ttk.Checkbutton(
    window,
    text = 'Exercise Checkbox',
    variable = check_var2,
    command = lambda: print(radio_var2.get()))
check3.pack()

def radio_button_func():
    print(check_var2.get())
    check_var2.set(False)

radio_var2 = tk.StringVar(value = 'A')
radio_a = ttk.Radiobutton(
    window,
    text = "Execerise Radiobutton A",
    value = 'A',
    variable = radio_var2,
    command = radio_button_func)
radio_a.pack()
radio_b = ttk.Radiobutton(
    window,
    text = "Execerise Radiobutton B",
    value = 'B',
    variable = radio_var2,
    command = radio_button_func)
radio_b.pack()

#run
window.mainloop()