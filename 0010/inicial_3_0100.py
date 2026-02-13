numero = int(input("Digite um número: "))
a, b = 0, 1
if(numero == 1):
    print("fibo é 1")
if(numero <= 0):
    print("0")
else:
    for i in range(1, numero+1):
        a , b = b ,a + b
        print(a)
    
    