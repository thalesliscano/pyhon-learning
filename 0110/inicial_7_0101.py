

#frequencia
def frequencia(palavras: list [str]) -> dict[str,int]:
#frequencia_print
    dicionario_palavras = {}
    for palavra in palavras:
        if(palavra in dicionario_palavras):
            dicionario_palavras[palavra] += 1
        else:
            dicionario_palavras[palavra] = 1
    return dicionario_palavras

texto = ["thales", "oi", "oi", "oi", "oi", "tchau", "tchau", "tchau", "tchau", "otario", "bobão", "otario", "bobão", "otario", "bobão",  "coitado",  "coitado",  "coitado",  "coitado",  "coitado"]

def frequencia_print(dicionario_palavras: dict[str, int]) -> str:
    for chave,valor in dicionario_palavras.items():
        print(f"{chave} : {valor}")

frequencia_print(frequencia(texto))