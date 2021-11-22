import math
from tkinter import *
import tkinter.messagebox as tmsg
import time
from math import *


def getvals(event):
    value = event.widget.cget('text')
    if value == 'Clr':
        sc_variable.set('')
    elif value == 'Pi':
        sc_variable.set(3.141)
    elif value == '=':
        try:
            sc_variable.set(eval(screen.get()))
            screen.update()
        except Exception as e:
            sc_variable.set('Error ')
            screen.update()
            screen.update()
            time.sleep(1)
            sc_variable.set('')
            screen.update()
            screen.update()

    else:
        sc_variable.set(f'{sc_variable.get()}{value}')


root = Tk()
canvas_width = 568
canvas_height = 610
root.geometry(f'{canvas_width}x{canvas_height}')
root.maxsize(canvas_width, canvas_height)
root.minsize(canvas_width, canvas_height)
root.title('Scientific Calculator ')


my_menu = Menu(root)
m1 = Menu(my_menu, tearoff=0, fg='red')
root.config(menu=my_menu)
my_menu.add_command(label='Exit', command=quit)

sc_variable = StringVar()
screen = Entry(root, textvariable=sc_variable, font='lucida 35 bold', fg='black', bg='white', border=25)
screen.grid(row=0, column=0, columnspan=5)
# define buttons

# Row 1
f = Frame(root)
f.place()
b1 = Button(root, text='sin', width=5, height=2, bg='black', fg='white', font=('Helvetica', 20, 'bold'), bd=4)
b2 = Button(root, text='cos', width=5, height=2, bg='black', fg='white', font=('Helvetica', 20, 'bold'), bd=4)
b3 = Button(root, text='tan', width=5, height=2, bg='black', fg='white', font=('Helvetica', 20, 'bold'), bd=4)
b4 = Button(root, text='(', width=5, height=2, bg='black', fg='white', font=('Helvetica', 20, 'bold'), bd=4)
b5 = Button(root, text=")", width=5, height=2, bg='black', fg='white', font=('Helvetica', 20, 'bold'), bd=4)

b1.bind('<Button-1>', getvals)
b2.bind('<Button-1>', getvals)
b3.bind('<Button-1>', getvals)
b4.bind('<Button-1>', getvals)
b5.bind('<Button-1>', getvals)
buttons = [b1, b2, b3, b4, b5]

for i in range(5):
    buttons[i].grid(row=1, column=i)

# Row 2
f = Frame(root)
f.place()
b1 = Button(root, text='7', width=5, height=2, bg='white', fg='black', font=('Helvetica', 20, 'bold'), bd=4)
b2 = Button(root, text='8', width=5, height=2, bg='white', fg='black', font=('Helvetica', 20, 'bold'), bd=4)
b3 = Button(root, text="9", width=5, height=2, bg='white', fg='black', font=('Helvetica', 20, 'bold'), bd=4)
b4 = Button(root, text='log10', width=5, height=2, bg='black', fg='white', font=('Helvetica', 20, 'bold'), bd=4)
b5 = Button(root, text='Clr', width=5, height=2, bg='blue', fg='white', font=('Helvetica', 20, 'bold'), bd=4)

b1.bind('<Button-1>', getvals)
b2.bind('<Button-1>', getvals)
b3.bind('<Button-1>', getvals)
b4.bind('<Button-1>', getvals)
b5.bind('<Button-1>', getvals)
buttons = [b1, b2, b3, b4, b5]

for i in range(5):
    buttons[i].grid(row=2, column=i)

# Row 3

f = Frame(root)
f.place()

b1 = Button(root, text='4', width=5, height=2, bg='white', fg='black', font=('Helvetica', 20, 'bold'), bd=4)
b2 = Button(root, text='5', width=5, height=2, bg='white', fg='black', font=('Helvetica', 20, 'bold'), bd=4)
b3 = Button(root, text='6', width=5, height=2, bg='white', fg='black', font=('Helvetica', 20, 'bold'), bd=4)
b4 = Button(root, text='*', width=5, height=2, bg='white', fg='black', font=('Helvetica', 20, 'bold'), bd=4)
b5 = Button(root, text='/', width=5, height=2, bg='white', fg='black', font=('Helvetica', 20, 'bold'), bd=4)

b1.bind('<Button-1>', getvals)
b2.bind('<Button-1>', getvals)
b3.bind('<Button-1>', getvals)
b4.bind('<Button-1>', getvals)
b5.bind('<Button-1>', getvals)
buttons = [b1, b2, b3, b4, b5]

for i in range(5):
    buttons[i].grid(row=3, column=i)

# Row 4
f = Frame(root)
f.place()
b1 = Button(root, text='1', width=5, height=2, bg='white', fg='black', font=('Helvetica', 20, 'bold'), bd=4)
b2 = Button(root, text='2', width=5, height=2, bg='white', fg='black', font=('Helvetica', 20, 'bold'), bd=4)
b3 = Button(root, text='3', width=5, height=2, bg='white', fg='black', font=('Helvetica', 20, 'bold'), bd=4)
b4 = Button(root, text='+', width=5, height=2, bg='white', fg='black', font=('Helvetica', 20, 'bold'), bd=4)
b5 = Button(root, text='-', width=5, height=2, bg='white', fg='black', font=('Helvetica', 20, 'bold'), bd=4)

b1.bind('<Button-1>', getvals)
b2.bind('<Button-1>', getvals)
b3.bind('<Button-1>', getvals)
b4.bind('<Button-1>', getvals)
b5.bind('<Button-1>', getvals)
buttons = [b1, b2, b3, b4, b5]

for i in range(5):
    buttons[i].grid(row=4, column=i)

# Row 5
f = Frame(root)
f.place()
b1 = Button(root, text='0', width=5, height=2, bg='white', fg='black', font=('Helvetica', 20, 'bold'), bd=4)
b2 = Button(root, text='.', width=5, height=2, bg='white', fg='black', font=('Helvetica', 20, 'bold'), bd=4)
b3 = Button(root, text='Pi', width=5, height=2, bg='white', fg='black', font=('Helvetica', 20, 'bold'), bd=4)
b4 = Button(root, text='%', width=5, height=2, bg='white', fg='black', font=('Helvetica', 20, 'bold'), bd=4)
b5 = Button(root, text='=', width=5, height=2, bg='white', fg='black', font=('Helvetica', 20, 'bold'), bd=4)

b1.bind('<Button-1>', getvals)
b2.bind('<Button-1>', getvals)
b3.bind('<Button-1>', getvals)
b4.bind('<Button-1>', getvals)
b5.bind('<Button-1>', getvals)
buttons = [b1, b2, b3, b4, b5]

for i in range(5):
    buttons[i].grid(row=5, column=i)

f = Frame(root)
f.place()

root.mainloop()
