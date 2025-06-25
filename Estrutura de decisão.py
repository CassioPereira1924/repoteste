idade = int(input('Qual a sua idade: '))
ingresso = input('Você comprou o ingresso? S/N ').upper()
nome = input('Qual o seu nome? ').title()

if idade >= 18 and ingresso == 'S':
    print(f'{nome}, seu acesso esta liberado! beba com modeação')
elif idade >= 18 and ingresso != 'S':
    print(f'{nome},vá até a bilheteria e compre um ingresso')
else:
    print('Acesso negado')