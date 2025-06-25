try:
    num1 = int(input('Digite o primeiro nº'))
    num2 = int(input('Digite o segundo nº'))
    divisão = num1 / num2
    resultado = round(divisão, 0)
    print(f'O resultado da divisão é {resultado}')

except ZeroDivisionError:
    print('Dvisão por zero não é permitido')

except ValueError:
    print('Digite um Nº válido')

except:
    print('Erro inesperado')



