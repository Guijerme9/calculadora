import math

def potencia(x):
    return math.pow(x, 2)

def raiz(x):
    return math.sqrt(x)

def seno(x):
    return math.sin(math.radians(x))

def cosseno(x):
    return math.cos(math.radians(x))

def tangente(x):
    return math.tan(math.radians(x))

def logaritmo(x):
    if x > 0:
        return math.log10(x)
    else:
        return "Erro: logaritmo de número não positivo"

numero = input("Digite o número: ")
operacao = input("Digite a operação (** para potência, sqrt, sin, cos, tan, log): ")

try:
    num = float(numero)

    if operacao == '**':
        resultado = potencia(num)
    elif operacao == 'sqrt':
        resultado = raiz(num)
    elif operacao == 'sin':
        resultado = seno(num)
    elif operacao == 'cos':
        resultado = cosseno(num)
    elif operacao == 'tan':
        resultado = tangente(num)
    elif operacao == 'log':
        resultado = logaritmo(num)
    else:
        resultado = "Operação inválida."

    print("Resultado:", resultado)
except ValueError:
    print("Erro: número inválido.")