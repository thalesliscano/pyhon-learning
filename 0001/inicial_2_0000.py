num = int(input("Digite o número: "))

if num != 0:
    if(num % 2 == 0):
        print(f"O Número {num} par")
    else:
        print(f"O Número {num} é impar")
else:
    print("Número tem que ser maior que 0")