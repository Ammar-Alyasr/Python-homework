from tkinter import *
top = Tk()





def kaydir():
    c = Canvas(top, bg="white", height=500, width=500)
    global x,y
    x = 250
    y = 250
    c.create_oval(x - 50, y - 50, x + 20, y + 20, width=2, fill='black')
    c.pack()

def solakaydir():
    if sol:
       for i in range(0,-500):
        i-=1
        print(i)

    elif sag:
        for e in range(0, 500):
            e +=1
            print(e)
    elif asagi:
        for a in range(0,-500):
            a -=1
            print(a)
    else:
        for u in range(0, 500):
            u+=1
            print(u)


sol = Button(top, text="SOL", width=10, command=solakaydir)
sol.pack(padx=20, pady=50, side=LEFT)
sag = Button(top, text="SAG", width=10)
sag.pack(padx=20, pady=50, side=RIGHT)

asagi = Button(top, text="ASAGI", width=10)
asagi.pack(padx=20, pady=50, side=BOTTOM)

yukari = Button(top, text="YUKARI", width=10)
yukari.pack(padx=20, pady=50, side=TOP)



kaydir()
top.mainloop()