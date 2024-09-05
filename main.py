def caminhoRED(arvore, no):
    print(no, end= " ")
    if arvore[no] != None:
        if arvore[no][0] != None:
            caminhoRED(arvore, arvore[no][0])
        if arvore[no][1] != None:
            caminhoRED(arvore, arvore[no][1])

def ordem(arvore, no):
    if arvore[no] != None:
        if arvore[no][0] != None:
            ordem(arvore, arvore[no][0])  
        print(no, end = " ")
        if(arvore[no][1] != None):
            ordem(arvore, arvore[no][1])    
    else:
        print(no, end = " ")

def posOrdem(arvore, no):
    if arvore[no] != None:
        if arvore[no][0] != None:
            posOrdem(arvore, arvore[no][0])            
        if arvore[no][1] != None:
            posOrdem(arvore, arvore[no][1])
        print(no, end = " ") 
    else:
        print(no, end= " ")

def exercicioA():
    print("Caminho em pré-ordem: ")
    caminhoRED(arvoreTeste2, 'A')
    print("\nCaminho em Ordem: ")
    ordem(arvoreTeste2, 'A')
    print("\nCaminho em pós-ordem")
    posOrdem(arvoreTeste2, 'A')

def exercicioB():
    return None

def exercicioC():
    return None

def exercicioD():
    return None

arvoreTeste = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['G', None],
    'D': None,
    'E': ['F', None],
    'F': None,
    'G': None
}

arvoreTeste2 = {    
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['G', 'H'],
    'D': ['I', 'J'],
    'E': ['K', 'L'],
    'G': ['O', 'P'],
    'H': ['Q', 'R'],
    'I': ['S', None],
    'J': None,
    'K': None,
    'L': ['T', None],
    'M': [None, 'U'],
    'N': None,
    'O': ['V', None],
    'P': None,
    'Q': [None, 'W'],
    'R': None,
    'S': None,
    'T': None,
    'U': None,
    'V': None,
    'W': None
}

exercicioA()
# entrada = input("Insira a arvore no formato: 'A': ['B', 'C'], 'B': ['A', 'D']\n")
# grafo = dict(eval("{" + entrada + "}"))
# for x in grafo.values():
#     print(x)