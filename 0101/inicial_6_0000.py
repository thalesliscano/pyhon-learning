import re

texto = "Hoje eu fui ao Recanto Ybeeporã. Hoje, EU fui cedo! Será que eu fui mesmo? Fui, sim: eu fui. No recanto, vi abelhas — abelhas Jataí, abelhas mandaçaia e ABELHAS! E eu pensei: “que lugar bom… bom, bom!”"

# pontuacao = '"“”.,!?;:—"()[]...'

# for letra in texto:
#     if(letra in pontuacao):
#         letra = " "
#     texto += letra

# Remove qualquer pontuação, inclusive grudada na palavra
texto = re.sub(r"[^\w\s]"," ", texto)
texto = " ".join(texto.split())
texto = texto.lower()
# print(texto)

dicionario_palavra = {}
lista_palavra = texto.split()

for palavra in lista_palavra:
    quantidade = lista_palavra.count(palavra)
    if not (palavra in dicionario_palavra):
        dicionario_palavra[palavra] = {
            "quantidade": quantidade
        }

for chave, valor in dicionario_palavra.items():
    print(chave, valor)
