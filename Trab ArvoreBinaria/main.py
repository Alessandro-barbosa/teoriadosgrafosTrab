# main.py
import random
from arvore.arvore_binaria import ArvoreBinaria

def criar_arvore_aleatoria(num_nos):
    # Cria a árvore com o valor inicial aleatório
    valor_inicial = random.randint(1, 100)
    arvore = ArvoreBinaria(valor_inicial)

    # Insere valores aleatórios na árvore
    for _ in range(num_nos - 1):
        valor = random.randint(1, 100)
        arvore.inserir(valor)
    
    return arvore

# Define o número de nós que a árvore vai ter, minimo 1 nó e maximo 10.
NUM_NOS = random.randint(1, 10)

# cria uma árvore com valores aleatórios
arvore = criar_arvore_aleatoria(NUM_NOS)

# Caminhos pré-ordem, em ordem e pós-ordem
print("Caminho Pré-Ordem:", arvore.pre_ordem())
print("Caminho Em Ordem:", arvore.em_ordem())
print("Caminho Pós-Ordem:", arvore.pos_ordem())

# Altura da árvore
print("Altura da Árvore:", arvore.altura())

# Tipo da arvore
print("A árvore é cheia?", arvore.e_cheia())
print("A árvore é completa?", arvore.e_completa())
