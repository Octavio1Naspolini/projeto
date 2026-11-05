from produto import Produto

class Livro(Produto):
    def __init__(self, id, nome, preco, estoque, editora, paginas):
        super().__init__(id, nome, preco, estoque)
        self.editora = editora
        self.paginas = paginas

    def __str__(self):
        return f"Livro: {self.nome} | R$ {self.preco:.2f} | Editora: {self.editora}"