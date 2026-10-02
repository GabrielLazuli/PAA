
vetor = [9,8,7,6,5,4,3,2,1]

def heap(vetor):

    n = len(vetor)

    # // faz o piso no calculo 
    ultimo_pai = (n // 2) - 1

    # segundo parametro é o criterio de parada terceiro parametro é para decrementar
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

        vetor[i], vetor[maior] = vetor[maior], vetor[i]

        heapify(vetor, n, maior)
