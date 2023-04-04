from tkinter import *
from tkinter import messagebox
from mysql.connector import Connect, Error

# my main root
mainroot=Tk()

w=300
h=300

sw=mainroot.winfo_screenwidth()
sh=mainroot.winfo_screenheight()

x=(sw/2)-(w/2)
y=(sh/2)-(h/2)

mainroot.geometry("%dx%d+%d+%d"%(w,h,x,y))


mainroot.mainloop()



