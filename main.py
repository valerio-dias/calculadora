from tkinter import *
from calculadora import Calculadora

tk = Tk()
tk.title("Calculadora")
tk['bg'] = '#A8DADC'
tk.geometry("280x360+0+0")
tk.resizable(False, False)
tk.iconbitmap("images/icon.ico")

bt1 = Button(tk, text="1", bg="#A8DADC", font=("Arial", 12, "bold"), padx=10, pady=10, bd=2)
bt1.place(x=10, y=100)


tk.mainloop()


    