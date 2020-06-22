from tkinter import *
from tkinter.messagebox import *
import math as m
root = Tk()
root.geometry("260x250")
root.title("Calculator")


def clear():
    ex=input.get()
    ex=ex[0:len(ex)-1]
    input.delete(0,END)
    input.insert(0,ex)


def Scintific_click(event):
    print("clicked")
    b1=event.widget
    text1=b1['text']
    print(text1)
    ex=input.get()
    answer=""
    if text1=="sqrt":
        print("square root")
        answer= m.sqrt(int(ex))
    elif text1=="deg":
        print("call degree")
        answer= m.degrees(float(ex))
    elif text1=="rad":
        print("call radian")
        answer=m.radians(float(ex))
    elif text1=="sin":
        print("call sin")
        answer=m.sin(m.radians(int(ex)))
    elif text1=="cos":
        print("call cos")
        answer=m.cos(m.radians(int(ex)))
    elif text1=="tan":
        print("call tan")
        answer=m.tan(m.radians(int(ex)))
    elif text1=="X!":
        print("call fact")
        answer=str(m.factorial(int(ex)))
    elif text1=="pow":
     print("call pow")
     base,pow=ex.split("^")
     answer=str(m.pow(int(base),int(pow)))

    input.delete(0,END)
    input.insert(0,answer)

def all_clear():
    input.delete(0,END)


def button_click(event):
    print("btn clicked")
    b=event.widget
    text=b['text']
    print(text)

    if text == "=":
        try:

            ex =input.get()
            answer=eval(ex)
            input.delete(0,END)
            input.insert(0,answer)
        except Exception as e:
            print("ERROR...",e)
            showerror("ERROR",e)

        return
    input.insert(END,text)


input=Entry(root,justify=CENTER,font="BellMT")
input.pack(side=TOP,fill=X,padx=5,pady=25)

# normal calc coding


p1 = PhotoImage(file="calculator.png")
root.iconphoto(False, p1)

buttonframe=Frame(root)
buttonframe.pack(side=TOP)
temp=1
for i in range(3):
    for j in range(3):
        btn = Button(buttonframe,text=temp,font="BellMT",width=5,relief="ridge",activebackground="orange",activeforeground="white")
        btn.grid(row=i,column=j)
        temp += 1
        btn.bind('<Button-1>',button_click)
zero=Button(buttonframe,text="0",font="BellMT",width=5,relief="ridge",activebackground="orange",activeforeground="white")
zero.grid(row=4,column=0)
point=Button(buttonframe,text=".",font="BellMT",width=5,relief="ridge",activebackground="orange",activeforeground="white")
point.grid(row=4,column=1)
equals= Button(buttonframe,text="=",font="BellMT",width=5,relief="ridge",activebackground="orange",activeforeground="white")
equals.grid(row=4,column=2,)
add = Button(buttonframe, text="+", font="BellMT", width=5, relief="ridge", activebackground="orange",activeforeground="white")
add.grid(row=0, column=3)
subtract = Button(buttonframe, text="-", font="BellMT", width=5, relief="ridge", activebackground="orange",activeforeground="white")
subtract.grid(row=1, column=3)
multiply = Button(buttonframe, text="*", font="BellMT", width=5, relief="ridge", activebackground="orange",activeforeground="white")
multiply.grid(row=2, column=3)
division = Button(buttonframe, text="/", font="BellMT", width=5, relief="ridge", activebackground="orange",activeforeground="white")
division.grid(row=4, column=3)
clear = Button(buttonframe, text="CLR", font="BellMT", width=11, relief="ridge", activebackground="orange",activeforeground="white",command=clear)
clear.grid(row=5,column=0,columnspan=2)
allclear = Button(buttonframe, text="AC", font="BellMT", width=11, relief="ridge", activebackground="orange",activeforeground="white",command=all_clear)
allclear.grid(row=5,column=2,columnspan=2)

zero.bind('<Button-1>',button_click)
point.bind('<Button-1>',button_click)
equals.bind('<Button-1>',button_click)
add.bind('<Button-1>',button_click)
subtract.bind('<Button-1>',button_click)
division.bind('<Button-1>',button_click)
multiply.bind('<Button-1>',button_click)


def enterclick(event):
    e=Event
    e.widget=equals
    button_click(e)


input.bind('<Return>',enterclick)


# Scintific calc coding

scframe=Frame(root)
sqrt = Button(scframe, text="sqrt", font="BellMT", width=5, relief="ridge", activebackground="orange",activeforeground="white",command=clear)
sqrt.grid(row=1,column=0)
deg = Button(scframe, text="deg", font="BellMT", width=5, relief="ridge", activebackground="orange",activeforeground="white",command=clear)
deg.grid(row=1,column=1)
rad = Button(scframe, text="rad", font="BellMT", width=5, relief="ridge", activebackground="orange",activeforeground="white",command=clear)
rad.grid(row=1,column=2)
cos = Button(scframe, text="cos", font="BellMT", width=5, relief="ridge", activebackground="orange",activeforeground="white",command=clear)
cos.grid(row=1,column=3)
sin = Button(scframe, text="sin", font="BellMT", width=5, relief="ridge", activebackground="orange",activeforeground="white",command=clear)
sin.grid(row=2,column=0)
tan = Button(scframe, text="tan", font="BellMT", width=5, relief="ridge", activebackground="orange",activeforeground="white",command=clear)
tan.grid(row=2,column=1)
pow = Button(scframe, text="pow", font="BellMT", width=5, relief="ridge", activebackground="orange",activeforeground="white",command=clear)
pow.grid(row=2,column=2)
fact = Button(scframe, text="X!", font="BellMT", width=5, relief="ridge", activebackground="orange",activeforeground="white",command=clear)
fact.grid(row=2,column=3)




normalcalc = True
def sc():
    global normalcalc
    if normalcalc:
        buttonframe.pack_forget()
        scframe.pack()
        buttonframe.pack()
        print("sc")
        normalcalc=False
        root.geometry("260x310")
    else:
        print("Normal Calc")
        scframe.pack_forget()
        normalcalc=True
        root.geometry("260x250")



menubar = Menu(root)
root.config(menu=menubar)
mode=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Mode",menu=mode)
mode.add_checkbutton(label="Scintific Calculator",command=sc)


sqrt.bind('<Button-1>',Scintific_click)
deg.bind('<Button-1>',Scintific_click)
rad.bind('<Button-1>',Scintific_click)
sin.bind('<Button-1>',Scintific_click)
cos.bind('<Button-1>',Scintific_click)
tan.bind('<Button-1>',Scintific_click)
pow.bind('<Button-1>',Scintific_click)
fact.bind('<Button-1>',Scintific_click)

root.mainloop()