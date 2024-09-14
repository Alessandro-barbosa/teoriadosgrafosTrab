class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def criar_arvore(definicao, valor_atual):
    if valor_atual is None:
        return None
    no = No(valor_atual)
    filhos = definicao.get(valor_atual, None)
    if filhos:
        no.esquerda = criar_arvore(definicao, filhos[0])
        no.direita = criar_arvore(definicao, filhos[1])
    return no

arvore_1 = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': None,
    'E': None,
    'F': None,
    'G': None
}

arvore_2 = {
    'A': ['B', 'C'],
    'B': ['D', None],
    'C': ['E', None],
    'D': None,
    'E': ['F', 'G'],
    'F': None,
    'G': None
}

raiz_arvore_1 = criar_arvore(arvore_1, 'A')
raiz_arvore_2 = criar_arvore(arvore_2, 'A')

def pre_ordem(no):
    if no is None:
        return []
    return [no.valor] + pre_ordem(no.esquerda) + pre_ordem(no.direita)

def em_ordem(no):
    if no is None:
        return []
    return em_ordem(no.esquerda) + [no.valor] + em_ordem(no.direita)

def pos_ordem(no):
    if no is None:
        return []
    return pos_ordem(no.esquerda) + pos_ordem(no.direita) + [no.valor]

def altura_arvore(no):
    if no is None:
        return -1
    return 1 + max(altura_arvore(no.esquerda), altura_arvore(no.direita))

def verificar_arvore_binaria(no):
    def verificar(no):
        if no is None:
            return True, None
        if no.esquerda and no.direita:
            return True, no.valor
        if not (no.esquerda or no.direita):
            return True, no.valor
        if not no.esquerda:
            return verificar(no.direita)
        if not no.direita:
            return verificar(no.esquerda)
        return False, no.valor

    binaria, _ = verificar(no)
    return binaria

def verificar_arvore_cheia(no):
    if no is None:
        return True
    if no.esquerda is None and no.direita is None:
        return True
    if no.esquerda is not None and no.direita is not None:
        return verificar_arvore_cheia(no.esquerda) and verificar_arvore_cheia(no.direita)
    return False

def verificar_arvore_completa(no, indice, total_nos):
    if no is None:
        return True
    if indice >= total_nos:
        return False
    return (verificar_arvore_completa(no.esquerda, 2 * indice + 1, total_nos) and
            verificar_arvore_completa(no.direita, 2 * indice + 2, total_nos))

def contar_nos(no):
    if no is None:
        return 0
    return 1 + contar_nos(no.esquerda) + contar_nos(no.direita)

def analisar_arvore(raiz, nome):
    total_nos = contar_nos(raiz)
    print(f"Árvore {nome}:")
    print("Pré-ordem:", pre_ordem(raiz))
    print("Em ordem:", em_ordem(raiz))
    print("Pós-ordem:", pos_ordem(raiz))
    print("Altura da árvore:", altura_arvore(raiz))
    print("É uma árvore binária?:", verificar_arvore_binaria(raiz))
    print("É uma árvore cheia?:", verificar_arvore_cheia(raiz))
    print("É uma árvore completa?:", verificar_arvore_completa(raiz, 0, total_nos))
    print()

analisar_arvore(raiz_arvore_1, "1")
analisar_arvore(raiz_arvore_2, "2")
