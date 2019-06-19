#encoding=UTF-8
import Tkinter
import tkFont
top = Tkinter.Tk()
#模板
#print tkFont.families()
def callback1():
    print "button clicked!"
#按鈕函式
for f in tkFont.families():
    print f
print
#字型
myFont = tkFont.Font(family='Verdana', size=30)
myCFont = tkFont.Font(family='Microsoft YaHei UI', size=30)
label1 = Tkinter.Label(top, text="Hello world1", pady=30, bg='#C0FFEE', font=myFont)
label2 = Tkinter.Label(top, text="welcome", padx=30, bg='#FFEEC0', font=myFont)
label3 = Tkinter.Label(top, text='橫逸資訊', font=myCFont, fg='#990000', bg='#EEFFC0',
                       padx=20, pady=40)
#bg顏色  font字大小
button1 = Tkinter.Button(top, text='按鈕1', font=myCFont, bg='#000000', fg='#C0FFEE',
                         command=callback1)
label2.pack()
label1.pack()
label3.pack()
button1.pack()
top.mainloop()