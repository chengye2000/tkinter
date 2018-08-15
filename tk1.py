import tkinter

app=tkinter.Tk()
app.title("hello,tkinter")
thelabel=tkinter.Label(app,text="label.txt",fg="blue",bg="red")
thebutton=tkinter.Button(app,text="thebutton",fg="blue",bg="red")
thebutton.pack(padx=10,pady=10)
thelabel.pack(padx=10,pady=10)
app.mainloop()