#Criar um dicionário:
aluno = {"nome": 'Ana', "idade": 16, "nota": 9.0}
# Acessar valores:
print(aluno["nome"]) # Ana
# Adicionar ou modificar valores:
aluno["nota"] = 9.5
aluno["turma"] = "3A"
print(aluno)
# Remover itens:
del aluno["idade"]
# Obter apenas chaves, valores ou ambos:
print(aluno.keys())
print(aluno.values())
print(aluno.items())
# Verificar se uma chave existe:
if "nome" in aluno:
    print("Nome encontrado!")
# Tamanho do dicionário:
print(len(aluno))

for chave, valor in aluno.items():
    print(f"{chave}: {valor}")

# Limpar o dicionário:
aluno.clear()
# Copiar um dicionário:
copia = aluno.copy()
# Usar get() para acessar valores com segurança:
print(aluno.get("nome"))
print(aluno.get("endereco",'errooooooooo'))
# Atualizar um dicionário com outro:
dados_novos = {"nota": 10, "cidade": "Rio"}
aluno.update(dados_novos)
# Substituir valor:
aluno["idade"] = 17
# Apagar chave:
del aluno["idade"]
# Apagar com retorno:
nota = aluno.pop("endereco", "Chave não encontrada")
# Apagar tudo:
aluno.clear()