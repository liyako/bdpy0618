# encoding=UTF-8
import Tkinter
import tkFont


def callback1():
    label1.config(text='buy iphonejs max')


def callback2():
    label1.config(text='buy pixee4')


top = Tkinter.Tk()
var1 = Tkinter.IntVar()
var1.set(1)  # option initial value
myFont = tkFont.Font(family='Verdana', size=30)
myCFont = tkFont.Font(family='Microsoft YaHei UI', size=30)
label1 = Tkinter.Label(top, text="label1", font=myFont)
rb1 = Tkinter.Radiobutton(top, text='iOS', font=myCFont, value=1, variable=var1, command=callback1)
rb2 = Tkinter.Radiobutton(top, text='android', font=myCFont, value=2, variable=var1, command=callback2)
label1.pack()
rb1.pack()
rb2.pack()
top.minsize(400, 300)
top.mainloop()
