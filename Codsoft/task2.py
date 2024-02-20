from tkinter import *
import random ,string
root=Tk()
root.geometry("679x500")
root.maxsize(679,500)
root.minsize(679,500)
root.configure(bg="#94eb8f")
root.title("Password generator")
label=Label(root,width=50,height=2,text="PASSWORD GENERATOR",font=("times new roman",25),bg="#073306",fg="white").pack()
label1=Label(root,text="Strength of the password",font=("times new roman",20,"bold"),bg="#94eb8f",fg="#301408").pack()

def section():
    section=choice.get()
choice=IntVar()
r1=Radiobutton(root,text="Poor",variable=choice,value=1,command=section,bg="#94eb8f",font=("times new roman",15)).pack(anchor=CENTER)
r2=Radiobutton(root,text="Average",variable=choice,value=2,command=section,bg="#94eb8f",font=("times new roman",15)).pack(anchor=CENTER)
r1=Radiobutton(root,text="Strong",variable=choice,value=3,command=section,bg="#94eb8f",font=("times new roman",15)).pack(anchor=CENTER)
labelchoice=Label(root,bg="#94eb8f")
labelchoice.pack()

lenlabel=StringVar()
lenlabel.set("Password length")
lentitle=Label(root,textvariable=lenlabel,bg="#94eb8f",font=("times new roman",15)).pack()
val=IntVar()
spinlenght=Spinbox(root,from_=8,to_=24,textvariable=val,width=13,font=("times new roman",15)).pack()

def callback():
    lsum.config(text="Password :: "+passgen(),bg="#94eb8f",font=("times new roman",15))

passgenButton=Label(root,text="",bg="#94eb8f")
passgenButton.pack()
passgenButton=Button(root,text="Genrate Password",bd=5,height=2,command=callback,pady=3,bg="#d14924")
passgenButton.pack()
l=Label(root,text="",bg="#94eb8f")

password=str(callback)
lsum=Label(root,text="",bg="#94eb8f")
lsum.pack()

poor=string.ascii_uppercase+string.ascii_lowercase
average=string.ascii_uppercase+string.ascii_lowercase+string.digits
symbols="""`~!@#$%^&*()_++{}[]|\:;"'<>,.?/"""
advance=poor+average+symbols
def passgen():
    if choice.get()==1:
        return "".join(random.sample(poor,val.get()))
    elif choice.get()==2:
        return "".join(random.sample(average,val.get()))
    elif choice.get()==3:
        return "".join(random.sample(advance,val.get()))



root.mainloop()
