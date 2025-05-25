def verifica_palindromo(texto: str) -> str:
    
    texto_limpo = ''.join(char.lower() for char in texto if char.isalnum())

    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
        return "Nao"


if __name__ == "__main__":
    entrada = input("Digite uma palavra ou frase: ")
    resultado = verifica_palindromo(entrada)
    print(f"É palíndromo? {resultado}")