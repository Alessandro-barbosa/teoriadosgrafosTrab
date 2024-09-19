def preOrdem(arvore, no):
    if no is None:
        return
    print(no, end=" ")
    if arvore[no] is not None:
        for filho in arvore[no]:
            if filho is not None:
                preOrdem(arvore, filho)


def ordem(arvore, no):
    if no is None:
        return

    # verifica se o nó atual tem filhos
    if arvore[no] is not None:
        filhos = arvore[no]

        if len(filhos) > 0 and filhos[0] is not None:
            ordem(arvore, filhos[0])
        print(no, end=" ")
        # filhos restantes
        for filho in filhos[1:]:
            if filho is not None:
                ordem(arvore, filho)
    else:
        print(no, end=" ")  # não tendo filhos, imprime o nó


def posOrdem(arvore, no):
    if no is None:
        return
    # nó existente na árvore
    if no in arvore:
        filhos = arvore[no]
        if filhos is not None:
            for filho in filhos:
                if filho is not None:
                    posOrdem(arvore, filho)

    # imprime o no raiz após todos
    print(no, end=" ")

