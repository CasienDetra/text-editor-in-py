import sys

try:
    from tkinter import *
    import tkinter.filedialog as tkFileDialog
except ImportError:
    from Tkinter import *
    import tkFileDialog


root = Tk("Text Editor")
root.title("Simple Editor Text")
text = Text(root)
text.grid()


def saveas():
    global text
    t = text.get("1.0", "end-1c")
    savelocation = tkFileDialog.asksaveasfilename()
    file1 = open(savelocation, "w+")
    file1.write(t)
    file1.close()


button = Button(root, text="Save", command=saveas)
button.grid()


def FontHelvetica():
    global text
    text.config(font="Helvetica")


def FontCourier():
    global text
    text.config(font="Courier")


font = Menubutton(root, text="Font", relief=RAISED)
font.grid()
font.menu = Menu(font, tearoff=0)
font.configure(menu=font.menu)

Helvetica = IntVar()
arial = IntVar()
times = IntVar()
Courier = IntVar()

font.menu.add_checkbutton(label="Courier", variable=Courier, command=FontCourier)

root.mainloop()

