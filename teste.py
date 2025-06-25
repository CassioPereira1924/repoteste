aluno = {"nome": 'Ana', "idade": 16, "nota": 9.0}

print(aluno.keys())
print(aluno.values())
print(aluno.items())

for a, b in aluno.items():
    print(f"A chave é {a} e o valor é {b}")

dados_novos = { "cidade": "Rio", "nota": 10}
aluno.update(dados_novos)
aluno.pop('nota', 5)

print(aluno)