from tkinter import *
from tkinter import messagebox

###### 1. CREATE WINDOW ######
window = Tk()
window.title('Demo GUI 02')
window.geometry('400x300')

###### 2. IMPLEMENT HANDLERS ######
def btn_ok_clicked():
    # get name from txt_name
    name = txt_name.get()
    # get age from txt_age
    age = txt_age.get()
    # show messagebox
    messagebox.showinfo(f'Hello {name}', f'You are {age} years old')

###### 3. CREATE WIDGETS ######
# create a label
lbl_name = Label(window, text='Name')
lbl_name.grid(row=0, column=0)

txt_name = Entry(window)
txt_name.grid(row=0, column=1)

lbl_age = Label(window, text='Age')
lbl_age.grid(row=1, column=0)

txt_age = Entry(window)
txt_age.grid(row=1, column=1)

btn_ok = Button(window, text='OK', command=btn_ok_clicked)
btn_ok.grid(row=2, column=1, sticky=W)

###### RUN ######
window.mainloop()