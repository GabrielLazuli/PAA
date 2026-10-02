


def insertion_sort(lista):
    """Ordena uma lista usando o algoritmo Insertion Sort."""

    # Percorre a lista a partir do segundo elemento.
    for indice_atual in range(1, len(lista)):
        valor_atual = lista[indice_atual]
        indice_anterior = indice_atual - 1

        # Move os elementos maiores para a direita até achar a posição correta.
        while indice_anterior >= 0 and lista[indice_anterior] > valor_atual:
            lista[indice_anterior + 1] = lista[indice_anterior]
            indice_anterior -= 1

        # Insere o valor_atual na posição correta.
        lista[indice_anterior + 1] = valor_atual

    return lista

if __name__ == "__main__":
    numeros = [7, 3, 9, 1, 5]
    print("Lista original:", numeros)
    print("Lista ordenada:", insertion_sort(numeros.copy()))
