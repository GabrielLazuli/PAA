
vetor = [5,4,1,2,3]

print(vetor)

def heap(vetor):

    #tamanho do vetor 
    n = len(vetor)

    # // faz o piso no calculo 
    ultimo_pai = (n // 2) - 1

    # 1. FASE DE CONSTRUÇÃO (Build)
    #segundo parametro é o criterio de parada terceiro parametro é para decrementar
    for i in range(ultimo_pai, -1, -1):
        heapify(vetor, n, i)

    # 2. FASE DE ORDENAÇÃO (Sort)
    # Começa do último índice (n-1) e vai descendo até o índice 1
    for i in range(n - 1, 0, -1):

        # Troca o maior elemento (raiz no índice 0) com o último não ordenado (índice i)
        vetor[i], vetor[0] = vetor[0], vetor[i]

        # Conserta a árvore. 
        # O detalhe genial: passamos 'i' como o novo tamanho do vetor.
        # Se 'i' vale 4, o heapify acha que o vetor só tem 4 posições e ignora a 5ª.
        heapify(vetor, i, 0)

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
