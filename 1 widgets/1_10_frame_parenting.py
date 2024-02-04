import tkinter as tk
from tkinter import ttk

#setup
window = tk.Tk()
window.geometry('600x400')
window.title('Frame and parenting')

#frame
frame = ttk.Frame(window, width = 200, height = 200, borderwidth = 10, relief = tk.GROOVE)
frame.pack_propagate(False)
frame.pack(side = 'left')

#master setting
label = ttk.Label(frame, text = 'Label in frame')
label.pack()

button = ttk.Button(frame, text = 'button in a frame')
button.pack()

#example
label2 = ttk.Label(window, text = 'label outside frame')
label2.pack(side = 'left')

#exercise
exercise_frame = ttk.Frame(window, borderwidth = 10, relief = tk.GROOVE)
exercise_frame.pack(side = 'right')

exercise_label = ttk.Label(exercise_frame, text = 'text')
exercise_label.pack(side = 'left')

exercise_button = ttk.Button(exercise_frame, text = 'text')
exercise_button.pack(side = 'left')

exercise_entry = ttk.Entry(exercise_frame)
exercise_entry.pack(side = 'left')

#run
window.mainloop()