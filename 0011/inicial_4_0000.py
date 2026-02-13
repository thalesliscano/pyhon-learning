frase = input("Digite uma palavra ou frase: ")

cont = 0

for letra in frase:
    if(letra in "aeiou"):
        cont +=1
print(cont)