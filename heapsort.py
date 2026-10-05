
vetor = [3,4,7,2,9]

def heap(vetor):

    #tamanho do vetor 
    n = len(vetor)

    # // faz o piso no calculo 
    ultimo_pai = (n // 2) - 1

    # 1. FASE DE CONSTRUÇÃO (Build)
    #segundo parametro é o criterio de parada terceiro parametro é para decrementar
    for i in range(ultimo_pai, -1, -1):
        heapify(vetor, n, i)


def heapify(vetor,n, i ):

    maior = i

    esquerdo = i * 2 + 1 
    direito = i * 2 + 2

    if esquerdo < n and  vetor[esquerdo] > vetor[maior]:
        maior = esquerdo

    if direito < n  and vetor[direito] > vetor[maior]: 
        maior = direito 
        
    if maior != i: 

        # A troca física dos valores no vetor
        vetor[i], vetor[maior] = vetor[maior], vetor[i]

        heapify(vetor, n, maior)


print(vetor)
heap(vetor)
print(vetor)
