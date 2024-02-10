import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Pack parenting')
window.geometry('400x600')

# Top frame
top_frame = ttk.Frame(window)
label1 = ttk.Label(top_frame, text = 'First Label', background = 'red')
label2 = ttk.Label(top_frame, text = 'Label 2', background = 'blue')

# middle widget
label3 = ttk.Label(window, text = 'Another label', background = 'green')

# bottom frame
bottom_frame = ttk.Frame(window)
label4 = ttk.Label(bottom_frame, text = 'Last of the labels', background = 'orange')
button1 = ttk.Button(bottom_frame, text = 'A Button')
button2 = ttk.Button(bottom_frame, text = 'Another Button')

# top layout
label1.pack(side = 'left', fill = 'both', expand = True)
label2.pack(side = 'left', fill = 'both', expand = True)
top_frame.pack(fill = 'both', expand = True)

# middle layout
label3.pack(expand = True)

# bottom layout
button1.pack(side = 'left', expand = True, fill = 'both')
label4.pack(side = 'left', expand = True, fill = 'both')
button2.pack(side = 'left', expand = True, fill = 'both')
bottom_frame.pack(expand = True, fill = 'both', padx = 20, pady = 20)

# exercise frame
exercise_frame = ttk.Frame(bottom_frame)
button3 = ttk.Button(exercise_frame, text = 'Button 3')
button4 = ttk.Button(exercise_frame, text = 'Button 4')
button5 = ttk.Button(exercise_frame, text = 'Button 5')

#exercise layout
button3.pack(expand = True, fill = 'both')
button4.pack(expand = True, fill = 'both')
button5.pack(expand = True, fill = 'both')
exercise_frame.pack(side = 'left', expand = True, fill = 'both')

# run
window.mainloop()