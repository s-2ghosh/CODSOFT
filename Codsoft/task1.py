import tkinter
from tkinter import *
root=Tk()
root.title("Calculator")
root.geometry("570x600+100+200")
root.configure(bg="#17161b")
equation=""
def display(val):
    global equation
    equation+=val
    lable_re.config(text=equation)
def clear():
    global equation
    equation=""
    lable_re.config(text=equation)
def calculate():
    global equation
    result=""
    if equation !="":
        try:
            result = eval(equation)
        except:
            result="error"
            equation=""
    lable_re.config(text=result)
lable_re=Label(root,width=50,height=4,text="",font=("arial,30"))
lable_re.pack()
Button(root,text="C",width=5,height=1,font=("arial",20,"bold"),bd=10,fg="#fff",bg="#3697f5",command=lambda:clear()).place(x=10,y=100)
Button(root,text="/",width=5,height=1,font=("arial",20,"bold"),bd=10,fg="#fff",bg="#2a2d36",command=lambda:display("/")).place(x=150,y=100)
Button(root,text="%",width=5,height=1,font=("arial",20,"bold"),bd=10,fg="#fff",bg="#2a2d36",command=lambda:display("%")).place(x=290,y=100)
Button(root,text="*",width=5,height=1,font=("arial",20,"bold"),bd=10,fg="#fff",bg="#2a2d36",command=lambda:display("*")).place(x=430,y=100)
Button(root,text="7",width=5,height=1,font=("arial",20,"bold"),bd=10,fg="#fff",bg="#2a2d36",command=lambda:display("7")).place(x=10,y=200)
Button(root,text="8",width=5,height=1,font=("arial",20,"bold"),bd=10,fg="#fff",bg="#2a2d36",command=lambda:display("8")).place(x=150,y=200)
Button(root,text="9",width=5,height=1,font=("arial",20,"bold"),bd=10,fg="#fff",bg="#2a2d36",command=lambda:display("9")).place(x=290,y=200)
Button(root,text="-",width=5,height=1,font=("arial",20,"bold"),bd=10,fg="#fff",bg="#2a2d36",command=lambda:display("-")).place(x=430,y=200)
Button(root,text="4",width=5,height=1,font=("arial",20,"bold"),bd=10,fg="#fff",bg="#2a2d36",command=lambda:display("4")).place(x=10,y=300)
Button(root,text="5",width=5,height=1,font=("arial",20,"bold"),bd=10,fg="#fff",bg="#2a2d36",command=lambda:display("5")).place(x=150,y=300)
Button(root,text="6",width=5,height=1,font=("arial",20,"bold"),bd=10,fg="#fff",bg="#2a2d36",command=lambda:display("6")).place(x=290,y=300)
Button(root,text="+",width=5,height=1,font=("arial",20,"bold"),bd=10,fg="#fff",bg="#2a2d36",command=lambda:display("+")).place(x=430,y=300)
Button(root,text="1",width=5,height=1,font=("arial",20,"bold"),bd=10,fg="#fff",bg="#2a2d36",command=lambda:display("1")).place(x=10,y=400)
Button(root,text="2",width=5,height=1,font=("arial",20,"bold"),bd=10,fg="#fff",bg="#2a2d36",command=lambda:display("2")).place(x=150,y=400)
Button(root,text="3",width=5,height=1,font=("arial",20,"bold"),bd=10,fg="#fff",bg="#2a2d36",command=lambda:display("3")).place(x=290,y=400)
Button(root,text="0",width=14,height=1,font=("arial",20,"bold"),bd=10,fg="#fff",bg="#2a2d36",command=lambda:display("0")).place(x=10,y=500)
Button(root,text=".",width=5,height=1,font=("arial",20,"bold"),bd=10,fg="#fff",bg="#2a2d36",command=lambda:display(".")).place(x=290,y=500)
Button(root,text="-",width=6,height=5,font=("arial",20,"bold"),bd=10,fg="#fff",bg="#fe9037",command=lambda:calculate()).place(x=430,y=400)
root.mainloop()