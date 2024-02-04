import tkinter as tk
from tkinter import ttk

def button_func():
    #get the content of the entry
    entry_text = entry.get()

    #update the label
    #label.configure(text = 'some other text')
    label['text'] = entry_text
    entry['state'] = 'disabled'

def exercise_func():
    #update the label
    label['text'] = 'Some text'
    entry['state'] = 'enabled'

#window
window = tk.Tk()
window.title('Getting and setting widgets')

#widgets

label = ttk.Label(master = window, text = 'Some text')
label.pack()

entry = ttk.Entry(master = window)
entry.pack()

button = ttk.Button(master = window, text = 'button', command = button_func)
button.pack()

exercise = ttk.Button(master =window, text = 'some text', command = exercise_func)
exercise.pack()

#run
window.mainloop()