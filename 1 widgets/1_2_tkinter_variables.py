import tkinter as tk
from tkinter import ttk

def button_func():
    print(string_var.get())
    string_var.set('button pressed')

#window
window = tk.Tk()
window.title('Tkineter Variables')

#tkinter variable
string_var = tk.StringVar()

#widgets

label = ttk.Label(master=window, text='test', textvariable=string_var)
label.pack()

entry = ttk.Entry(master=window, text='test', textvariable=string_var)
entry.pack()

button = ttk.Button(master=window, text='button', command=button_func)
button.pack()

#exercise
exercise_var = tk.StringVar()

exercise_label = ttk.Label(master=window, textvariable=exercise_var)
exercise_label.pack()

exercise_entry = ttk.Entry(master=window, textvariable=exercise_var)
exercise_entry.pack()

exercise_entry2 = ttk.Entry(master=window, textvariable=exercise_var)
exercise_entry2.pack()

exercise_var.set('test')

#run
window.mainloop()