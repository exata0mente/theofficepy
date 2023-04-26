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

class Funcionario:
    def __init__(self, nome, cargo):
        self._nome = nome
        self._cargo = cargo

    def imprimir_info(self):
        print("Nome:", self.nome)
        print("Cargo:", self.cargo)
    
    def get_nome(self):
        return self._nome

class Gerente(Funcionario):
    def __init__(self, nome, cargo, departamento):
        super().__init__(nome, cargo)
        self.departamento = departamento

    def imprimir_info(self):
        super().imprimir_info()
        print("Departamento:", self.departamento)

class Episodio:
    def __init__(self, numero, titulo, diretor, temporada):
        self.numero = numero
        self.titulo = titulo
        self.diretor = diretor
        self.temporada = temporada

    def imprimir_info(self):
        print("Episódio: {numero} - {titulo}".format(numero=self.numero, titulo=self.titulo))
        print("Título:", self.titulo)
        print("Diretor:", self.diretor)
        print("Personagens:")