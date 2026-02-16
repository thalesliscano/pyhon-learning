lista_um = ( 2, 4, 5, 9, 8, 0, 7, 6)
lista_dois = (4, 2, 6, 7, 6,7 )

nova_lista = []

for i in lista_um:
    if(i in lista_dois):
        if(not (i in nova_lista)):
            nova_lista.append(i)
    print(nova_lista)