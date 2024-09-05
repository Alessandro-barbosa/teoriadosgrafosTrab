def balanceda(arvore, no):
    esquerda = contarAltura(arvore, arvore[no][0])
    direita = contarAltura(arvore, arvore[no][1])
    diferenca = esquerda - direita
    if diferenca > 1 or diferenca < -1:
        return False
    else:
        return True


def contarAltura(arvore, no):
    if arvore[no] != None:
        if arvore[no][0] != None:
            esquerda = contarAltura(arvore, arvore[no][0]) + 1
        else:
            esquerda = 0;
        if arvore[no][1] != None:
            direita = contarAltura(arvore, arvore[no][1]) + 1
        else:
            direita = 0;
        if (direita > esquerda):
            return direita
        else:
            return esquerda;
    else:
        return 0;

def isBinario(arvore, no):
    if arvore[no] is not None:
        if len(arvore[no]) > 2:
            return False
        else:
            if arvore[no][0] is not None:
                if not isBinario(arvore, arvore[no][0]):
                    return False
            if arvore[no][1] is not None:
                if not isBinario(arvore, arvore[no][1]):
                    return False
    return True

def isDegenerada(arvore, no):
    if arvore[no] is not None:
        if arvore[no][0] is not None and arvore[no][1] is not None:
            return False
        elif arvore[no][0] is not None:
            return isDegenerada(arvore, arvore[no][0])
        elif arvore[no][1] is not None:
            return isDegenerada(arvore, arvore[no][1])
    return True

def isCheia(arvore, no):
    if arvore[no] is not None:
        if arvore[no][0] is None and arvore[no][1] is not None:
            return False
        elif arvore[no][0] is not None and arvore[no][1] is None:
            return False
        else:
            return isCheia(arvore, arvore[no][0]) and isCheia(arvore, arvore[no][1])
    return True

arvoreTeste = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['G', 'F'],
    'D': None,
    'E': [None, 'H'],
    'F': None,
    'G': None,
    'H': [None, 'S'],
    'S': None
}
arvoreDegen = {
    'A': ['B', None],
    'B': [None, 'C'],
    'C': ['D', None],
    'D': None
}
arvoreComp = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['G', 'F'],
    'D': None,
    'E': None,
    'G': None,
    'F': None
}

print("Balanceada? : " + str(balanceda(arvoreTeste, 'A')))
print("Binária? : " + str(isBinario(arvoreTeste, 'A')))
print("Degenerada? : " + str(isDegenerada(arvoreTeste, 'A')))
print("Cheia? : " + str(isCheia(arvoreComp, 'A')))
