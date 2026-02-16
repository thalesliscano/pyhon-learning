lista_um = [ 1,2,3,4,5,0]

nova_lista = []

print(lista_um[-0:])
print("oi")
for i in range(0, len(lista_um)+1):
    nova_lista = lista_um[-i:] + lista_um[:-i]# ignora o resto da lista + ignora o último da lista
    print(nova_lista)
    