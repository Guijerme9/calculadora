def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero"

print("Calculadora com Funções")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operador = input("Digite o operador (+, -, *, /): ")

if operador == '+':
    resultado = somar(num1, num2)
elif operador == '-':
    resultado = subtrair(num1, num2)
elif operador == '*':
    resultado = multiplicar(num1, num2)
elif operador == '/':
    resultado = dividir(num1, num2)
else:
    resultado = "Operador inválido."

print("Resultado:", resultado)