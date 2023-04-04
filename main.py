from tkinter import *
from tkinter import messagebox
from mysql.connector import Connect, Error

# my main root
mainroot=Tk()
mainroot.resizable(width=0,height=0)

w=300
h=300

sw=mainroot.winfo_screenwidth()
sh=mainroot.winfo_screenheight()

x=(sw/2)-(w/2)
y=(sh/2)-(h/2)

mainroot.geometry("%dx%d+%d+%d"%(w,h,x,y))


# add key button
def ecchangecolor(event):
    addkey.config(bg="#DCDCDC")

def lchangekey(event):
    addkey.config(bg="#ffffff")
    
def pushkey(event):
    pass
    
addkey=Button(master=mainroot, text="new book", fg="#000000", bg="#ffffff",width=10)
addkey.bind("<Enter>",ecchangecolor)
addkey.bind("<Leave>",lchangekey)
addkey.bind("<Button>",pushkey)
addkey.grid(row=0,column=0, padx=100)


mainroot.mainloop()



