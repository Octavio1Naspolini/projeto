from datetime import date
from item_venda import ItemVenda

class Venda:
    def __init__(self, id, cliente):
        self.id = id
        self.data = date.today()
        self.cliente = cliente
        self.itens = []

    def adicionar_item(self, produto, quantidade):
        if produto.estoque >= quantidade:
            produto.estoque -= quantidade
            self.itens.append(ItemVenda(produto, quantidade))
        else:
            print(f"Estoque insuficiente: {produto.nome}")

    def total(self):
        return sum(item.subtotal() for item in self.itens)

    def mostrar(self):
        print(f"\nID: {self.id}")
        print(f"Data: {self.data}")
        print(f"Cliente: {self.cliente}")
        
        print("\nItens:")
        for item in self.itens:
            print(f"- Produto: {item.produto.nome} | Quantidade: {item.quantidade} | R$ {item.subtotal():.2f}")

        print(f"\nTotal: R$ {self.total():.2f}")