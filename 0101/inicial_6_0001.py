import re

texto = "Hoje eu fui ao Recanto Ybeeporã. Hoje, EU fui cedo! Será que eu fui mesmo? Fui, sim: eu fui. No recanto, vi abelhas — abelhas Jataí, abelhas mandaçaia e ABELHAS! E eu pensei: “que lugar bom… bom, bom!”"

texto = re.sub(r"[^\w\s]", " ", texto)
texto = texto.lower()
texto = " ".join(texto.split())
lista_palavra = texto.split()

dicionario = {}

for palavra in lista_palavra:
    quantidade = lista_palavra.count(palavra)
    tam = len(palavra)
    if not (palavra in dicionario):
        dicionario[palavra] = {
            "valores": (quantidade, tam)
        }
for i in dicionario:
    print(dicionario[i])