class Usuario():
    MAX_emprestimo = 3
    def __init__(self, nome, cpf, telefone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.lista_livros = []

    def pegar_emprestado(self,livro):
        if len(self.lista_livros) == self.MAX_emprestimo:
            return "Limite atingido"
        
        self.lista_livros.append(livro.nome)