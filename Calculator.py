from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())
        
        scvalue.set(value)
        screen.update()

    elif text == "AC":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()
root.geometry("650x950")
root.title("Calculator")
root.resizable(False, False)
# root.wm_iconbitmap("1.ico")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 40 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)



frame = Frame(root, bg="grey")
button = Button(frame, text="AC", padx=19, pady=18, font="lucid 30 bold")
button.pack(side=LEFT, padx=18, pady=5)
button.bind("<Button-1>", click)

button = Button(frame, text="=", padx=28, pady=17, font="lucid 35 bold")
button.pack(side=LEFT, padx=18, pady=5)
button.bind("<Button-1>", click)

button = Button(frame, text="%", padx=23, pady=17, font="lucid 33 bold")
button.pack(side=LEFT, padx=18, pady=5)
button.bind("<Button-1>", click)

button = Button(frame, text="/", padx=28, pady=17, font="lucid 35 bold")
button.pack(side=LEFT, padx=18, pady=5)
button.bind("<Button-1>", click)

frame.pack()

frame = Frame(root, bg="grey")
button = Button(frame, text="9", padx=28, pady=18, font="lucid 35 bold")
button.pack(side=LEFT, padx=18, pady=5)
button.bind("<Button-1>", click)

button = Button(frame, text="8", padx=28, pady=18, font="lucid 35 bold")
button.pack(side=LEFT, padx=18, pady=5)
button.bind("<Button-1>", click)

button = Button(frame, text="7", padx=28, pady=18, font="lucid 35 bold")
button.pack(side=LEFT, padx=18, pady=5)
button.bind("<Button-1>", click)

button = Button(frame, text="*", padx=28, pady=18, font="lucid 35 bold")
button.pack(side=LEFT, padx=18, pady=5)
button.bind("<Button-1>", click)

frame.pack()

frame = Frame(root, bg="grey")
button = Button(frame, text="6", padx=28, pady=18, font="lucid 35 bold")
button.pack(side=LEFT, padx=18, pady=5)
button.bind("<Button-1>", click)

button = Button(frame, text="5", padx=28, pady=18, font="lucid 35 bold")
button.pack(side=LEFT, padx=18, pady=5)
button.bind("<Button-1>", click)

button = Button(frame, text="4", padx=28, pady=18, font="lucid 35 bold")
button.pack(side=LEFT, padx=18, pady=5)
button.bind("<Button-1>", click)

button = Button(frame, text="-", padx=28, pady=18, font="lucid 36 bold")
button.pack(side=LEFT, padx=18, pady=5)
button.bind("<Button-1>", click)

frame.pack()

frame = Frame(root, bg="grey")
button = Button(frame, text="3", padx=26, pady=18, font="lucid 36 bold")
button.pack(side=LEFT, padx=18, pady=5)
button.bind("<Button-1>", click)

button = Button(frame, text="2", padx=27, pady=18, font="lucid 37 bold")
button.pack(side=LEFT, padx=18, pady=5)
button.bind("<Button-1>", click)

button = Button(frame, text="1", padx=27, pady=18, font="lucid 37 bold")
button.pack(side=LEFT, padx=18, pady=5)
button.bind("<Button-1>", click)

button = Button(frame, text="+", padx=25, pady=18, font="lucid 34 bold")
button.pack(side=LEFT, padx=18, pady=5)
button.bind("<Button-1>", click)

frame.pack()

frame = Frame(root, bg="grey")
button = Button(frame, text="00", padx=20, pady=17, font="lucid 32 bold")
button.pack(side=LEFT, padx=18, pady=5)
button.bind("<Button-1>", click)

button = Button(frame, text="0", padx=28, pady=18, font="lucid 36 bold")
button.pack(side=LEFT, padx=18, pady=5)
button.bind("<Button-1>", click)

button = Button(frame, text="(", padx=30, pady=18, font="lucid 36 bold")
button.pack(side=LEFT, padx=18, pady=5)
button.bind("<Button-1>", click)

button = Button(frame, text=")", padx=28, pady=18, font="lucid 36 bold")
button.pack(side=LEFT, padx=18, pady=5)
button.bind("<Button-1>", click)

frame.pack()

root.mainloop()