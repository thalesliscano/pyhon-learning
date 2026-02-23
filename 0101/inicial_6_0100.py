import re

texto = "Hoje eu fui ao Recanto Ybeeporã. Hoje, EU fui cedo! Será que eu fui mesmo? Fui, sim: eu fui. No recanto, vi abelhas — abelhas Jataí, abelhas mandaçaia e ABELHAS! E eu pensei: “que lugar bom… bom, bom!”"

texto = re.sub(r"[^\w\s]", " ", texto)
texto = texto.lower()
texto = " ".join(texto.split())
lista_palavra = texto.split()

dicionario = {}


for palavra in lista_palavra:
    tam = len(palavra)
    if(tam in dicionario):
        if(palavra not in dicionario[tam]):
            print(dicionario[tam])
            dicionario[tam].append(palavra)
    else:
        dicionario[tam] = [palavra]

print(dicionario)