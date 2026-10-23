import random

def quick_sort_multi(lista, num_pivos):

    # CONDIÇÃO DE PARADA (CASO BASE DA RECURSÃO)
    
    if len(lista) <= 1:
        return lista
    
    qtd_pivos = min(num_pivos, len(lista) - 1)

    if qtd_pivos < 1:   
        qtd_pivos = 1

    pivos = sorted(lista[:qtd_pivos])
    resto_da_lista = lista[qtd_pivos:]

    # FASE 2: CRIAÇÃO DOS BALDES DINÂMICOS NA MEMÓRIA

    intervalos = [[] for _ in range(qtd_pivos + 1)]
   
    iguais = [[p] for p in pivos] 

    # --------------------------------------------------------
    # FASE 3: A DISTRIBUIÇÃO (O Fatiamento na Prática)
    # --------------------------------------------------------
    for x in resto_da_lista:
        alocado = False
 
        for i in range(qtd_pivos):

            if x < pivos[i]:
                intervalos[i].append(x)
                alocado = True
                break 
 
            elif x == pivos[i]:
                iguais[i].append(x)
                alocado = True
                break
    
        if not alocado:
            intervalos[-1].append(x)

    resultado = []

    for i in range(qtd_pivos):
        resultado += quick_sort_multi(intervalos[i], num_pivos) + iguais[i]
    resultado += quick_sort_multi(intervalos[-1], num_pivos)

    return resultado


# ======================================================================
# BATERIA DE TESTES COM GERADOR ALEATÓRIO E EMBARALHAMENTO
# ======================================================================
vetor_teste_1 = []

# Geração de vetor ordenado de 0 a 9
for i in range(10):
    vetor_teste_1.append(i)

# O caos: embaralha as posições para testar a resiliência do algoritmo
random.shuffle(vetor_teste_1)

print("Original desordenado: ", vetor_teste_1)

# Diferente do Heap Sort (in-place), este Quicksort gera um vetor novo.
# Por isso guardamos o retorno na mesma variável.
vetor_teste_1 = quick_sort_multi(vetor_teste_1, num_pivos=7)

print("Ordenado perfeitamente: ", vetor_teste_1)