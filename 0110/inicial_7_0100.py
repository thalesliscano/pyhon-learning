import re
import unicodedata

def normalizar(texto: str, manter_acentos: bool=True) -> list[str]:
    texto_limpo = re.sub(r"[^\w\s]", " ", texto)
    texto_limpo = " ".join(texto_limpo.split())
    texto_limpo = texto_limpo.lower()
    
    if(manter_acentos):
        lista_palavras = texto_limpo.split()
        return lista_palavras
    else:
        texto_limpo = unicodedata.normalize("NFD", texto)
        texto_sem_acentuacao = "".join(
            c for c in texto_limpo
            if unicodedata.category(c) != "Mn"
        )
        texto_minusculo = texto_sem_acentuacao.lower()
        lista_palavras = texto_minusculo.split()
        return lista_palavras

texto = "Hoje eu fui ao Recanto Ybeeporã. Hoje, EU fui cedo! Será que eu fui mesmo? Fui, sim: eu fui. No recanto, vi abelhas — abelhas Jataí, abelhas mandaçaia e ABELHAS! E eu pensei: “que lugar bom… bom, bom!”"
lista_palavras = normalizar(texto)




