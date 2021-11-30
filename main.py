# from tkinter import *
from calculadora import Calculadora

# # menu_inicial = Tk()
# # menu_inicial.title("Calculadora")
# # menu_inicial.mainloop()
calc = Calculadora()

calc.operando(20)
print(calc.somar(10)) # teste de classe

calc.limpar()
calc.operando(60)
print(calc.subtrair(20)) # teste de classe

calc.limpar()
calc.operando(6)
print(calc.multiplicar(20)) # teste de classe

calc.limpar()
calc.operando(60)
print(calc.dividir(20)) # teste de classe

calc.limpar()
calc.operando(3)
print(calc.potencia(3)) # teste de classe
