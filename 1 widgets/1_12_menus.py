import tkinter as tk
from tkinter import ttk

#window
window = tk.Tk()
window.geometry('600x400')
window.title('Menu')

#menu
menu = tk.Menu(window)

#sub menu
file_menu = tk.Menu(menu, tearoff = False)
file_menu.add_command(label = 'New', command = lambda : print('New file'))
file_menu.add_command(label = 'Open', command = lambda : print('Open file'))
file_menu.add_separator()
menu.add_cascade(label = 'File', menu = file_menu)

#another sub menu
help_menu = tk.Menu(menu, tearoff = False)
help_menu.add_command(label = 'Help entry', command = lambda : print(help_check_string.get()))

help_check_string = tk.StringVar()
help_menu.add_checkbutton(label = 'check', onvalue = 'on', offvalue = 'off', variable = help_check_string)

menu.add_cascade(label = 'Help', menu = help_menu)

#exercise
exercise1 = tk.Menu(menu, tearoff = False)
exercise1.add_command(label = 'Exercise 1', command = lambda : print('Exercise 1'))
menu.add_cascade(label = 'Exercise 1', menu = exercise1)

exercise2 = tk.Menu(menu, tearoff = False)
exercise2.add_command(label = 'Exercise 2', command = lambda : print('Exercise 2'))
exercise1.add_cascade(label = 'Exercise 2', menu = exercise2)

window.configure(menu = menu)

#menu button
menu_button = tk.Menubutton(window, text = 'MenuButton')
menu_button.pack()

button_sub_menu = tk.Menu(menu_button,tearoff = False)
button_sub_menu.add_command(label = 'entry 1', command = lambda : print('test 1'))
button_sub_menu.add_checkbutton(label  = 'check 1')
menu_button.configure(menu = button_sub_menu)

#run
window.mainloop()