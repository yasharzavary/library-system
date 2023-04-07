from tkinter import *
from tkinter import messagebox
from mysql.connector import Connect, Error
import re

shown=1
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
# delete key button change color functions
def decchangecolor(event):
    deletekey.config(bg="#DCDCDC")

def dlchangekey(event):
    deletekey.config(bg="#ffffff")
# -----------------------------------------
# find key button change color functions
def fecchangecolor(event):
    findkey.config(bg="#DCDCDC")

def flchangekey(event):
    findkey.config(bg="#ffffff")
# -----------------------------------------
# show key button change color functions
def secchangecolor(event):
    showkey.config(bg="#DCDCDC")

def slchangekey(event):
    showkey.config(bg="#ffffff")
# my new book function
def pushkey(event):
    def errorhapend(message):
        messagebox.showerror("Error", message)
        return False      
    def controlAndAdd(event):
        nameOfTheBook=nameentry.get()
        gnum=gentry.get()
        wname=writerentry.get()
        winfo=winfoentry.get()
        global newbookid, done
        def control():
            if nameOfTheBook=="" or gnum=="" or wname=="" or winfo=="":
                return errorhapend("slots can't be empty")
            elif re.search(r"[0-9]",wname):
                return errorhapend("writer name can't have numbers")    
            elif re.search(r"[^0-9]",gnum):
                return errorhapend("guide number only can have numbers")
            with Connect(user="root", password="Yasharzavary360", host="127.0.0.8", database="library") as conn:
                mysq=conn.cursor()
                mysq.execute("select * from book")
                for i in mysq.fetchall():
                    if i[1]==gnum:
                        return errorhapend("guide number can't be same")
                    elif i[2]==nameOfTheBook and i[3]==wname and i[4]==winfo:
                        return errorhapend("we have that book")
                conn.commit()
            return True
           
        if control() == True:
            try:
                with Connect(user="root", password="Yasharzavary360", host="127.0.0.8", database="library") as conn:
                    mysq=conn.cursor()
                    mysq.execute("select max(record_id) from book")
                    for i in mysq:
                        if i[0]!=None:
                            newbook=i[0]+1
                        else:
                            newbook=1
                    mysq.execute("""insert into book(record_id, guidenum, booksubject, writername, writerinfo)
                                    values(%s,%s,%s,%s,%s)""",(newbook,int(gentry.get()),nameentry.get(),writerentry.get(),winfoentry.get()))
                    conn.commit()
                messagebox.showinfo("👁‍🗨","book added succesfully")
            except Error as err:
                print(err)
                
    addroot=Tk()
    addroot.title("add new book")
    addroot.iconbitmap("newbook.ico")
    addroot.geometry("%dx%d+%d+%d"%(400,200,x+300,y))
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
         
    # mine ok button that send our information to adding to database
    okbutton=Button(master=addroot,text="OK",fg="#000000",font=("Tahoma",10))
    okbutton.grid(row=5,column=0)
    
    # my control and add part
    okbutton.bind("<Button>", controlAndAdd)

    addroot.mainloop()
# delete one book
def delete_book(event):
    # delete with book id
    def delwithid():
        def delbook():
            wehave=False
            bid=int(identery.get())
            try:
                with Connect(user="root", password="Yasharzavary360", host="127.0.0.8", database="library") as conn:
                    mysq=conn.cursor()
                    mysq.execute("select * from book")
                    for i in mysq.fetchall():
                        if bid==i[0]:
                            wehave=True
                            mysq.execute("delete from book where record_id="+str(bid))       
                    conn.commit()
                if wehave:
                    messagebox.showinfo("ok!","book deleted")
                else:
                    messagebox.showerror("error","we don't have such book")
            except Error as err:
                print(err)
                
        delidroot=Tk()
        delidroot.geometry("%dx%d+%d+%d"%(250,150,100,500))
        delidlabel=Label(master=delidroot,text="record id:")
        delidlabel.grid(row=0,column=0,padx=10,pady=10)
        
        identery=Entry(master=delidroot)
        identery.grid(row=0,column=1)
        
        delokbutton=Button(master=delidroot,text="delete",command=delbook)
        delokbutton.grid(row=1,column=0)
        
        delidroot.mainloop()
    def searchanddelete():
        pass
    optionroot=Tk()
    optionroot.title("delete book")
    optionroot.iconbitmap("delete.ico")
    optionroot.geometry("%dx%d"%(400,100))
    havebutton=Button(master=optionroot,text="delete with record id",fg="#000000",command=delwithid)
    havebutton.grid(row=1,column=1,padx=50,pady=30)
    
    donothave=Button(master=optionroot,text="search by name and delete",fg="#000000",command=searchanddelete)
    donothave.grid(row=1,column=2)
    
    optionroot.mainloop()
