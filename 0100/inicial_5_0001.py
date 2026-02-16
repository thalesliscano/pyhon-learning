lista = [2,4,5,4,2,2,5,7,8]

nova_lista = []

for i in range(len(lista)):
    if(lista[i] in lista):
        if(not (lista[i] in nova_lista)):
            nova_lista.append(lista[i])
        else:
            continue
print(nova_lista)