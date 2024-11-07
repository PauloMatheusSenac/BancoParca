from Model.livros import Livros
from Model.main import Database

class ControllerLivro:
    def cadastrarLivro(self):
        bd = Database("10.28.2.59", "suporte", "suporte", "biblioteca")
        bd.conectar()

        livro = Livros("Dom Casmuurro", "Machado de Assis", "Suspense", 123)
        self.livro = Livros("Dom Casmuurro", "Machado de Assis", "Suspense", 123)
        try:
            bd.cursor.execute(livro.create())
            bd.conexao.commit()
            print("Livro cadastrado com sucesso!")
        except Exception as e:
            print(f"Erro ao cadastrar livro: {e}")
            bd.conexao.rollback()
        finally:
            bd.desconectar()

    def excluirLivro(self):
        bd = Database("10.28.2.59", "suporte", "suporte", "biblioteca")
        bd.conectar()

        livro = Livros("Dom Casmurro", "Machado de Assis", "Suspense", 123)
        try:
            bd.cursor.execute(livro.delete())
            bd.conexao.commit()
            print("Livro excluído com sucesso!")
        except Exception as e:
            print(f"Erro ao excluir livro: {e}")
            bd.conexao.rollback()
        finally:
            bd.desconectar()

    def atualizarLivro(self):
        bd = Database("10.28.2.59", "suporte", "suporte", "biblioteca")
        bd.conectar()

        livro = Livros("Dom Casmurro", "Machado de Assis", "Suspense", 123)
        novo_titulo = "Dom Casmurro - Edição Atualizada"
        novo_autor = "Machado de Assis"
        novo_status = "Indisponível"
        try:
            bd.cursor.execute(livro.update(novo_titulo=novo_titulo, novo_autor=novo_autor, novo_status=novo_status))
            bd.conexao.commit()
            print("Livro atualizado com sucesso!")
        except Exception as e:
            print(f"Erro ao atualizar livro: {e}")
            bd.conexao.rollback()
        finally:
            bd.desconectar()

    def consultarLivro(self):
        bd = Database("10.28.2.59", "suporte", "suporte", "biblioteca")
        bd.conectar()

        livro = self.livro
        #try:
        bd.cursor.execute(livro.select())
        resultado = bd.cursor.fetchall()
        for linha in resultado:
            print(linha)  
        #     else:
        #         print("Livro não encontrado.")
        # except Exception as e:
        #     print(f"Erro ao consultar livro: {e}")
        # finally:
        #     bd.desconectar()

 



controladora = ControllerLivro()

controladora.cadastrarLivro()

controladora.consultarLivro()

controladora.atualizarLivro()

controladora.excluirLivro()




