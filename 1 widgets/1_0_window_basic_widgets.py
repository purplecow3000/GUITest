import tkinter as tk
from tkinter import ttk

def button_func():
    print('A button was pressed')

def hello():
    print('hello')

# create a window
window = tk.Tk()
window.title('Window and Widgets')
window.geometry('800x500')

#ttk label
label = ttk.Label(master = window, text = 'This is a test')
label.pack()

#tk. text
text = tk.Text(master = window)
text.pack()

#ttk entry
entry = ttk.Entry(master = window)
entry.pack()

#my label
my_label = ttk.Label(master = window, text = 'my label')
my_label.pack()

#hello button
#hello_button = ttk.Button(master = window, text = 'my label', command = hello)
hello_button = ttk.Button(master = window, text = 'my label', command = lambda: print('hello'))
hello_button.pack()

#ttk button
button = ttk.Button(master = window, text = 'A button', command = button_func)
button.pack()

# run
window.mainloop()