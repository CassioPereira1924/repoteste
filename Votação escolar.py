print("=== Sistema de Votação Escolar ===")

votos_goku = 0
votos_naruto = 0
votos_luffy = 0

while True:
      print("\n=== INICIANDO VOTAÇÃO ===")

      while True:
          try:
              nome = input("Digite seu nome: ").strip().title()
              if not nome.replace(" ", "").isalpha():
                  raise ValueError("Erro: Nome inválido. Digite apenas letras.\n")
              break
          except ValueError as e:
              print(e)

      while True:
          try:
              idade = int(input(f"{nome} digite sua idade: "))
              if idade < 14:
                    raise ValueError(f"{nome}, somente alunos com 14 anos ou mais podem votar.\n")
                    break
              break
          except ValueError as e:
              print(e)

      while True:
          print("\nCandidatos:")
          print("1. GOKU")
          print("2. NARUTO")
          print("3. LUFFY")

          try:
              voto = int(input("Digite o número do seu candidato: "))
              if voto in [1, 2, 3]:
                if voto == 1:
                    votos_goku += 1
                    break
                elif voto == 2:
                    votos_naruto += 1
                    break
                elif voto == 3:
                    votos_luffy += 1
                    break
              else:
                  raise ValueError("Erro: Número de candidato inválido.\n")
          except ValueError as e:
              print(e)


      continuar = input("Deseja registrar outro voto? (s/n): ").strip().lower()
      if continuar != 's':
        break

print("\n=== Resultado da Eleição ===")
print("goku:", votos_goku, "votos")
print("naruto:", votos_naruto, "votos")
print("luffy:", votos_luffy, "votos")


if votos_goku > votos_naruto and votos_goku > votos_luffy:
    vencedor = "goku"
elif votos_naruto > votos_goku and votos_naruto > votos_luffy:
    vencedor = "naruto"
elif votos_luffy > votos_goku and votos_luffy > votos_naruto:
    vencedor = "luffy"
else:
    vencedor = "Empate"

if vencedor == "Empate":
    print("\nA eleição terminou em empate.")
else:
    print(f"\nO vencedor da eleição é: {vencedor}!")
