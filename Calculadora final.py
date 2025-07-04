while True:
  try:
    num = int(input('Digite um número inteiro: '))
    break
  except ValueError:
    print('Valor inválido. Tente novamente.')

while True:
  try:
    operacao = input('Digite a operação desejada (+, -, *, /): ')
    if operacao in ['+', '-', '*', '/']:
      break
    else:
      print('Operação inválida. Tente novamente.')
  except ValueError:
    print(f'Erro:')

while True:
  try:
    num2 = int(input('Digite outro número inteiro: '))
    if operacao == '/' and num2 == 0:
      raise ValueError('Não é possível dividir por zero.')
    break
  except ValueError as e:
    print(f'Erro: {e}')


if operacao == '+':
  resultado = num + num2
  print(f'O resultado da soma é: {resultado}')
elif operacao == '-':
  resultado = num - num2
  print(f'O resultado da subtração é: {resultado}')
elif operacao == '*':
  resultado = num * num2
  print(f'O resultado da multiplicação é: {resultado}')
else:
  resultado = num / num2
  print(f'O resultado da divisão é 3: {resultado}')
