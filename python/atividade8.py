while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação (+, -, *, /): ")

        if operacao not in ['+', '-', '*', '/']:
            print("Operação inválida. Tente novamente.")
            continue

        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            if num2 == 0:
                print("Erro: divisão por zero não é permitida.")
                continue
            resultado = num1 / num2

        print(f"Resultado: {num1} {operacao} {num2} = {resultado}")
        break

    except ValueError:
        print("Erro: insira apenas números válidos.")