palavra = input("Digite uma palavra: ")
palavra_clear = palavra.replace(" ", "").lower()
palavra_revertida = ""

for i in palavra_clear[::-1]:
    palavra_revertida += i
if(palavra_clear == palavra_revertida):
    print("É um palíndromo!")
else:
    print("Não é um palíndromo!")
