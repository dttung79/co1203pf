from tkinter import *
from tkinter import messagebox

###### 1. CREATE WINDOW ######
window = Tk()
window.title('Demo radio buttons')
window.geometry('250x300')

###### 2. IMPLEMENT HANDLERS ######
def check_answer():
    points = 0
    n_choices = 0
    if triangle_var.get() == True:
        n_choices += 1

    if square_var.get() == True:
        n_choices += 1
        points += 5
    
    if circle_var.get() == True:
        n_choices += 1
    
    if rectangle_var.get() == True:
        n_choices += 1
        points += 5
    
    if n_choices > 2:
        points = 0
    
    lbl_result.config(text=f'Result: {points} pts')

###### 3. CREATE WIDGETS ######
lbl_question = Label(window, text='Which shape has 4 sides?')
lbl_question.grid(row=0, column=0, padx=50, pady=5, sticky=W)

triangle_var = BooleanVar()
cb_triangle = Checkbutton(window, text='Triangle', variable=triangle_var)
cb_triangle.grid(row=1, column=0, padx=50, pady=5, sticky=W)

square_var = BooleanVar()
cb_square = Checkbutton(window, text='Square', variable=square_var)
cb_square.grid(row=2, column=0, padx=50, pady=5, sticky=W)

circle_var = BooleanVar()
cb_circle = Checkbutton(window, text='Circle', variable=circle_var)
cb_circle.grid(row=3, column=0, padx=50, pady=5, sticky=W)

rectangle_var = BooleanVar()
cb_rectangle = Checkbutton(window, text='Rectangle', variable=rectangle_var)
cb_rectangle.grid(row=4, column=0, padx=50, pady=5, sticky=W)

btn_answer = Button(window, text='Answer', command=check_answer)
btn_answer.grid(row=5, column=0, padx=50, pady=5, sticky=W)

lbl_result = Label(window, text='Result: O pts')
lbl_result.grid(row=6, column=0, padx=50, pady=5, sticky=W)
###### 4. MAIN LOOP ######
window.mainloop()