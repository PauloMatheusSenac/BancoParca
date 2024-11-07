from Model.livros import Livros
from Model.usuario import Usuario

class Biblioteca:
    Acervo:list[Livros] = []


    @staticmethod
    def emprestar(usuario: Usuario, livros: list[Livros] ):

        for item in livros:
            if len(usuario.lista_livros) == usuario.MAX_EMPRESTIMO:
                return
            usuario.pegar_emprestado(item)
            item.emprestar_livro(usuario)

    # @staticmethod
    # def devolver(livro: Livros, usuario: Usuario):
    #     livro.devolver_livro()
    #     usuario.