# Dicionário para armazenar os usuários e seus filmes
usuarios_filmes = {}

while True:
    print("\n=== MENU ===")
    print("1 - Adicionar filme")
    print("2 - Remover filme")
    print("3 - Consultar filmes de um usuário")
    print("4 - Exibir todos os usuários")
    print("0 - Sair")

    try:
        escolha = int(input("Escolha: "))
    except ValueError:
        print("Por favor, digite um número válido.")
        

    match escolha:
        case 1:
            usuario = input("Nome do usuário: ").title()
            filme = input("Nome do filme: ").title()
            if usuario in usuarios_filmes:
                usuarios_filmes[usuario].append(filme)
            else:
                usuarios_filmes[usuario] = [filme]
            print("Filme adicionado com sucesso!")

        case 2:
            usuario = input("Nome do usuário: ").title()
            filme = input("Nome do filme: ").title()
            if usuario in usuarios_filmes:
                if filme in usuarios_filmes[usuario]:
                    usuarios_filmes[usuario].remove(filme)
                    print(f"Filme '{filme}' removido de {usuario}.")
                else:
                    print(f"O filme '{filme}' não está na lista de {usuario}.")
            else:
                print(f"O usuário '{usuario}' não está cadastrado.")

        case 3:
            usuario = input("Nome do usuário: ").strip().title()
            filmes = usuarios_filmes.get(usuario)
            if filmes is not None:
                print(f"Filmes assistidos por {usuario}: {filmes}")
            else:
                print(f"O usuário '{usuario}' não está cadastrado.")



        case 4:
            if usuarios_filmes:
                for usuario, filmes in usuarios_filmes.items():
                    print(f"{usuario}: {filmes}")
            else:
                print("Nenhum usuário cadastrado.")

        case 0:
            print("Encerrando o programa...")
            break

        case _:
            print("Opção inválida. Tente novamente.")