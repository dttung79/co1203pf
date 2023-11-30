from tkinter import *
from tkinter import messagebox

###### 1. CREATE WINDOW ######
window = Tk()
window.title('Arithmetic Operators')
window.geometry('400x300')

###### 2. IMPLEMENT HANDLERS ######
def calculate(op):
    a = int(txt_a.get())
    b = int(txt_b.get())
    if op == '+':
        c = a + b
    elif op == '-':
        c = a - b
    elif op == 'x':
        c = a * b
    elif op == ':':
        c = a / b
    
    txt_c.delete(0, END)
    txt_c.insert(0, c)

def btn_add_clicked():
    calculate('+')

def btn_sub_clicked():
    calculate('-')

def btn_mul_clicked():
    calculate('x')

def btn_div_clicked():
    calculate(':')

###### 3. CREATE WIDGETS ######
lbl_a = Label(window, text='a')
lbl_a.grid(row=0, column=0, padx=10, pady=5)

txt_a = Entry(window)
txt_a.grid(row=0, column=1, padx=0, pady=5)

lbl_b = Label(window, text='b')
lbl_b.grid(row=1, column=0, padx=10, pady=5)

txt_b = Entry(window)
txt_b.grid(row=1, column=1, padx=0, pady=5)

lbl_c = Label(window, text='c')
lbl_c.grid(row=2, column=0, padx=10, pady=5)

txt_c = Entry(window)
txt_c.grid(row=2, column=1, padx=0, pady=5)

btn_add = Button(window, text='+', command=btn_add_clicked)
btn_add.grid(row=3, column=1, padx=0, pady=5)

btn_sub = Button(window, text='-', command=btn_sub_clicked)
btn_sub.grid(row=4, column=1, padx=0, pady=5)

btn_mul = Button(window, text='*', command=btn_mul_clicked)
btn_mul.grid(row=5, column=1, padx=0, pady=5)

btn_div = Button(window, text='/', command=btn_div_clicked)
btn_div.grid(row=6, column=1, padx=0, pady=5)

###### RUN ######
window.mainloop()