class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self, valor_raiz):
        self.raiz = No(valor_raiz)

    def inserir(self, valor):
        self._inserir_recursivo(self.raiz, valor)

    def _inserir_recursivo(self, no, valor):
        if valor < no.valor:
            if no.esquerda is None:
                no.esquerda = No(valor)
            else:
                self._inserir_recursivo(no.esquerda, valor)
        else:
            if no.direita is None:
                no.direita = No(valor)
            else:
                self._inserir_recursivo(no.direita, valor)

    def pre_ordem(self):
        return self._pre_ordem_recursivo(self.raiz, [])

    def _pre_ordem_recursivo(self, no, caminho):
        if no:
            caminho.append(no.valor)
            self._pre_ordem_recursivo(no.esquerda, caminho)
            self._pre_ordem_recursivo(no.direita, caminho)
        return caminho

    def em_ordem(self):
        return self._em_ordem_recursivo(self.raiz, [])

    def _em_ordem_recursivo(self, no, caminho):
        if no:
            self._em_ordem_recursivo(no.esquerda, caminho)
            caminho.append(no.valor)
            self._em_ordem_recursivo(no.direita, caminho)
        return caminho

    def pos_ordem(self):
        return self._pos_ordem_recursivo(self.raiz, [])

    def _pos_ordem_recursivo(self, no, caminho):
        if no:
            self._pos_ordem_recursivo(no.esquerda, caminho)
            self._pos_ordem_recursivo(no.direita, caminho)
            caminho.append(no.valor)
        return caminho

    def altura(self):
        return self._altura_recursiva(self.raiz)

    def _altura_recursiva(self, no):
        if no is None:
            return 0
        altura_esquerda = self._altura_recursiva(no.esquerda)
        altura_direita = self._altura_recursiva(no.direita)
        return 1 + max(altura_esquerda, altura_direita)

    def e_cheia(self):
        return self._e_cheia_recursiva(self.raiz)

    def _e_cheia_recursiva(self, no):
        if no is None:
            return True
        if no.esquerda is None and no.direita is None:
            return True
        if no.esquerda is not None and no.direita is not None:
            return self._e_cheia_recursiva(no.esquerda) and self._e_cheia_recursiva(no.direita)
        return False

    def e_completa(self):
        return self._e_completa_recursiva(self.raiz, 0, self._contar_nos(self.raiz))

    def _e_completa_recursiva(self, no, indice, total_nos):
        if no is None:
            return True
        if indice >= total_nos:
            return False
        return (self._e_completa_recursiva(no.esquerda, 2 * indice + 1, total_nos) and
                self._e_completa_recursiva(no.direita, 2 * indice + 2, total_nos))

    def _contar_nos(self, no):
        if no is None:
            return 0
        return 1 + self._contar_nos(no.esquerda) + self._contar_nos(no.direita)
