lista_num = [int(x) for x in input("Digite os números separados por espaço: ").split()]

maior = lista_num[0]
menor = lista_num[0]

for i in lista_num:
    if i < menor:
        menor = i
    if i > maior:
        maior = i

print(f"Maior é {maior}")
print(f"Menor é {menor}")