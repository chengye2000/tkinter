import tkinter
# 添加测试
#添加了帐号
#commit之后要push
#在本机进行测试
app=tkinter.Tk()
app.title("hello,tkinter")
thelabel=tkinter.Label(app,text="label.txt",fg="blue",bg="red")
thebutton=tkinter.Button(app,text="thebutton",fg="blue",bg="red")
thebutton.pack(padx=10,pady=10)
thelabel.pack(padx=10,pady=10)
app.mainloop()