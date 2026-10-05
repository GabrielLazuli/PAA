def heapify(vetor, n, i):
    
    maior = i            # Assumimos que o pai atual é o 'rei' absoluto
    esquerdo = 2 * i + 1 # Posição do filho da esquerda
    direito = 2 * i + 2  # Posição do filho da direita

    #  O filho da esquerda existe e é maior que o maior atual?
    if esquerdo < n and vetor[esquerdo] > vetor[maior]:
        maior = esquerdo  # O filho da esquerda assume o maior!

    # O filho da direita existe e é maior que o maior atual?
    if direito < n and vetor[direito] > vetor[maior]:
        maior = direito   # O filho da direita rouba o maior!

    #Se o maior original (i) foi derrotado por algum dos seus filhos...
    if maior != i:
        # Troca: O filho forte sobe e o pai fraco cai
        vetor[i], vetor[maior] = vetor[maior], vetor[i]

        #O pai que caiu continua sendo testado no andar de baixo
        heapify(vetor, n, maior)


def heap_sort(vetor):
  
    n = len(vetor)

    # =========================================================================
    # FASE 1: A CONSTRUÇÃO DA HIERARQUIA (Build Max-Heap)
    # Varrida de baixo para cima (bottom-up) para organizar o caos.
    # =========================================================================
    
    # Encontra o último nó que realmente é pai (tem pelo menos 1 filho)
    ultimo_pai = (n // 2) - 1

    # Caminhamos de marcha à ré: do último pai até a grande Raiz (índice 0)
    for i in range(ultimo_pai, -1, -1):
        heapify(vetor, n, i)

    # Neste ponto exato, o maior número de TODOS está garantido na Raiz (vetor[0])!

    # =========================================================================
    # FASE 2: O TORNEIO DE ELIMINAÇÃO (Sort)
    # Arrancamos o campeão do topo e jogamos para o final da fila.
    # =========================================================================
    
    # Vais encolhendo a arena do torneio, do último índice (n-1) até o índice 1
    for i in range(n - 1, 0, -1):
        
        # 1. O Maior garantido no (vetor[0]) vai para o cofre no final do vetor (vetor[i]),
        #    e um pequeno aleatório do fim da fila é jogado no (vetor[0]).
        vetor[0], vetor[i] = vetor[i], vetor[0]
        # 2.  Passamos 'i' como novo tamanho para "trancar"
        #    o campeão no fim e pedimos para o heapify arrumar a raiz bagunçada.
        heapify(vetor, i, 0)


# =============================================================================
# TESTANDO O NOSSO TORNEIO DE NÚMEROS
# =============================================================================
vetor = [3, 4, 7, 2, 9, 1, 5]

print("não ordenado:", vetor)

heap_sort(vetor)

print("ordenado:", vetor)