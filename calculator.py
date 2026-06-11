from tkinter import *

def click(value):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(END, current + str(value))

def clear():
    entry.delete(0, END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(END, str(result))
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")

root = Tk()
root.title("CSC426 Calculator")
root.geometry("350x450")

entry = Entry(root, font=("Arial", 20), bd=10, justify="right")
entry.pack(fill=BOTH, padx=10, pady=10)

buttons = [
    ['7','8','9','/'],
    ['4','5','6','*'],
    ['1','2','3','-'],
    ['0','%','^','+']
]

for row in buttons:
    frame = Frame(root)
    frame.pack(expand=True, fill="both")

    for btn in row:
        Button(
            frame,
            text=btn,
            font=("Arial",18),
            command=lambda b=btn: click("**" if b=="^" else b)
        ).pack(side=LEFT, expand=True, fill="both")

Frame(root).pack(expand=True, fill="both")

Button(root,text="C",font=("Arial",18),
       command=clear).pack(fill="both")

Button(root,text="=",font=("Arial",18),
       command=calculate).pack(fill="both")

root.mainloop()
