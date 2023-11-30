from tkinter import *
from tkinter import messagebox

###### 1. CREATE WINDOW ######
window = Tk()
window.title('Demo radio buttons')
window.geometry('200x300')

###### 2. IMPLEMENT HANDLERS ######
def check_answer():
    # get user selected answer
    answer = answer_var.get()
    if answer == 2:
        lbl_result.config(text='Result: Correct!')
    else:
        lbl_result.config(text='Result: Wrong!')
    
###### 3. CREATE WIDGETS ######
lbl_question = Label(window, text='1 + 1 = ?')
lbl_question.grid(row=0, column=0, padx=50, pady=5)

answer_var = IntVar()
rd_option1 = Radiobutton(window, text='1', value=1, variable=answer_var)
rd_option1.grid(row=1, column=0, padx=50, pady=5)

rd_option2 = Radiobutton(window, text='2', value=2, variable=answer_var)
rd_option2.grid(row=2, column=0, padx=50, pady=5)

rd_option3 = Radiobutton(window, text='3', value=3, variable=answer_var)
rd_option3.grid(row=3, column=0, padx=50, pady=5)

rd_option4 = Radiobutton(window, text='4', value=4, variable=answer_var)
rd_option4.grid(row=4, column=0, padx=50, pady=5)

btn_answer = Button(window, text='Answer', command=check_answer)
btn_answer.grid(row=5, column=0, padx=50, pady=5)

lbl_result = Label(window, text='Result')
lbl_result.grid(row=6, column=0, padx=50, pady=5)
###### 4. MAIN LOOP ######
window.mainloop()