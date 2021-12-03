from tkinter import *


tk = Tk()
tk.title("Calculadora")
tk['bg'] = '#BBBBBB'
tk.geometry("220x415+0+0")
tk.resizable(False, False)
tk.iconbitmap("images/icon.ico")

def btn_click(item):
    global valor

    valor = valor + str(item)

    input_valor.set(valor)


def btn_clear():
    global valor

    valor = ""

    input_valor.set("")


def btn_igual():
    global valor

    resultado = str(eval(valor)) 

    input_valor.set(resultado)


valor = " "

input_valor = StringVar()

input_frame = Frame(tk, width=210, height=85, bd=2, bg="lightgray", highlightbackground="black", highlightcolor="black",
                    highlightthickness=1, padx=10, pady=10)

input_frame.pack(side=TOP)

input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_valor, width=50, bg="#EEE", bd=0,
                    justify=RIGHT)

input_field.grid(row=0, column=0)

input_field.pack(ipady=10)  



clear = Button(tk, text="C", bg="#882222",fg = "white", width=11, height= 1, font=("Arial", 12, "bold"), padx=10, pady=10, bd=2, cursor="hand2",command=lambda: btn_clear())
clear.place(x=15, y=100)

divisao = Button(tk, text="/", bg="#000000",fg = "white", width=1, height= 1, font=("Arial", 12, "bold"), padx=10, pady=10, bd=2, cursor="hand2",command=lambda: btn_click("/"))
divisao.place(x=165, y=100)

sete = Button(tk, text="7", bg="#000000",fg = "white", width=1, height= 1, font=("Arial", 12, "bold"), padx=10, pady=10, bd=2, cursor="hand2",command=lambda: btn_click(7))
sete.place(x=15, y=160)

oito = Button(tk, text="8", bg="#000000",fg = "white", width=1, height= 1, font=("Arial", 12, "bold"), padx=10, pady=10, bd=2, cursor="hand2",command=lambda: btn_click(8))
oito.place(x=65, y=160)

nove = Button(tk, text="9", bg="#000000",fg = "white", width=1, height= 1, font=("Arial", 12, "bold"), padx=10, pady=10, bd=2, cursor="hand2",command=lambda: btn_click(9))
nove.place(x=115, y=160)

multiplicacao = Button(tk, text="*", bg="#000000",fg = "white", width=1, height= 1, font=("Arial", 12, "bold"), padx=10, pady=10, bd=2, cursor="hand2",command=lambda: btn_click("*"))
multiplicacao.place(x=165, y=160)

quatro = Button(tk, text="4", bg="#000000",fg = "white", width=1, height= 1, font=("Arial", 12, "bold"), padx=10, pady=10, bd=2, cursor="hand2",command=lambda: btn_click(4))
quatro.place(x=15, y=220)

cinco = Button(tk, text="5", bg="#000000",fg = "white", width=1, height= 1, font=("Arial", 12, "bold"), padx=10, pady=10, bd=2, cursor="hand2",command=lambda: btn_click(5))
cinco.place(x=65, y=220)

seis = Button(tk, text="6", bg="#000000",fg = "white", width=1, height= 1, font=("Arial", 12, "bold"), padx=10, pady=10, bd=2, cursor="hand2",command=lambda: btn_click(6))
seis.place(x=115, y=220)

soma = Button(tk, text="+", bg="#000000",fg = "white", width=1, height= 1, font=("Arial", 12, "bold"), padx=10, pady=10, bd=2, cursor="hand2",command=lambda: btn_click("+"))
soma.place(x=165, y=220)

um = Button(tk, text="1", bg="#000000",fg = "white", width=1, height= 1, font=("Arial", 12, "bold"), padx=10, pady=10, bd=2, cursor="hand2",command=lambda: btn_click(1))
um.place(x=15, y=280)

dois = Button(tk, text="2", bg="#000000",fg = "white", width=1, height= 1, font=("Arial", 12, "bold"), padx=10, pady=10, bd=2, cursor="hand2",command=lambda: btn_click(2))
dois.place(x=65, y=280)

tres = Button(tk, text="3", bg="#000000",fg = "white", width=1, height= 1, font=("Arial", 12, "bold"), padx=10, pady=10, bd=2, cursor="hand2",command=lambda: btn_click(3))
tres.place(x=115, y=280)

subtracao = Button(tk, text="-", bg="#000000",fg = "white", width=1, height= 1, font=("Arial", 12, "bold"), padx=10, pady=10, bd=2, cursor="hand2",command=lambda: btn_click("-"))
subtracao.place(x=165, y=280)

zero = Button(tk, text="0", bg="#000000",fg = "white", width=6, height= 1, font=("Arial", 12, "bold"), padx=10, pady=10, bd=2, cursor="hand2",command=lambda: btn_click(0))
zero.place(x=15, y=340)

ponto = Button(tk, text=".", bg="#000000",fg = "white", width=1, height= 1, font=("Arial", 12, "bold"), padx=10, pady=10, bd=2, cursor="hand2",command=lambda: btn_click("."))
ponto.place(x=115, y=340)

igual = Button(tk, text="=", bg="#005511",fg = "white", width=1, height= 1, font=("Arial", 12, "bold"), padx=10, pady=10, bd=2, cursor="hand2",command=lambda: btn_igual())
igual.place(x=165, y=340)


tk.mainloop()


    