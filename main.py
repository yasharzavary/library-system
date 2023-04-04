from tkinter import *
from tkinter import messagebox
from mysql.connector import Connect, Error

newbookid=0

# my main root
mainroot=Tk()
mainroot.resizable(width=0,height=0)
mainroot.title("library")
mainroot.iconbitmap("mainroot.ico")


w=300
h=300
sw=mainroot.winfo_screenwidth()
sh=mainroot.winfo_screenheight()
x=(sw/2)-(w/2)
y=(sh/2)-(h/2)
mainroot.geometry("%dx%d+%d+%d"%(w,h,x,y))


# welcome message
wellcomelabel=Label(master=mainroot, text="wellcome:",fg="#000000",font=("Tahoma",10))  
wellcomelabel.grid(row=0,column=0,padx=100) 

# add key buttonchange color functions
def ecchangecolor(event):
    addkey.config(bg="#DCDCDC")

def lchangekey(event):
    addkey.config(bg="#ffffff")
    
# -----------------------------------------

# my new book function
def pushkey(event):
    global newbookid
    addroot=Tk()
    addroot.title("add new book")
    addroot.iconbitmap("newbook.ico")
    addroot.geometry("%dx%d+%d+%d"%(400,400,x+300,y))
    # welcome message for new book part
    welcomelabel=Label(master=addroot, text="please fill info for add new book",font=("Tahoma",10)) 
    welcomelabel.grid(row=0, column=0)
    
    # get info of new book
    namelabel=Label(master=addroot, text="name of the book:",fg="#0000FF",font=("Tahoma",10))
    namelabel.grid(row=1,column=0)
    nameentry=Entry(master=addroot)
    nameentry.grid(row=1,column=1)
    
    glabel=Label(master=addroot, text="guide number:",fg="#0000FF",font=("Tahoma",10))
    glabel.grid(row=2,column=0)
    gentry=Entry(master=addroot)
    gentry.grid(row=2,column=1)
    
    writerlabel=Label(master=addroot, text="writer name:",fg="#0000FF",font=("Tahoma",10))
    writerlabel.grid(row=3,column=0)
    writerentry=Entry(master=addroot)
    writerentry.grid(row=3,column=1)
    
    winfolabel=Label(master=addroot, text="writerinfo:",fg="#0000FF",font=("Tahoma",10))
    winfolabel.grid(row=4,column=0)
    winfoentry=Entry(master=addroot)  
    winfoentry .grid(row=4,column=1) 
         
    okbutton=Button(master=addroot,text="OK",fg="#000000",font=("Tahoma",10))
    okbutton.grid(row=5,column=0)
    addroot.mainloop()

# my add key
addkey=Button(master=mainroot, text="new book", fg="#000000", bg="#ffffff",width=10,cursor="plus")
addkey.bind("<Enter>",ecchangecolor)
addkey.bind("<Leave>",lchangekey)
addkey.bind("<Button>",pushkey)
addkey.grid(row=1,column=0, padx=100)


mainroot.mainloop()



