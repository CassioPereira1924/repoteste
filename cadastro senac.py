print(30*('#') + (' BEM VINDO AO SENAC ') + 30*('#'))

while True:
    try:
        nome = input('\nDigite seu nome: ')

        if not nome.isalpha():
            raise ValueError('\nDigite nome com letras do alfabeto')
        break
    except ValueError as e:
        print(e)

print('1 - ANÁLISE DE DADOS\n2 - POWER BI')

while True:
    try:
        opcao = int(input('Digite a opção do curso desejado: '))
        if opcao in [1,2]:
            break       
    except ValueError:
        print('Digite uma opção válida')

match opcao:
    case 1:
        print(f'Parabéns {nome}!! Seu curso de Análise de Dados começará em 10 dias')
    case 2:
        print(f'Parabéns {nome}!! Seu curso de Power BI começará em 10 dias')


