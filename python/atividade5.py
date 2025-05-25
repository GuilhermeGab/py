
idade = int(input("Por Favor, informe a sua idade: "))

if idade >= 1 and idade <= 12:
    print(f"Voce tem: {idade}, ainda é criança")

elif idade >= 13 and idade <= 17:
    print(f"Voce tem: {idade}, ja é um adolecente")

elif idade >= 18 and idade <= 59:
    print(f"Voce tem: {idade}, é um adulto")

elif idade >= 60:
    print(f"Voce tem: {idade}, já é idoso")