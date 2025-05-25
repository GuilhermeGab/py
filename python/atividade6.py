try:  
    altura = float(input("Informe sua altura: ")) 
    peso = float(input("Informe seu peso: "))

    imc = peso / (altura ** 2)

    print(f"Seu IMC é de: {imc:.1f}")

    if imc <= 18.4:
        print("Você está abaixo do peso")
    elif imc >= 18.5 and imc <= 24.9:
        print("Você está com o peso normal")
    elif imc >= 25 and imc <= 29.9:
        print("Você está com sobrepeso")
    elif imc >= 30 and imc <= 34.9:
        print("Você está com obesidade grau 1")
    elif imc >= 35 and imc <= 39.9:
        print("Você está com obesidade grau 2")
    elif imc >= 40:
        print("Você está com obesidade grau 3")

except ValueError:
    print("Erro: informe valores numéricos válidos.")

