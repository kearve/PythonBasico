class calculadora:
    def __init__(self,numero1,numero2,operando):
        self.numero1 = float(numero1)
        self.numero2 = float(numero2)
        self.operando = operando
    def genera_operacion(self):
        if self.operando == "+" :
           operacion = self.numero1 + self.numero2
        elif self.operando == "-":
           operacion = self.numero1 - self.numero2
        elif self.operando == "/":
           operacion = self.numero1 / self.numero2   
        elif self.operando == "*":
           operacion = self.numero1 * self.numero2
        else:
           operacion = None
        return operacion

print("Bienvenido a la calculadora")
numero_1 = input("Digite el primer numero: ")
operando = input("Operando: ")
numero_2 = input("Digite el segundo numero: ")

calc = calculadora(numero_1,numero_2,operando)

print("El resultado de la operacion es : ", calc.genera_operacion())
