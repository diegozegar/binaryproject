import os

def calcularBinario(texto):
    TABLABINARIO = [128, 64, 32, 16, 8, 4, 2, 1]
    LISTARESULTADO = []
    resultadoFinal = ""
    letra = texto
    for item in letra:
        LISTABINARIA = []
        value = ord(item)
        for x in range(len(TABLABINARIO)):
            if value >= TABLABINARIO[x]:
                value = value - TABLABINARIO[x]
                LISTABINARIA.append(1)
            else:
                LISTABINARIA.append(0)
        LISTARESULTADO.append(LISTABINARIA)

    for item in LISTARESULTADO:
        for values in item:
            resultadoFinal += str(values)
        resultadoFinal += " "
    return(resultadoFinal)
    print(LISTARESULTADO)