# find with id
def findwithid(event):
    def finding():
        ifind=True
        bid=int(identery.get())
        with Connect(user="root", password="Yasharzavary360", host="127.0.0.8", database="library") as conn:
                mysq=conn.cursor()
                mysq.execute("select * from book")
                for i in mysq.fetchall():
                    if i[0]==bid:
                        ifind=False
                        messagebox.showinfo("result",f"id:{i[0]}\tguidenum:{i[1]}\tbooksubject:{i[2]}\twritername:{i[3]}//writerinfo:{i[4]}")
                conn.commit()
        if ifind:
            messagebox.showerror("result","we don't have such book")
    findroot=Tk()
    findroot.title("find with id")
    findroot.iconbitmap("find.ico")
    findroot.geometry("%dx%d"%(200,100))
    flabel=Label(master=findroot,text="id for search: ")
    flabel.grid(row=0,column=0)
    identery=Entry(master=findroot)
    identery.grid(row=0,column=1)
    findbutton=Button(master=findroot,text="find",command=finding)
    findbutton.grid(row=1,column=0)
    
    findroot.mainloop()
# show all books
def showbooks(event):
    def show(bid,gname,name,wname,winfo):
        global shown
        templabel=Label(master=showroot,text=f"id:{bid} / gnumber:{gname} / name:{name} / writer:{wname} / info:{winfo}")
        templabel.grid(row=shown,column=0)
        shown+=1
    showroot=Tk()
    showroot.title("all books")
    showroot.iconbitmap("show.ico")
    showroot.geometry("%dx%d+%d+%d"%(500,100,500,100))
    with Connect(host="127.0.0.8",user="root",password="Yasharzavary360",database="library") as conn:
        mysq=conn.cursor()
        mysq.execute("select * from book")
        for i in mysq.fetchall():
            show(i[0],i[1],i[2],i[3],i[4])     
        conn.commit()
    showroot.mainloop()

# my add key
addkey=Button(master=mainroot, text="new book", fg="#000000", bg="#ffffff",width=10,cursor="plus")
addkey.bind("<Enter>",ecchangecolor)
addkey.bind("<Leave>",lchangekey)
addkey.bind("<Button>",pushkey)
addkey.grid(row=1,column=0, padx=100)

# my delete key
deletekey=Button(master=mainroot, text="delete book", fg="#000000", bg="#ffffff",width=10,cursor="pirate")
deletekey.bind("<Enter>",decchangecolor)
deletekey.bind("<Leave>",dlchangekey)
deletekey.bind("<Button>",delete_book)
deletekey.grid(row=2,column=0,padx=100)

# my fing key
findkey=Button(master=mainroot, text="find with id",fg="#000000", bg="#ffffff",width=10,cursor="target")
findkey.bind("<Enter>",fecchangecolor)
findkey.bind("<Leave>",flchangekey)
findkey.bind("<Button>",findwithid)
findkey.grid(row=3,column=0,padx=100)


# show all book key
showkey=Button(master=mainroot, text="show books",fg="#000000",bg="#ffffff",width=10,cursor="dotbox")
showkey.bind("<Enter>",secchangecolor)
showkey.bind("<Leave>",slchangekey)
showkey.bind("<Button>",showbooks)
showkey.grid(row=4,column=0,padx=100)


mainroot.mainloop()


