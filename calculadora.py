

class Calculadora:
    def __init__(self):
        self.resultado = 0

    def operando(self, numero):
        self.resultado = numero
        return self.resultado

    def somar(self, numero):
        self.resultado += numero
        return self.resultado

    def subtrair(self, numero):
        self.resultado -= numero
        return self.resultado

    def multiplicar(self, numero):
        self.resultado *= numero
        return self.resultado

    def dividir(self, numero):
        self.resultado /= numero
        return self.resultado

    def potencia(self, numero):
        self.resultado = self.resultado ** numero
        return self.resultado

    def limpar(self):
        self.resultado = 0
        return self.resultado
