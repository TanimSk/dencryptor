from tkinter import*
from tkinter import ttk
from tkinter import filedialog

win = Tk()

win.resizable(width=False, height=False)

win.title("DENCRYPTOR")
Label(win, text="navigate your file:").grid(row=0)

en = Entry(win, width=50, borderwidth=2)
en.grid(row=1, columnspan=3, pady=5, padx=5)


def browser():
    filename = filedialog.askopenfilename(initialdir='/', title="Select a File", filetypes=('All Files', '* .*'))
    en.insert(0, filename)


def encrypt():
    f = open(en.get(), "r")
    f1 = open("temp.de", "w")
    while 1:
        c = f.read(1)
        if not c:
            break
        f1.write(str(ord(c)+100))

    f = open(en.get(), "w")
    f1 = open("temp.de", "r")
    f.write(f1.read())


def decrypt():
    f1 = open("temp.de", "r")
    f = open(en.get(), "w")
    while 1:
        c = f1.read(3)
        if not c:
            break
        f.write(chr(int(c) - 100))


ttk.Button(win, text="Browse", command=browser).grid(row=2, column=0, padx=5)
ttk.Button(win, text="Encrypt", command=encrypt).grid(row=2, column=1, pady=5)
ttk.Button(win, text="Dencrypt", command=decrypt).grid(row=2, column=2, pady=5)


win.mainloop()
