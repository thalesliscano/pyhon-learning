def frequencia2(palavras: list [str]) -> dict[str, int]:
    i = 0
    dict_palavras = {}
    for palavra in palavras:
        dict_palavras[palavra] = dict_palavras.get(palavra,0) + 1
        
    return dict_palavras
valor_freq = frequencia2(["thales", "oi", "oi", "oi", "oi", "tchau", "tchau", "tchau", "tchau", "otario", "bobão", "otario", "bobão", "otario", "bobão",  "coitado",  "coitado",  "coitado",  "coitado",  "coitado", "carlos", "carlos", "carlos"])

def top_n(freq: dict[str, int], n : int=5) -> list(tuple[str,int]):
    lista_palavras = []
    for chave, valor in freq.items():
        if(chave not in lista_palavras):
            lista_palavras.append((chave, valor))
    print(lista_palavras)
    for i in range(len(lista_palavras)):
        # print(i)
        # Vai trocando a posição dos itens do array até achar algo maior que i, se achar ele troca e reseta o loop
        for j in range(i + 1, len(lista_palavras)):
            if(lista_palavras[i][1] < lista_palavras[j][1]):
                lista_palavras[i], lista_palavras[j] = lista_palavras[j], lista_palavras[i]
                print(lista_palavras)
    print(lista_palavras)

    return lista_palavras
top_n(valor_freq)

