

saida = ''

def adicao(a, b):
    return a + b

def subracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Não foi possível realizar a divisão por 0"
    return a / b

def calculadora(num1, num2, operacao):
    op = operacao.strip().lower()
    if op == '+' or op in ('adicao', 'adição'):
        return adicao(num1, num2)
    elif op == '-' or op in ('subtracao', 'subtração'):
        return subracao(num1, num2)
    elif op == '*' or op in ('multiplicacao', 'multiplicação'):
        return multiplicacao(num1, num2)
    elif op == '/' or op in ('divisao', 'divisão'):
        return divisao(num1, num2)
    else:
        return "Operação inválida"

while saida.lower() != 'n':
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    operacao = input('Digite a operação (+, -, *, / ou nome): ')
    resultado = calculadora(num1, num2, operacao)
    print('Resultado da operação:', resultado)
    saida = input('Deseja continuar? (S/N): ')
