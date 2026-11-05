from produto import Produto

class CD(Produto):
    def __init__(self, id, nome, preco, estoque, faixas, duracao):
        super().__init__(id, nome, preco, estoque)
        self.faixas = faixas
        self.duracao = duracao

    def __str__(self):
        return f"CD: {self.nome} | R$ {self.preco:.2f} | Faixas: {self.faixas}"