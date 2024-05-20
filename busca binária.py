def busca_binaria(lista, numero):
    i_menor = 0
    i_maior = len(lista) - 1
    while (True):  # roda até algum return
        i_meio = (i_menor + i_maior) // 2
        if i_menor == i_maior and lista[i_meio] != numero:
            return False
        if (i_maior < i_menor):
            return False
        if lista[i_meio] == numero:
            return True
        elif lista[i_meio] > numero:
            i_maior = i_meio - 1
        elif lista[i_meio] < numero:
            i_menor = i_meio + 1


print(busca_binaria([10, 20, 30, 40, 50, 60, 70], 45))
print(busca_binaria([0, 1, 2, 3, 4, 9, 10, 11, 12, 25, 32, 54, 56, 67, 72, 76, 87, 89, 100, 112, 400], 5))