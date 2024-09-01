def caminhoRED(arvore, no):
    print(no , end=" ")
    # Se tiver filhos
    if arvore[no] != None:
        # Filho a esquerda
        caminhoRED(arvore, arvore[no][0])
        # Filho a direita
        if len(arvore[no]) > 1:
            caminhoRED(arvore, arvore[no][1])

def exercicioA():
    print("Caminho em pré-ordem: ")
    caminhoRED(arvoreTeste, 'A')

def exercicioB():
    return None

def exercicioC():
    return None

def exercicioD():
    return None

arvoreTeste = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['G'],
    'D': None,
    'E': ['F'],
    'F': None,
    'G': None
}

exercicioA()

# entrada = input("Insira a arvore no formato: 'A': ['B', 'C'], 'B': ['A', 'D']\n")
# grafo = dict(eval("{" + entrada + "}"))
# for x in grafo.values():
#     print(x)