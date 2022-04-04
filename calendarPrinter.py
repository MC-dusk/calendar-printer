# 日历打印器 v3.1
# calendar printer v3.1

# 本地时间

import time

def getTime():
    localtime = time.strftime("%Z %Y-%m-%d %A %H:%M:%S", time.localtime())
    return localtime

# 文件输出

import calendar

def saveFile():
    try:
        if type(eval(et.get())) == int:
            year = int(et.get())
            file = open(str(year) + ".txt", "w")
            file.write(calendar.calendar(year,w=3,l=1,c=6) + '\n')
            printTime = getTime()
            file.write(u'打印时间：' + printTime)
            file.close()
            mb.showinfo('提示','输出成功！',icon = mb.INFO)
    except:
        et.delete(0,'end')
        mb.showerror('提示','请正确输入！',icon = mb.ERROR)

# GUI界面

import tkinter as tk
from tkinter import messagebox as mb

def gui(root):
    fr = tk.Frame(root, relief='groove')
    fr.place(relx=0.5, rely=0.5, anchor='center')

    lb = tk.Label(fr, text = "日历打印器\n\n请输入要打印的年份：", bd=20, font=(20), fg="red", bg="yellow")
    lb.grid(row=0,column=0,columnspan=2)

    global et
    et = tk.Entry(fr)
    et.insert(0,time.strftime('%Y'))
    et.grid(row=1,column=0,columnspan=2)

    bt = tk.Button(fr, text = "保存到当前目录", command = saveFile)
    bt.grid(row=3,column=0)

    quit = tk.Button(fr, text = "退出", command = root.quit)
    quit.grid(row=3,column=1)

def main():
    root = tk.Tk()
    root.title("日历打印器 v3.0")
    # root.iconbitmap(".\\\calendar.ico")
    root.geometry('320x180+200+200')
    gui(root)
    root.mainloop()

main()
