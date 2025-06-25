'''contador = 0

while contador <= 5:
    print(f'Nº {contador}')
    contador += 1'''

'''while True:
    senha = input('Digite a senha: ')

    if senha == 'senac@13455':
        print('Acesso permitido')
        break
    else:
        print('Senha inválida')'''



lista = []

while True:
    try:
        nome = input('Digite um nome: ')

        if not nome.isalpha():
            raise ValueError("Digite um nome válido sem números.")

        lista.append(nome)

        sair = input('Deseja adicionar mais um nome? ').lower()

        if sair != 'sim':
            break

    except ValueError as e:
        print(e)


print(lista)

'''try:
    num = int(input('nº:' ))
    print(num)
except ValueError as e:
    print(f'o erro é {e}')'''
'''while True:
    try:

        num1 = int(input('Nº: '))
        break
    except ValueError:
        print('digite um Nº')'''



