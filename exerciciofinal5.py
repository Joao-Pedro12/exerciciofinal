def encontra_palavras(lista_palavras, letra):
 return [palavra for palavra in lista_palavras if palavra.startswith(letra)]

palavras = ["banana", "maçã", "laranja", "limão"]
letra = "l"
print(encontra_palavras(palavras, letra))
