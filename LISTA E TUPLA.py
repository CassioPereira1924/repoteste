lista = ['João', 16, 'Santa Cruz']

print(f'O aluno {lista[0]} tem {lista[1]} anos e mora em {lista[2]}')

lista.append('Rio de Janeiro')

print(f'O aluno {lista[0]} tem {lista[1]} anos e mora no bairro {lista[2]} na cidade {lista[3]}')

lista.insert(1, 'Masculino')
print(lista)


'''lista.pop(2)
lista.remove()'''
print(lista[3:6])