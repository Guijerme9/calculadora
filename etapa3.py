def validar_numero(valor):
    try:
        return float(valor)
    except ValueError:
        return None

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero"

def calcular(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return dividir(a, b)
    else:
        return "Operador inválido."

n1 = input("Digite o primeiro número: ")
n2 = input("Digite o segundo número: ")
op = input("Digite o operador (+, -, *, /): ")

num1 = validar_numero(n1)
num2 = validar_numero(n2)

if num1 is None or num2 is None:
    print("Erro: entrada inválida.")
else:
    resultado = calcular(num1, num2, op)
    print("Resultado:", resultado)