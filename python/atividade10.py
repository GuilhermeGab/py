while True:
    senha = input("Digite uma senha forte (ou 'sair' para encerrar): ")
    if senha.lower() == 'sair':
        print("Programa encerrado.")
        break

    if len(senha) < 8:
        print("A senha deve ter pelo menos 8 caracteres.")
        continue

    if not any(char.isdigit() for char in senha):
        print("A senha deve conter pelo menos um número.")
        continue

    print("Senha forte cadastrada com sucesso!")
    break