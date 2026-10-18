import random 

def quick_sort(lista): 

    if len(lista) <= 1:
        return lista

    pivo = lista[len(lista) // 2]

    esquerda = [x for x in lista if x < pivo ]
    meio = [x for x in lista if x == pivo ]
    direita = [x for x in lista if x > pivo ]

    return quick_sort(esquerda) + meio + quick_sort(direita)

vetor_teste_1 = []

for i in range(10):
    vetor_teste_1.append(i)
random.shuffle(vetor_teste_1)


print(f"Desordenado: {vetor_teste_1}" )
lista = quick_sort(vetor_teste_1)
print(f"Ordenado:    {lista}" )
