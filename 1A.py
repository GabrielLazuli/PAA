import random

def quick_sort_multi(lista, num_pivos):
    # ---------------------------------------------------------
    # CONDIÇÃO DE PARADA (CASO BASE DA RECURSÃO)
    # ---------------------------------------------------------
    # Se a lista tem 1 ou 0 elementos, é impossível dividi-la mais. Já está ordenada.
    if len(lista) <= 1:
        return lista

    # TRAVA DE SEGURANÇA:
    # Garante que não vamos tentar usar mais pivôs do que o tamanho do vetor.
    # Ex: Num vetor de 3 números, podemos ter no máximo 2 pivôs (sobrando 1 para avaliar).
    qtd_pivos = min(num_pivos, len(lista) - 1)
    if qtd_pivos < 1:
        qtd_pivos = 1

    # ---------------------------------------------------------
    # FASE 1: A ESCOLHA E PREPARAÇÃO DOS PIVÔS (AS FACAS)
    # ---------------------------------------------------------
    # Cortamos os N primeiros elementos da lista e os ORDENAMOS. 
    # Sem ordenar os pivôs, as barreiras de limite (menor que, maior que) não funcionam.
    pivos = sorted(lista[:qtd_pivos])
    
    # O que sobra do vetor após tirar os pivôs. Estes são os números que vamos distribuir.
    resto_da_lista = lista[qtd_pivos:]

    # ---------------------------------------------------------
    # FASE 2: CRIAÇÃO DOS BALDES DINÂMICOS NA MEMÓRIA
    # ---------------------------------------------------------
    # Se temos N pivôs, o vetor será fatiado em N + 1 intervalos (espaços entre os pivôs).
    intervalos = [[] for _ in range(qtd_pivos + 1)]
    
    # Criamos N baldes específicos para guardar números que sejam exatamentes iguais aos pivôs.
    iguais = [[p] for p in pivos] 

    # ---------------------------------------------------------
    # FASE 3: A DISTRIBUIÇÃO (O Fatiamento na Prática)
    # ---------------------------------------------------------
    for x in resto_da_lista:
        alocado = False
        
        # Testamos o número 'x' contra cada pivô, da esquerda para a direita
        for i in range(qtd_pivos):
            
            # Se 'x' for menor que a barreira do pivô atual, ele cai no balde correspondente
            if x < pivos[i]:
                intervalos[i].append(x)
                alocado = True
                break # Achou a casa dele, para de testar os outros pivôs
                
            # Se 'x' for empatado com o pivô, vai para o balde dos iguais
            elif x == pivos[i]:
                iguais[i].append(x)
                alocado = True
                break
                
        # O BALDE DOS GIGANTES (+ 1):
        # Se 'x' passou por todas as barreiras (todos os pivôs) e não era menor 
        # nem igual a ninguém, ele obrigatoriamente é maior que o último pivô.
        if not alocado:
            intervalos[-1].append(x)

    # ---------------------------------------------------------
    # FASE 4: RECURSÃO E MONTAGEM DO VETOR FINAL
    # ---------------------------------------------------------
    # Equivalente ao antigo: quick_sort(esquerda) + meio + quick_sort(direita)
    resultado = []
    
    # Roda a função novamente para ordenar cada pequeno intervalo e o junta com o seu pivô
    for i in range(qtd_pivos):
        resultado += quick_sort_multi(intervalos[i], num_pivos) + iguais[i]
        
    # Por fim, anexa o balde dos gigantes (o último intervalo gerado pelo N + 1)
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
vetor_teste_1 = quick_sort_multi(vetor_teste_1, num_pivos=3)

print("Ordenado perfeitamente: ", vetor_teste_1)