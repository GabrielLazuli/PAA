def quick_sort(lista): 

    if len(lista) <= 1:
        return lista

    pivo = lista[len(lista) // 2]

    esquerda = [x for x in lista if x < pivo ]
    meio = [x for x in lista if x == pivo ]
    direita = [x for x in lista if x > pivo ]

    return quick_sort(esquerda) + meio + quick_sort(direita)

lista = [1,3,9,6,7,4,8,2,5]

print(f"Desordenado: {lista}" )
lista = quick_sort(lista)
print(f"Ordenado:    {lista}" )
