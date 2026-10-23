import random

def heapify(vetor, n, i, d):
 

    posicao_maior = i

    for k in range(d):    
        filho = d * i + k + 1 

        if filho < n and vetor[filho] > vetor[posicao_maior]:
            posicao_maior = filho  
            
    if posicao_maior != i:
        vetor[i], vetor[posicao_maior] = vetor[posicao_maior], vetor[i]
        heapify(vetor, n, posicao_maior, d)


def heap_sort_d_ario(vetor, d):
    """
    O CONTROLADOR DO TORNEIO (Para qualquer D filhos)
    """
    

    n = len(vetor)

    ultimo_pai = (n - 2) // d

    for i in range(ultimo_pai, -1, -1):

        heapify(vetor, n, i, d)
 
    for i in range(n - 1, 0, -1):
        
        vetor[0], vetor[i] = vetor[i], vetor[0]
    
        heapify(vetor, i, 0, d)



vetor_teste_1 = []

for i in range(10):
    vetor_teste_1.append(i)

random.shuffle(vetor_teste_1)

print("Original caótico: ", vetor_teste_1)
heap_sort_d_ario(vetor_teste_1, d=0)
print("Ordenado com D=3: ", vetor_teste_1)