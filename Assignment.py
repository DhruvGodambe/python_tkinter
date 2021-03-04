from tkinter import *
from tkinter import messagebox

from datetime import datetime

# gender = IntVar()
# agree = IntVar()
win = Tk()
win.geometry("800x600+100+100")
win.title('Event Registration')

lable1 = Label(win,text="REGISTRATION FORM")
lable1.pack()

lable2 = Label(win,text="First name:")
lable2.place(x=50,y=20)
fname = Entry(win,width=30)
fname.place(x=200,y=20)

lable3 = Label(win,text="Last name:")
lable3.place(x=500,y=20)
lname = Entry(win,width=30)
lname.place(x=600,y=20)

lable4 = Label(win,text="Mobile number:")
lable4.place(x=50,y=50)
mb = Entry(win,width=30)
mb.place(x=200,y=50)

lable5 = Label(win,text="Email id:")
lable5.place(x=500,y=50)
email = Entry(win,width=30)
email.place(x=600,y=50)

gender = IntVar()
label6 = Label(win,text="Gender:")
label6.place(x=50,y=80)

male_gender = Radiobutton(win,text='Male',value=1,variable=gender)
male_gender.place(x=200,y=80)
female_gender = Radiobutton(win,text='Female',value=2,variable=gender) 
female_gender.place(x=250,y=80)
other_gender = Radiobutton(win,text='Other',value=3,variable=gender)
other_gender.place(x=320,y=80)

lable7 = Label(win,text="Age:")
lable7.place(x=500,y=80)
age = Entry(win,width=30)
age.place(x=600,y=80)

lable3 = Label(win,text="Category of Event:")
lable3.place(x=50,y=110)
event = Entry(win,width=30)
event.place(x=200,y=110)

lable3 = Label(win,text="Select Event:")
lable3.place(x=500,y=110)
event = Entry(win,width=30)
event.place(x=600,y=110)

agree = IntVar()
agree_button = Checkbutton(win,text="I agree with terms and condition",variable=agree,onvalue=1,offvalue=0)
agree_button.place(x=300,y=140)


register_button = Button(win, text='Register', width=20, fg='white', bg='green', )
register_button.place(x=200,y=170)
reset_button = Button(win, text='Reset', width=20, fg='white', bg='red', )
reset_button.place(x=600,y=170)

today = datetime.today()
f_today = today.strftime("%c %p")
today_lable = Label(win,text=f_today)
today_lable.place(x=100,y=200)

reset_button = Button(win, text='View Entry', width=20, fg='black', bg='brown', )
reset_button.place(x=600,y=230)

reset_button = Button(win, text='hello', width=20, fg='black', bg='brown', )
reset_button.place(x=600,y=260)

# photo = PhotoImage(file="sunflowers.png")
# lable = Label(win,image=photo)
# lable.pack()


win.mainloop()