# Mais linha de código e treino de lógica de programação
def frequencia(palavras: list [str]) -> dict[str, int]:
    i = 0
    dict_palavras = {}
    for palavra in palavras:
        i = 0
        if(palavra not in dict_palavras):
            dict_palavras[palavra] = 1
        else:
            i += 1
            dict_palavras[palavra]  += i
    print(dict_palavras)
        
    return dict_palavras

# menos linhas de código e mais abstrato
def frequencia2(palavras: list [str]) -> dict[str, int]:
    i = 0
    dict_palavras = {}
    for palavra in palavras:
        dict_palavras[palavra] = dict_palavras.get(palavra,0) + 1
    print(dict_palavras)
        
    return dict_palavras

frequencia(["thales", "oi", "oi", "oi", "oi", "tchau", "tchau", "tchau", "tchau", "otario", "bobão", "otario", "bobão", "otario", "bobão"])

frequencia2(["thales", "oi", "oi", "oi", "oi", "tchau", "tchau", "tchau", "tchau", "otario", "bobão", "otario", "bobão", "otario", "bobão",  "coitado",  "coitado",  "coitado",  "coitado",  "coitado"])

