from tkinter import *
from calculadora import Calculadora

tk = Tk()
tk.title("Calculadora")
tk['bg'] = '#BBBBBB'
tk.geometry("220x324+0+0")
tk.resizable(False, False)
tk.iconbitmap("images/icon.ico")

bt1 = Button(tk, text="7", bg="#000000",fg = "white", font=("Arial", 12, "bold"), padx=10, pady=10, bd=2)
bt1.place(x=10, y=100)

bt1 = Button(tk, text="8", bg="#000000",fg = "white", font=("Arial", 12, "bold"), padx=10, pady=10, bd=2)
bt1.place(x=60, y=100)

bt1 = Button(tk, text="9", bg="#000000",fg = "white", font=("Arial", 12, "bold"), padx=10, pady=10, bd=2)
bt1.place(x=110, y=100)

bt1 = Button(tk, text="*", bg="#000000",fg = "white", font=("Arial", 12, "bold"), padx=10, pady=10, bd=2)
bt1.place(x=160, y=100)

bt1 = Button(tk, text="4", bg="#000000",fg = "white", font=("Arial", 12, "bold"), padx=10, pady=10, bd=2)
bt1.place(x=10, y=160)

bt1 = Button(tk, text="5", bg="#000000",fg = "white", font=("Arial", 12, "bold"), padx=10, pady=10, bd=2)
bt1.place(x=60, y=160)

bt1 = Button(tk, text="6", bg="#000000",fg = "white", font=("Arial", 12, "bold"), padx=10, pady=10, bd=2)
bt1.place(x=110, y=160)

bt1 = Button(tk, text="+", bg="#000000",fg = "white", font=("Arial", 12, "bold"), padx=10, pady=10, bd=2)
bt1.place(x=160, y=160)

bt1 = Button(tk, text="1", bg="#000000",fg = "white", font=("Arial", 12, "bold"), padx=10, pady=10, bd=2)
bt1.place(x=10, y=210)

bt1 = Button(tk, text="2", bg="#000000",fg = "white", font=("Arial", 12, "bold"), padx=10, pady=10, bd=2)
bt1.place(x=60, y=210)

bt1 = Button(tk, text="3", bg="#000000",fg = "white", font=("Arial", 12, "bold"), padx=10, pady=10, bd=2)
bt1.place(x=110, y=210)

bt1 = Button(tk, text="-", bg="#000000",fg = "white", font=("Arial", 12, "bold"), padx=10, pady=10, bd=2)
bt1.place(x=160, y=210)

bt1 = Button(tk, text="-", bg="#000000",fg = "white", font=("Arial", 12, "bold"), padx=10, pady=10, bd=2)
bt1.place(x=160, y=160)

bt1 = Button(tk, text="-", bg="#000000",fg = "white", font=("Arial", 12, "bold"), padx=10, pady=10, bd=2)
bt1.place(x=160, y=160)

bt1 = Button(tk, text="-", bg="#000000",fg = "white", font=("Arial", 12, "bold"), padx=10, pady=10, bd=2)
bt1.place(x=160, y=160)


tk.mainloop()


    