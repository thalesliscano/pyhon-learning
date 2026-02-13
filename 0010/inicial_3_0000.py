numero = int(input("Digite até qual tabuada você deseja ver: "))
aux = 0
for i in range(1,10+1):
    aux = numero * i
    print(f"{numero} X {i} = {aux}")
