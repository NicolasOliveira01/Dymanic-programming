def selectionSort(lista):
    for indice in range(len(lista)):
        i_menor = indice
        for i in range(indice + 1, len(lista)):
            if lista[i] < lista[i_menor]:
                i_menor = i
        if i_menor != indice:
            temp = lista[indice]
            lista[indice] = lista[i_menor]
            lista[i_menor] = temp
    return lista

print(selectionSort([3,6,10,76,2,50,45,1,55555,20202845,32,6,76,2]))