import tkinter as tk
from tkinter import messagebox

top = tk.Tk()

def helloCallBack():
    messagebox.askretrycancel("Failed!", "Try again")

B = tk.Button(top, text="Click", command=helloCallBack)
B.pack()

top.mainloop()

