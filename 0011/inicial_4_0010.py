# aaabbbccc
# a3b3c3

frase = input("Digite algo: ")
frase_final = ""

conjunto_letras = set()
for letra in frase:
    conjunto_letras.add(letra)
lista_letras = sorted(conjunto_letras)

for i in lista_letras:
    z = 0
    for j in frase:
        if(i == j):
            z += 1
    frase_final +=i
    frase_final += str(z)      
print(frase_final)