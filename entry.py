from Tkinter import *


master = Tk()


master.minsize(500,400)
master.maxsize(500,400)
# photo=PhotoImage(file="qabas.png")
# lable=Label(master, image=photo)
# lable.pack()
#
# master.mainloop()



#texbox ve button ekleme
e = Entry(master, width=50)
e.pack()


def callback():
    top = Toplevel()
    print e.get()

b = Button(master, text="get", width=10, command=callback)
b.pack()
#texbox ve button ekleme



#secenekler ekleme
var = StringVar(master)
var.set("one") # initial value

option = OptionMenu(master, var, "one", "two", "three", "four")

option.place(x=60, y=30)

#secenekler ekleme

#secilen vereyi elde etme
def ok():
    print "value is", var.get()

#secilen vereyi elde etme

button = Button(master, text="OK", command=ok)
button.pack()



mainloop()





