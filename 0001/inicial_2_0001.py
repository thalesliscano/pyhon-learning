# num_1 = int(input("Digite o primeiro número: "))
# num_2 = int(input("Digite o segundo número: "))
# num_3 = int(input("Digite o terceiro número: "))
num_1 = 21
num_2 = 32
num_3 = 43

aux = 0
print("oi")
if(num_1 > num_2):
    if(num_1 > num_3):
        aux = num_1 
    else:
        aux = num_3
        if(aux > num_2):
            aux = aux
        else:
            aux = num_2
else:
    aux = num_2
    if(aux > num_3):
        aux = aux
    else:
        aux = num_3
print(aux)