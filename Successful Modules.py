#-----------------------------------------------------------------------

from tkinter import *

def goto_window(event):
        print(variable1.get())

def f2createmenu(master, options):
        variable = StringVar(master)
        variable.set("one")  # default value
        w = OptionMenu(master, variable, *options)
        w.pack()
        return variable

master = Tk()
options = ("one", "two", "three")

variable1 = StringVar()
variable1 = f2createmenu(master, options)

button1 = Button(master, text="Click Me Here")
button1.bind("<Button-1>", goto_window)
button1.pack()

master.mainloop()
#-----------------------------------------------------------------------
options_board = ("Pokhara University", "Tribhuvan University", "Kathmandu Univeristy", "Mid-Western University",
                 "Purbanchal University", "Higher Secondary Education Board", "Nepal Education Board")

teacher_board_label = Label(teacher_frame3, text="University/Board", font=("verdana", 10), width=19,
                                relief=FLAT, fg="black", bg="bisque")
teacher_board_label.grid(row=1, column=1, pady=5, padx=5)
teacher_board_entry = ttk.Combobox(teacher_frame3, state="readonly", values=options_board, font=("verdana", 10, 'bold'), width=17, textvariable=teacher_board1)
teacher_board_entry.current(2)
teacher_board_entry.grid(row=2, column=1, pady=5, padx=5)

#-----------------------------------------------------------------------


import datetime
a = datetime.datetime.now().strftime('%Y')
b = datetime.datetime.now().strftime('%m')
c = datetime.datetime.now().strftime('%d')
current = int(input("Enter your Year?  "))
month_nepali = int(input("Enter your Month?  "))
neapli_day = int(input("Enter your Day?  "))

def date_converter_returning_age(provided_year, provided_month, provided_day, now_year, now_month, now_day):
    year = int(provided_year)
    month = int(provided_month)
    day = int(provided_day)
    a = int(now_year)
    b = int(now_month)
    c = int(now_day)
    if month<10:
        if month == 9 and day>15:
            day-=15
            month=1
            year-=56
        elif month == 9 and (day<15 or day==15):
            day+=15
            month=12
            year-=57
        elif (day<15 or day==15):
            day+=15
            month+=3
            year-=57
        else:
            day-=15
            month+=4
            year-=57
    else:
        year-=56
        if (day<15 or day == 15):
            day+=15
            month-=9

        else:
            day-=15
            month-=8

    #Age Calculation Stars
    if b>month:
        if c>day:
            year1 = a-year
            month1 = b-month
            day1 = c-day
        else:
            year1 = a-year
            month1 = (b-month)-1
            day1 = 30-(day-c)

    elif b<month:
        if c > day:
            year1 = (a-year)-1
            month1 = 12-(month-b)
            day1 = c-day
        else:
            day1 = 30-(day-c)
            month1 = 11-(month-b)
            year1 = (a-year)-1
    elif c == day:
        if b>month:
            day1 = 0
            month1 = b-month
            year1 = a-year
        else:
            day1 = 0
            month1 = 12-(month-b)
            year1 = (a - year)-1
    else:
        if c>day:
            day1 = c-day
            month1 = b-month
            year1 = a-year
        else:
            day1 = 30-(day-c)
            month1 = 11
            year1 = a-year


    age = str(year1) + "Years" + str(month1) + "Month" + str(day1) + "Days"

    print(year, month, day)
    print (age)

date_converter_returning_age(current, month_nepali, neapli_day, a, b, c)

#---------------------------------------------------------------


import tkinter
import os

main_path = os.getcwd()
main_folder = "School Database"
print(main_path)

path1 = main_path + "\\" + main_folder
folder1 = "Students Database"
folder2 = "Teachers Database"
folder3 = "Staffs Database"
path11 = path1 + "\\" + folder1
path12 = path1 + "\\" + folder2
path13 = path1 + "\\" + folder3
folder11 = "Composite Classwise Records"
folder12 = "Individual Records"
folder13 = "Registration Records"
folder14 = "MixedUp Records"
path111 = path1 + "\\" + folder11
path112 = path1 + "\\" + folder12
path113 = path1 + "\\" + folder13
path114 = path1 + "\\" + folder14
folder21 = "Composite  Records"
folder22 = "Individual Records"
path121 = path1 + "\\" + folder21
path122 = path1 + "\\" + folder22
folder31 = "Composite  Records"
folder32 = "Individual Records"
path131 = path1 + "\\" + folder31
path132 = path1 + "\\" + folder32


def directory(instance):
    if os.path.exists(main_folder) is False:

        os.makedirs(main_folder)
        os.chdir(path1)
        os.makedirs(folder1)
        os.makedirs(folder2)
        os.makedirs(folder3)

        os.chdir(path11)
        os.makedirs(folder11)
        os.makedirs(folder12)
        os.makedirs(folder13)
        os.makedirs(folder14)

        os.chdir(path12)
        os.makedirs(folder21)
        os.makedirs(folder22)

        os.chdir(path13)
        os.makedirs(folder31)
        os.makedirs(folder32)

    else:
        print("Already Exists")

    if instance == "Student":


directory()

#------------------------------------------------------





from tkinter import *

def callUpdater():
    text = textBox.get()
    textBox.delete(0, 'end')
    chat.configure(state='normal')
    chat.insert('1.0', text + '\n')
    chat.configure(state='disabled')

root = Tk()
chatBox = Scrollbar(root)
chat = Text(root, wrap='word', state='disabled', width=50,
            yscrollcommand=chatBox.set)
chatBox.configure(command=chat.yview)

chat.grid(row=0, columnspan=2, sticky='ewns')
chatBox.grid(row=0, column=2, sticky='ns')

frame1 = Frame(root)
frame1.grid(row=0, column=0, sticky="nwes")

main_scroll = Scrollbar(frame1)
canvas_main = Canvas(frame1, yscrollcommand=main_scroll.set, width=1300)
main_scroll.configure(command=canvas_main.yview)
canvas_main.grid(row=0, column=0, sticky="ewns")
main_scroll.grid(row=0, column=1, sticky="ns")

frame = Frame(canvas_main, width=1000, height=1300)
frame.grid(row=0, column=0)

Label(root, text="Input: ").grid(row=1, column=0)

textBox = Entry(root, bd=0, width=40, bg="pink")
textBox.grid(row=1, column=1)

Button(root, text="Send", command=callUpdater).grid(row=2, columnspan=2)
root.mainloop()