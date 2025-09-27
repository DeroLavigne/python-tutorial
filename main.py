import tkinter as tk

def add():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        result_label.config(text=str(a + b))
    except ValueError:
        result_label.config(text="Invalid input")

def subtract():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        result_label.config(text=str(a - b))
    except ValueError:
        result_label.config(text="Invalid input")

def multiply():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        result_label.config(text=str(a * b))
    except ValueError:
        result_label.config(text="Invalid input")

def divide():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        if b == 0:
            result_label.config(text="Cannot divide by zero")
        else:
            result_label.config(text=str(a / b))
    except ValueError:
        result_label.config(text="Invalid input")

root = tk.Tk()
root.title("Simple Calculator")

tk.Label(root, text="Number 1:").grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Number 2:").grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

tk.Button(root, text="+", command=add).grid(row=2, column=0)
tk.Button(root, text="-", command=subtract).grid(row=2, column=1)
tk.Button(root, text="*", command=multiply).grid(row=3, column=0)
tk.Button(root, text="/", command=divide).grid(row=3, column=1)

result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()
