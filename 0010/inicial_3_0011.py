numero = int(input("Digite um número: "))
i = 0
while numero > 0:
    rest = numero % 10
    numero = numero // 10
    i += 1
print(f"A quantidade de número é {i}")



