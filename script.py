import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import re

def create_table():
    conn = sqlite3.connect("registration.db")
    with conn:
        cursor = conn.cursor()
        q = cursor.execute('CREATE TABLE IF NOT EXISTS users(id integer primary key autoincrement not null, fullname text, mobile text, age integer, gender text, email text, event_category text, event_type text)')
        conn.commit()
        print(q)
        conn.close()

create_table()

def verify_email():
    if re.match('^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$',email_input.get()):
        return True

def view_entry():
    conn = sqlite3.connect("registration.db")
    show_entries.place(x="5",y="400")
    with conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        result = cursor.fetchall()
        for entry in result:
            show_entries.insert(END, str(entry) + "\n")

def clear_entry():
    conn = sqlite3.connect("registration.db")
    show_entries.place(x="5",y="400")
    with conn:
        cursor = conn.cursor()
        cursor.execute("DELETE from users")
        show_entries.delete(1.0,END)
        messagebox.showinfo("Alert","successfully cleared database")

def reset():
    fname_input.delete(0, END)
    lname_input.delete(0, END)
    mobile_input.delete(0, END)
    email_input.delete(0, END)
    age_input.delete(0, END)
    event_input.delete(0, END)
    event_type_input.delete(0, END)

def pick_event(a):
    if eventVar.get() == "Sport":
        event_type_input.config(value=Sport)
        event_type_input.current()
    elif eventVar.get() == "Cultural":
        event_type_input.config(value=Cultural)
        event_type_input.current()
    elif eventVar.get() == "Academic":
        event_type_input.config(value=Academic)
        event_type_input.current()

def submit():
    print(fname_input.get(), lname_input.get(), mobile_input.get(), email_input.get(), gender.get(), age_input.get(), eventVar.get(), eventType.get())
    sql = f'INSERT INTO users(fullname, mobile, email, gender, age, event_category, event_type) VALUES("{fname_input.get() + " " + lname_input.get()}","{mobile_input.get()}","{email_input.get()}","{gender.get()}",{age_input.get()},"{eventVar.get()}","{eventType.get()}")'
    print(sql)
    conn = sqlite3.connect("registration.db")
    with conn:
        cursor = conn.cursor()
        q = cursor.execute(sql)
        conn.commit()
        print(q)
        conn.close()
        messagebox.showinfo("Alert", "successfully registered")

window = Tk()
window.title('REGISTERATION FORM')
window.geometry("800x800")
backgroundColor = 'coral1'
window.configure(background=backgroundColor)

title_label = Label(window, text="REGISTRATION FORM", width="20",font=("Arial", 25),bg=backgroundColor)
title_label.pack()

frame = Frame(window)
frame.configure(background=backgroundColor)
frame.pack(fill="both", expand=True)

events = ['Cultural', 'Sport', 'Academic']
Cultural = ['Singing Competition', 'Dancing Competition', 'Drawing Competition', 'Mehendi Competition',
            'Rangoli Competition']
Sport = ['Cricket', 'Volleyball', 'Badminton', 'Football', 'Basketball']
Academic = ['Microcontroller based quiz', 'GK quiz', 'Coding quiz']

# label and input configuration
fname_label = Label(frame, text="First Name", width="20",height="3",bg=backgroundColor)
fname_label.grid(row=0,column=0)
fname_input = Entry(frame, width="20")
fname_input.grid(row=0,column=1)

lname_label = Label(frame, text="Last Name", width="20", height="3",bg=backgroundColor)
lname_label.grid(row=0,column=2)
lname_input = Entry(frame, width="20")
lname_input.grid(row=0,column=3)

mobile_label = Label(frame, text="Mobile No.", width="20", height="3",bg=backgroundColor)
mobile_label.grid(row=1,column=0)
mobile_input = Entry(frame, width="20")
mobile_input.grid(row=1,column=1)

email_label = Label(frame, text="email", width="20", height="3",bg=backgroundColor)
email_label.grid(row=1,column=2)
email_input = Entry(frame, width="20")
email_input.grid(row=1,column=3)

genderFrame = Frame(frame)
genderFrame.grid(row=2,column=1)
gender_label = Label(frame, text="Gender", width="20", height="3",bg=backgroundColor)
gender_label.grid(row=2,column=0)
gender = StringVar()
gender_input1 = Radiobutton(genderFrame, text="Male", variable=gender, value="Male",bg=backgroundColor)
gender_input2 = Radiobutton(genderFrame, text="Female", variable=gender, value="Female",bg=backgroundColor)
gender_input3 = Radiobutton(genderFrame, text="Other", variable=gender, value="Other",bg=backgroundColor)
gender_input1.grid(row=2,column=1)
gender_input2.grid(row=2,column=2)
gender_input3.grid(row=2,column=3)

age_label = Label(frame, text="Age", width="20", height="3",bg=backgroundColor)
age_label.grid(row=2,column=2)
age_input = Entry(frame, width="20")
age_input.grid(row=2,column=3)

eventVar = StringVar()
event_label = Label(frame, text="Select event category", width="20", height="3",bg=backgroundColor)
event_label.grid(row=3,column=0)
event_input = ttk.Combobox(frame, width="20", value=events, textvariable=eventVar)
event_input.grid(row=3,column=1)
event_input.current()
event_input.bind("<<ComboboxSelected>>", pick_event)

eventType = StringVar()
event_type_label = Label(frame, text="Select event type", width="20", height="3",bg=backgroundColor)
event_type_label.grid(row=3,column=2)
event_type_input = ttk.Combobox(frame, width="20", textvariable=eventType)
event_type_input.grid(row=3,column=3)

agreed = IntVar()
termsAndConditions = Checkbutton(frame,  text='I agree all terms and conditions', onvalue=1, offvalue=0, variable=agreed, background=backgroundColor)
termsAndConditions.grid(row=4,column=1, columnspan=2)

submit_button = Button(frame, text="register",width="20",command=submit,font=('Arial',22))
submit_button.grid(row=5,column=0,columnspan=2)

reset_button = Button(frame, text="reset",width="20",command=reset,font=('Arial',22))
reset_button.grid(row=5,column=2,columnspan=2)

view_button = Button(frame, text="view all entries", width="40", height="2", command=view_entry)
view_button.grid(row=6,column=1, columnspan=2, padx=20, pady=10)

clear_button = Button(frame, text="clear entries", width="40", height="2", command=clear_entry)
clear_button.grid(row=7,column=1, columnspan=2, padx=20)

show_entries = Text(window, width="65", height="15", bg="black", fg="green", font=("Arial", 20))
# show_entries.current()

window.mainloop()