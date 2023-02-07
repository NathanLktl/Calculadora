#Define a operação
def calcule(numero1, operador, numero2):
    if operador == '+':
        return numero1 + numero2
    elif operador == '-':
        return numero1 - numero2
    elif operador == '*':
        return numero1 * numero2
    elif operador == '/':
        return numero1 / numero2
    else:
        return 'Operador Inválido'


#Pega os dados inseridos pelo usuário
numero1 = float(input('Digite um número: '))
operador = input('Digite o operador desejado: ')
numero2 = float(input('Digite outro número: '))

# Calcula o resultado
resultado= calcule(numero1, operador, numero2)

# Mostra o resultado
print(resultado)
