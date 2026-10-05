import random
def heapify(vetor, n, i, d):
    
    maior = i
    
    # Laço que percorre cada um dos d filhos do nó 'i'
    # k varia de 0 até d-1
    for k in range(d):
        filho = d * i + k + 1  # Fórmula do k-ésimo filho no vetor

    
        # Se o filho existe dentro da arena (filho < n)
        # e tem valor maior do que o 'maior' encontrado até agora
        if filho < n and vetor[filho] > vetor[maior]:
            maior = filho
            
    # Se o maior elemento for um dos d filhos (e não o pai)
    if maior != i:
        # Troca o pai pelo filho maior
        vetor[i], vetor[maior] = vetor[maior], vetor[i]
        
        # Continua descendo a árvore para consertar o perdedor no seu novo nível
        heapify(vetor, n, maior, d)


def heap_sort_d_ario(vetor, d):

    n = len(vetor)
    
    # ------------------------------------------------------------------
    # FASE 1: CONSTRUÇÃO (Build Max-Heap D-ário)
    # ------------------------------------------------------------------
    # Cálculo do último nó pai para uma árvore com D filhos
    ultimo_pai = (n - 2) // d

    # Varre todos os pais de trás para frente, até a raiz (0)
    for i in range(ultimo_pai, -1, -1):
        heapify(vetor, n, i, d)
        
    # ------------------------------------------------------------------
    # FASE 2: ORDENAÇÃO (Sort)
    # ------------------------------------------------------------------
    # Desloca o maior elemento para o final do vetor e encurta a arena
    for i in range(n - 1, 0, -1):
        # O campeão no topo (0) troca com a última posição não ordenada (i)
        vetor[0], vetor[i] = vetor[i], vetor[0]
        
        # Reorganiza o nó 0 considerando que o vetor encolheu para tamanho 'i'
        heapify(vetor, i, 0, d)


# ======================================================================
# BATERIA DE TESTES
# ======================================================================

# Exemplo 1: Heap Ternário (d = 3 filhos)
vetor_teste_1 = []

#geração de vetor aleatorio de 20 entradas 
for i in range(30):
    vetor_teste_1.append(i)
random.shuffle(vetor_teste_1)

print("--- TESTE: Heap Ternário (d = 3) ---")
print("Original: ", vetor_teste_1)
heap_sort_d_ario(vetor_teste_1, d=3)
print("Ordenado: ", vetor_teste_1)
