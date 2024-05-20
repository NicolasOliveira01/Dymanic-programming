def quebra_em_listas(lista):
    resposta = []
    for e in lista:
        resposta.append([e])
    return resposta

def merge(lista1,lista2):
    i1 = 0
    i2 = 0
    resposta = []
    while i1 < len(lista1) and i2 < len(lista2):
        if (lista1[i1] < lista2[i2]):
            resposta.append(lista1[i1])
            i1 += 1
        elif (lista1[i1] >= lista2[i2]):
            resposta.append(lista2[i2])
            i2 += 1
    while i1 < len(lista1):
        resposta.append(lista1[i1])
        i1 += 1
    while i2 < len(lista2):
        resposta.append(lista2[i2])
        i2 += 1
    return resposta

def mergeSort(lista):
    lista_de_listas = quebra_em_listas(lista)
    while len(lista_de_listas) >= 2:
        l1 = lista_de_listas.pop()
        l2 = lista_de_listas.pop()
        juntada = merge(l1, l2)
        lista_de_listas.insert(0, juntada)
    return lista_de_listas[0]

print(mergeSort([5,10,66,29,4,6,120,4201,4,20]))