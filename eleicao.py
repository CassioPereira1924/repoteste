print("=== Sistema de Votação Escolar ===")

# Contadores de votos
votos_goku = 0
votos_naruto = 0
votos_luffy = 0

while True:
      print("\n=== Votação ===")

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
                  print('somente alunos com 14 anos ou mais podem votar.\n')
                  pode_votar = 'nao'
                  break
              else:
                  pode_votar = 'sim'
                  break
          except ValueError:
              print('Difite um Nº Válido')


      if pode_votar == 'nao':
          break





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
                    elif voto == 2:
                        votos_naruto += 1
                    elif voto == 3:
                        votos_luffy += 1
                else:
                    print("\nErro: Número de candidato inválido.\n")
            except ValueError:
                print('Digite um número')


            continuar = input("Deseja registrar outro voto? (s/n): ").strip().lower()
            if continuar != 's':
                break

      break


if pode_votar == 'sim':
        print("\n=== Resultado da Eleição ===")
        print("goku:", votos_goku, "votos")
        print("naruto:", votos_naruto, "votos")
        print("luffy:", votos_luffy, "votos")


        if votos_goku > votos_naruto and votos_goku > votos_luffy:
            vencedor = "Goku"
        elif votos_naruto > votos_goku and votos_naruto > votos_luffy:
            vencedor = "Naruto"
        elif votos_luffy > votos_goku and votos_luffy > votos_naruto:
            vencedor = "Luffy O REI DOS PIRATAS"
        else:
            vencedor = "Empate"

        if vencedor == "Empate":
            print("\nA eleição terminou em empate.")
        else:
            print(f"\nO vencedor da eleição é: {vencedor}!")
