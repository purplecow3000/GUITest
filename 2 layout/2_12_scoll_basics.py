import tkinter as tk
from tkinter import ttk
from random import randint, choice

# window
window = tk.Tk()
window.geometry('600x400')
window.title('Scrolling')

# # canvas
# canvas = tk.Canvas(window, bg = 'white', scrollregion= (0,0,2000,5000))
# canvas.create_line(0,0,2000,5000, fill = 'green', width = 10)
# for i in range(100):
#     l = randint(0,2000)
#     t = randint(0,5000)
#     r = l + randint(10,500)
#     b = t + randint(10,500)
#     color = choice(('red', 'green', 'blue', 'yellow', 'orange'))
#     canvas.create_rectangle(l, r, t, b, fill = color)
# canvas.pack(expand = True, fill = 'both')

# # mouse wheel scrolling
# canvas.bind('<MouseWheel>', lambda event: canvas.yview_scroll(-int(event.delta / 60), 'units'))

# # scrollbar
# scrollbar = ttk.Scrollbar(window, orient = 'vertical', command = canvas.yview)
# canvas.configure(yscrollcommand = scrollbar.set)
# scrollbar.place(relx = 1, rely = 0, relheight = 1, anchor = 'ne')

# # exercise
# exercise_scrollbar = ttk.Scrollbar(window, orient = 'horizontal', command = canvas.xview)
# canvas.configure(xscrollcommand = exercise_scrollbar.set)
# exercise_scrollbar.place(relx = 0, rely = 1, relwidth = 1, anchor = 'sw')

# canvas.bind('<Control MouseWheel>', lambda event: canvas.xview_scroll(-int(event.delta / 60), 'units'))

# # text
# text = tk.Text(window)
# for i in range (1,200):
#     text. insert(f'{i}.0', f'text: {i} \n')
# text.pack(expand = True, fill = 'both')

# scrollbar_text = ttk.Scrollbar(window, orient = 'vertical', command = text.yview)
# text.configure(yscrollcommand = scrollbar_text.set)
# scrollbar_text.place(relx = 1, rely = 0, relheight = 1, anchor = 'ne')

#treeview
table = ttk.Treeview(window, columns = (1, 2), show = 'headings')
table.heading(1, text = 'First name')
table.heading(2, text = 'Surname')
first_names = ['Bob', 'Maria', 'Alex', 'James', 'Susan', 'Henry', 'Lisa', 'Anna', 'Lisa']
last_names = ['Smith', 'Brown', 'Wilson', 'Thomson', 'Cook', 'Taylor', 'Walker', 'Clark']
for i in range(100):
    table.insert(parent = '', index = tk.END, values = (choice(first_names), choice(last_names)))
table.pack(fill = 'both', expand = True)

scrollbar_table = ttk.Scrollbar(window, orient = 'vertical', command = table.yview)
table.configure(yscrollcommand = scrollbar_table.set)
scrollbar_table.place(relx = 1, rely = 0, relheight = 1, anchor = 'ne')

# run
window.mainloop()