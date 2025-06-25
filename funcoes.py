'''def saudacao():
    return print('Análise de dados Senac')

saudacao()

def dobro(a):
    dobro = a * 2
    return print(f'O dobro de {a} é {dobro}')

def nota(b):
    if b >= 7:
        return print('Aprovado')
    else:
        return print('Reprovado')

nota(5)

def verificar_par(numero):
    if numero % 2 == 0:
         return print("Par")
    else:
        return print("Ímpar")

verificar_par(5)

verificar_par(122)'''


def maior(a,b):
    if a > b:
        return print(f'{a} é o maior')
    else:
        return print(f'{b} é o maior')

num1 = 30
num2 = 40    
maior(num1, num2)

def media_lista(a):
    media = sum(a) / len(a)
    return print(f'A média é {media}')

lista = [15,36,59,252]

media_lista(lista)