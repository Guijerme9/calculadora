import math

# Funções matemáticas básicas
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

# Funções científicas
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

# Validação de número
def validar_numero(valor):
    try:
        return float(valor)
    except ValueError:
        return None

# Menu de seleção
def exibir_menu():
    print("\n--- CALCULADORA CIENTÍFICA ---")
    print("1 - Operações básicas (+, -, *, /)")
    print("2 - Operações científicas (**², sqrt, sin, cos, tan, log)")
    print("0 - Sair")

# Execução principal
while True:
    exibir_menu()
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        n1 = validar_numero(input("Digite o primeiro número: "))
        n2 = validar_numero(input("Digite o segundo número: "))
        op = input("Digite o operador (+, -, *, /): ")

        if None in (n1, n2):
            print("Erro: entrada inválida.")
        else:
            if op == '+':
                print("Resultado:", somar(n1, n2))
            elif op == '-':
                print("Resultado:", subtrair(n1, n2))
            elif op == '*':
                print("Resultado:", multiplicar(n1, n2))
            elif op == '/':
                print("Resultado:", dividir(n1, n2))
            else:
                print("Operador inválido.")

    elif escolha == '2':
        n = validar_numero(input("Digite o número: "))
        op = input("Digite a operação (** para potência, sqrt, sin, cos, tan, log): ")

        if n is None:
            print("Erro: número inválido.")
        else:
            if op == '**':
                print("Resultado:", potencia(n))
            elif op == 'sqrt':
                print("Resultado:", raiz(n))
            elif op == 'sin':
                print("Resultado:", seno(n))
            elif op == 'cos':
                print("Resultado:", cosseno(n))
            elif op == 'tan':
                print("Resultado:", tangente(n))
            elif op == 'log':
                print("Resultado:", logaritmo(n))
            else:
                print("Operação inválida.")

    elif escolha == '0':
        print("Encerrando a calculadora. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")

