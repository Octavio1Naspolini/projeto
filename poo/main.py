from cd import CD
from livro import Livro
from cliente import Cliente
from venda import Venda

# CDs
cd1 = CD(1, "Rock", 50, 10, 12, 60)
cd2 = CD(2, "Pop", 40, 10, 10, 50)
cd3 = CD(3, "Jazz", 60, 5, 8, 70)

# Livros
livro1 = Livro(4, "Python", 70, 10, "Editora A", 300)
livro2 = Livro(5, "POO", 90, 10, "Editora B", 400)
livro3 = Livro(6, "Algoritmos", 80, 10, "Editora C", 350)

# Cliente
cliente = Cliente(1, "Octavio", "octavionaspolinineto@gmail.com", "99610-5538")

# Venda
venda = Venda(1, cliente)

# Adicionando itens
venda.adicionar_item(cd1, 2)
venda.adicionar_item(cd2, 2)
venda.adicionar_item(livro1, 1)
venda.adicionar_item(livro2, 1)

# Mostrar venda
venda.mostrar()