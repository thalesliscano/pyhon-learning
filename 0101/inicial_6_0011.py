import re

texto = "Hoje eu fui ao Recanto Ybeeporã. Hoje, EU fui cedo! Será que eu fui mesmo? Fui, sim: eu fui. No recanto, vi abelhas — abelhas Jataí, abelhas mandaçaia e ABELHAS! E eu pensei: “que lugar bom… bom, bom!”"

texto = re.sub(r"[^\w\s]", " ", texto)
texto = texto.lower()
texto = " ".join(texto.split())
lista_palavra = texto.split()

dicionario = {
    "mais_longa": ("",len(lista_palavra[0])),
    "mais_curta": ("",len(lista_palavra[0])),
}
for palavra in lista_palavra:
    tam = len(palavra)
    if(tam > dicionario["mais_longa"][1]):
        dicionario["mais_longa"] = (palavra, tam)
    if(tam < dicionario["mais_curta"][1]):
        dicionario["mais_curta"] = (palavra, tam)
print(dicionario)

