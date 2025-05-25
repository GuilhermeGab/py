
def calcula_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

while True:
    try:
        print("\n--- Calculadora de Gorjeta ---")
        valor = float(input("Digite o valor da conta (ou 0 para sair): "))
        if valor == 0:
            print("Encerrando...")
            break

        porcentagem = float(input("Digite a porcentagem da gorjeta: "))
        gorjeta = calcula_gorjeta(valor, porcentagem)
        print(f"Gorjeta: R$ {gorjeta:.2f}")
        print(f"Total com gorjeta: R$ {valor + gorjeta:.2f}")
    
    except ValueError:
        print("Erro: por favor, digite números válidos.")
