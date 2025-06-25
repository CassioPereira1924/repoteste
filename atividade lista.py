#ATIVIDADE 1
nomes = []


contador = 0
while contador < 5:
    nome = input(f"Digite o {contador + 1}º nome: ")
    nomes.append(nome)
    contador += 1

print("\nLista completa de nomes:")
print(nomes)

nome_remover = input("\nDigite um nome para remover da lista: ")

if nome_remover in nomes:
    nomes.remove(nome_remover)
    print(f"\n'{nome_remover}' foi removido da lista.")
else:
    print(f"\n'{nome_remover}' não está na lista.")


print("\nLista atualizada de nomes:")
print(nomes)


#ATIVIDADE 2
produto = []
preco = []
contador = 0

while contador <= 2:
    try:
        nome_produto = input(f'Digite o nome do {contador + 1}º produto: ')
        produto.append(nome_produto)
        valor_produto = float(input(f'Digite o valor do {nome_produto}: '))
        preco.append(valor_produto)
        contador += 1
    except:
        print('erro')



indice = 0
while indice < len(produto):
    print(f'Produto {produto[indice]} custa R$ {preco[indice]:.2f}')
    indice +=1



#ATIVIDADE 3 
contador = 0
while contador < 10:
    try:
        nota = float(input(f"Digite a {contador + 1}ª nota: "))
        notas.append(nota)
        contador += 1
    except ValueError:
        print("Por favor, digite um número válido.")

notas = [5, 10 ,9.5 ,7.6 ,8 ,9.3 ,3.6 ,2 ,7 ]
print(len(notas))

media = sum(notas) / len(notas)
maior = max(notas)
menor = min(notas)
notas = [5, 10 ,9.5 ,7.6 ,8 ,9.3 ,3.6 ,2 ,7 ]
acima_da_media = []
indice = 0
while indice < len(notas):
    if notas[indice] > media:
        acima_da_media.append(notas[indice])
    indice += 1


print(f"\nMédia das notas: {media:.2f}")
print(f"Maior nota: {maior}")
print(f"Menor nota: {menor}")
print("Notas acima da média:", acima_da_media)


