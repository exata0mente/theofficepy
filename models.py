class Personagem:
    def __init__(self, nome, cargo, idade, escritorio, frase_famosa):
        self.nome = nome
        self.cargo = cargo
        self.idade = idade
        self.escritorio = escritorio,
        self.frase_famosa = frase_famosa

    def imprimir_info(self):
        print("Nome:", self.nome)
        print("Cargo:", self.cargo)
        print("Idade:", self.idade)
        print("Escritório:", self.escritorio)
        print("Frase Famosa:", self.frase_famosa)
