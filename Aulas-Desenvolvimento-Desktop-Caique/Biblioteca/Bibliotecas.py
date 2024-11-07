from Livros import Livro
from Usuarios import Usuario


class Biblioteca:
    pass

    Acervo = []
    @staticmethod
    def emprestar(usuario:Usuario, livros:list(Livro)):
        for item in Livro:
            item.emprestar_livro(usuario)
            usuario.pegar_emprestado(livros)
    
    # @staticmethod
    # def devolver(livro:Livro , usuario:Usuario):
    #     livro.devolver_livro