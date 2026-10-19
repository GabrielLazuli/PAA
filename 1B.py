import random

def heapify(vetor, n, i, d):
    """
    O MOTOR DA GRAVIDADE (A regra do 'Pai Guloso')
    Esta função garante que o pai (índice 'i') seja sempre maior que seus 'd' filhos.
    Se ele for fraco, a gravidade o puxa para as gavetas de baixo.
    """
    
    # Guarda apenas a COORDENADA (o índice da gaveta) de onde está o maior número.
    # Começamos assumindo que o pai (i) é o rei.
    posicao_maior = i
    
    # Laço que percorre dinamicamente todos os 'd' filhos do nó 'i'
    # Substitui as antigas variáveis fixas (esquerdo e direito)
    for k in range(d):
        
        # A MATEMÁTICA DA ÁRVORE:
        # Calcula o endereço exato do k-ésimo filho na memória do vetor
        filho = d * i + k + 1 

        # A TRAVA DE SEGURANÇA (O Curto-Circuito do 'and'):
        # 1. 'filho < n': Garante que não vamos tentar abrir uma gaveta que não existe (evita erro fatal).
        # 2. 'vetor[filho] > ...': Abre a gaveta e vê se o filho bateu o rei atual.
        if filho < n and vetor[filho] > vetor[posicao_maior]:
            posicao_maior = filho  # Atualiza a etiqueta com o índice da nova gaveta vencedora
            
    # Se a gaveta vencedora não for a do pai original, significa que ele perdeu para um filho.
    if posicao_maior != i:
        
        # A TROCA FÍSICA (Nas gavetas):
        # O número grande sobe para a gaveta 'i' (topo da sub-árvore).
        # O número pequeno cai para a gaveta 'posicao_maior' (fundo).
        vetor[i], vetor[posicao_maior] = vetor[posicao_maior], vetor[i]
        
        # O EFEITO CASCATA (A recursão):
        # O número pequeno caiu para a coordenada 'posicao_maior'. 
        # Chamamos o heapify de novo apontando para essa nova gaveta, 
        # para garantir que ele não seja um péssimo pai para o andar de baixo.
        heapify(vetor, n, posicao_maior, d)


def heap_sort_d_ario(vetor, d):
    """
    O CONTROLADOR DO TORNEIO (Para qualquer D filhos)
    """
    
    # Guarda o tamanho real (size) da lista 
    n = len(vetor)
    
    # ==================================================================
    # FASE 1: CONSTRUÇÃO (Build Max-Heap D-ário)
    # Arrumamos a bagunça inicial garantindo que todo pai seja maior que os filhos
    # ==================================================================
    
    # ENGENHARIA REVERSA:
    # Pegamos o índice do último elemento (n - 1), jogamos na fórmula do pai e 
    # descobrimos exatamente onde está o último nó que possui filhos.
    ultimo_pai = (n - 2) // d

    # Marcha à ré: Varre todos os pais, do último até a raiz (0)
    for i in range(ultimo_pai, -1, -1):

        # Chama a gravidade passando: o vetor, o tamanho total, a gaveta do pai atual e a quantidade de filhos
        heapify(vetor, n, i, d)
        
    # ==================================================================
    # FASE 2: ORDENAÇÃO (Sort)
    # O maior de todos já está no topo (0). Agora é colher os resultados!
    # ==================================================================
    
    # O laço encurta a "arena" a cada rodada. O 'i' marca o fim da área não ordenada.
    for i in range(n - 1, 0, -1):
        
        # O CAMPEÃO VAI PARA O COFRE:
        # Pega o maior número garantido na raiz (0) e joga para a última posição disponível (i).
        # O número pequeno aleatório que estava no fim é jogado na raiz (0).
        vetor[0], vetor[i] = vetor[i], vetor[0]
        
        # O CONSERTO DO ESTRAGO:
        # Passamos 'i' como o NOVO TAMANHO, blindando os números gigantes já guardados no fim.
        # Passamos '0' porque a raiz foi o único lugar que recebeu um número errado (intruso).
        heapify(vetor, i, 0, d)


# ======================================================================
# BATERIA DE TESTES COM CAOS (GERAÇÃO ALEATÓRIA)
# ======================================================================
vetor_teste_1 = []

# Geração de vetor ordenado de 0 a 9 (10 entradas)
for i in range(10):
    vetor_teste_1.append(i)

# Embaralha os números, provando que o algoritmo organiza qualquer cenário
random.shuffle(vetor_teste_1)

print("Original caótico: ", vetor_teste_1)

# Aciona o motor passando o vetor e exigindo que a árvore seja Ternária (3 filhos por nó)
heap_sort_d_ario(vetor_teste_1, d=3)

print("Ordenado com D=3: ", vetor_teste_1)