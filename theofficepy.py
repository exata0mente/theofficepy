class Personagem:
    def __init__(self, nome, cargo, idade, escritorio, nacionalidade=None):
        self._nome = nome
        self._cargo = cargo
        self._idade = idade
        self._escritorio = escritorio
        self._nacionalidade = nacionalidade
        self._numero_episodios = 0
        self._link_dunderpedia = ""    
        self._participacoes = dict()
        self._relacionamentos = dict()
        self._filhos = []
        self._familiares = {}

    def __str__(self):
        info = f"Nome: {self._nome}\n"
        info += f"Idade: {self._idade}\n"
        info += f"Cargo: {self._cargo}\n"
        info += f"Relacionamentos:\n"
        if len(self._relacionamentos):
            for personagem, tipo_relacionamento in self._relacionamentos.items():
                info += f"- {personagem._nome} ({tipo_relacionamento})\n"
        return info
    
    def verifica_relacionamento(self, personagem):
        if personagem in self._relacionamentos:
            return True
        else:
            return False
    
    def adiciona_relacionamento(self, personagem, tipo_relacionamento, atualiza_relacionamento=False):
        if not isinstance(personagem, Personagem):
            raise TypeError("O personagem deve ser uma instância da classe Personagem")

        if self.verifica_relacionamento(personagem):
            if atualiza_relacionamento:
                self._relacionamentos.update({personagem: tipo_relacionamento})
            else:
                raise ValueError("O relacionamento já existe, definir atualiza_relacionamento=True para atualizar o relacionamento")
        else:
            self._relacionamentos[personagem] = tipo_relacionamento

    def atualiza_informacoes(self, nome=None, cargo=None, idade=None, escritorio=None):
        if nome:
            self._nome = nome
        if cargo:
            self._cargo = cargo
        if idade:
            self._idade = idade
        if escritorio:
            self._escritorio = escritorio
    
    def get_relacionamentos(self):
        info = f"Relacionamentos:"
        for objeto_personagem, relacionamento in self._relacionamentos.items():
            info += " {} : {}, ".format(objeto_personagem._nome, relacionamento)
        return info
        

class Episodio(Personagem):
 
        def __init__(self, nome, temporada, numero, diretor, roteirista, data, link_imdb="", link_dunderpedia="", participacoes=list()):
            self._nome = nome
            self._temporada = temporada
            self._numero = numero
            self._diretor = diretor
            self._data = data
            self._link_imdb = link_imdb
            self._link_dunderpedia = link_dunderpedia
            self._participacoes = participacoes

        def __str__(self):
            info = f"Nome: {self._nome}\n"
            info += f"Temporada: {self._temporada}\n"
            info += f"Numero: {self._numero}\n"
            info += f"Diretor: {self._diretor}\n"
            info += f"Data: {self._data}\n"
            info += f"Participações:\n"

            nome_personagens = []
            [nome_personagens.append(personagem._nome) for personagem in self._participacoes if personagem._nome not in nome_personagens]
            for personagem_episodio in nome_personagens:
                info += f"- {personagem_episodio}\n"
            return info
        
class TheOffice:
    def __init__(self):
        self.personagens = []

    def adicionar_personagem(self, nome, idade, cargo, relacionamentos=dict()):
        novo_personagem = Personagem(nome, idade, cargo, relacionamentos)
        self.personagens.append(novo_personagem)

    def remover_personagem(self, nome):
        for personagem in self.personagens:
            if personagem.nome == nome:
                self.personagens.remove(personagem)
                return f"Personagem {nome} removido com sucesso!"
        return f"Personagem {nome} não encontrado no sistema."
    
    def get_personagens(self):
        info = "Personagens:\n"
        for personagem in self.personagens:
            info += f"- {personagem._nome}\n"
        return info

