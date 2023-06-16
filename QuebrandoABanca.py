def maior_saldo(saldo, num_digitos):
    saldo = list(saldo)  # Converte o saldo em uma lista de caracteres
    while num_digitos > 0:
        i = 0
        while i < len(saldo) - 1:
            if saldo[i] < saldo[i+1]:
                saldo.pop(i)  # Remove o caractere se for menor que o próximo
                num_digitos -= 1
                if num_digitos == 0:
                    break
            else:
                i += 1
        else:
            saldo.pop()  # Remove o último caractere se ainda há dígitos a serem removidos

    return ''.join(saldo)


# Lê os casos de teste até o final do arquivo
while True:
    try:
        A, B = map(int, input().split())
        saldo = input().strip()
        resultado = maior_saldo(saldo, B)
        print(resultado)
    except EOFError:
        break

    