pares = 0
impares = 0

while True:
    entrada = input("Digite um número inteiro (ou 'fim' para encerrar): ")
    if entrada.lower() == 'fim':
        break
    try:
        numero = int(entrada)
        if numero % 2 == 0:
            print("Par")
            pares += 1
        else:
            print("Ímpar")
            impares += 1
    except ValueError:
        print("Entrada inválida. Digite um número inteiro ou 'fim'.")

print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")