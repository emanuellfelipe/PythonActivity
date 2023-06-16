# Definindo as operações
def sucessor(a):
    return a + 1

def soma(a, b):
    for _ in range(b):
        a = sucessor(a)
    return a

def multiplicacao(a, b):
    result = 0
    for _ in range(b):
        result = soma(result, a)
    return result

def exponenciacao(a, b):
    result = 1
    for _ in range(b):
        result = multiplicacao(result, a)
    return result

#Descobrindo qual operação foi selecionada e executando-a
while True:
    operacao = input()
    if operacao == "":
        break

    operacao = operacao.capitalize().split()
    if operacao[0] == "Suc":
        a = int(operacao[1])
        print(sucessor(a))
    elif operacao[0] == "Soma":
        a = int(operacao[1])
        b = int(operacao[2])
        print(soma(a, b))
    elif operacao[0] == "Exp":
        a = int(operacao[1])
        b = int(operacao[2])
        print(exponenciacao(a, b))
    elif operacao[0] == "Mult" or "Multi":
        a = int(operacao[1])
        b = int(operacao[2])
        print(multiplicacao(a, b))
    else:
        
        a = int(operacao[1])
        b = int(operacao[2])
        print(exponenciacao(a, b))
        
