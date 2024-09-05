import random

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def gerar_arvore_aleatoria(n):
    if n == 0:
        return None
    raiz = No(random.randint(1, 10))
    nos = [raiz]
    for _ in range(n - 1):
        no = random.choice(nos)
        novo_no = No(random.randint(1, 10))
        if no.esquerda is None:
            no.esquerda = novo_no
        elif no.direita is None:
            no.direita = novo_no
        else:
            nos.remove(no)
            no = random.choice(nos)
            if no.esquerda is None:
                no.esquerda = novo_no
            else:
                no.direita = novo_no
        nos.append(novo_no)
    return raiz

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
        return 0
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

# Gerar uma árvore com um número de nós de 1 a 10
n = random.randint(1, 10)
arvore = gerar_arvore_aleatoria(n)

# Verificar o número total de nós
total_nos = contar_nos(arvore)

# Informações da Árvore
print("Árvore Gerada:")
print("Pré-ordem:", pre_ordem(arvore))
print("Em ordem:", em_ordem(arvore))
print("Pós-ordem:", pos_ordem(arvore))
print("Altura da árvore:", altura_arvore(arvore))
print("É uma árvore binária?:", verificar_arvore_binaria(arvore))
print("É uma árvore cheia?:", verificar_arvore_cheia(arvore))
print("É uma árvore completa?:", verificar_arvore_completa(arvore, 0, total_nos))
