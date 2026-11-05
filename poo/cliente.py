class Cliente:
    def __init__(self, id, nome, email, celular):
        self.id = id
        self.nome = nome
        self.email = email
        self.celular = celular

    def __str__(self):
        return f"{self.nome} ({self.email} - {self.celular})"