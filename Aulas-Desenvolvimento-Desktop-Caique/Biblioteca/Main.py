#from Bibliotecas import Biblioteca
#from Livros import Livro
#from Usuarios import Usuario
import mysql.connector

try:
    conexao = mysql.connector.connect(
        host='10.28.2.59',
        user='suporte',
        password='suporte',
        database='biblioteca',
    )

    if conexao.is_connected():
        print("Conexão bem-sucedida!")
        
        cursor = conexao.cursor()
        print(dir(conexao))
        
        cursor.execute('INSERT INTO livro(titulo, autor, genero, status_livro, codigo) VALUES ("O pequeno principe", "Enzo", "Fantasia", "Disponivel", 5106106)') 
        conexao.commit()
        print("Registro inserido com sucesso.")

        cursor.execute('INSERT INTO livro(titulo, autor, genero, status_livro, codigo) VALUES ("Nome teste", "Enzo", "Drama", "Disponivel", 464654)') 
        conexao.commit()
        print("Registro inserido com sucesso.")

        
        cursor.execute('UPDATE livro SET status_livro = "Indisponivel" WHERE titulo = "O pequeno principe" AND autor = "Enzo"')
        conexao.commit()
        print("Registro atualizado com sucesso.")

        
        cursor.execute('DELETE FROM livro WHERE titulo = "O pequeno principe" AND autor = "Enzo"')
        conexao.commit()
        print("Registro deletado com sucesso.")

        
        cursor.execute('SELECT * FROM livro ') 
        resultados = cursor.fetchall()
        print(resultados)




































except mysql.connector.Error as err:
    print(f"Erro: {err}")

finally:
    if 'conexao' in locals() and conexao.is_connected():
        conexao.close()
        print("Conexão encerrada.")




#     else:
#         print("Falha na conexão.")

# except mysql.connector.Error as err:
#     print(f"Erro: {err}")

# finally:
#     if 'conexao' in locals() and conexao.is_connected():
#         conexao.close()
#         print("Conexão encerrada.")





# import pymysql

# try:
#     conexao = pymysql.connect(
#         host='10.28.2.59',
#         user='suporte',
#         password='suporte',
#         database='biblioteca'
#     )

#     if conexao.open:
#         print("Conexão bem-sucedida!")
#         print(vars(conexao))
#     else:
#         print("Falha na conexão.")

# except pymysql.MySQLError as err:
#     print(f"Erro: {err}")

# finally:
#     if 'conexao' in locals() and conexao.open:
#         conexao.close()
#         print("Conexão encerrada.")



# rafaela = Usuario("Rafaela", "501651651065","654645654645")
# print(vars(rafaela))
# don_casmurro = Livro("Don Casmurro","Machado de Assis", "Drama", "2165165165")
# print(vars(don_casmurro))            
# incidente_antares = Livro("Incidente Antares","Erico Verissimo", "Drama", "2654545165")
# print(vars(don_casmurro))
# teste1 = Livro("Teste 1","Machado de Assis", "Drama", "46456465")
# print(vars(don_casmurro))
# teste2 = Livro("Teste 2","Machado de Assis", "Drama", "4564654548")
# print(vars(don_casmurro))
# teste3 = Livro("Teste 3","Machado de Assis", "Drama", "68746581654")
# print(vars(don_casmurro))
# Biblioteca.Acervo.append(don_casmurro)
# Biblioteca.Acervo.append(incidente_antares)
# Biblioteca.Acervo.append(teste1)
# Biblioteca.Acervo.append(teste2)
# Biblioteca.Acervo.append(teste3)

# rafaela.pegar_emprestado(don_casmurro)
# rafaela.pegar_emprestado(incidente_antares)
# rafaela.pegar_emprestado(teste1)
# rafaela.pegar_emprestado(teste2)
# rafaela.pegar_emprestado(teste3)

# don_casmurro.emprestar_livro(rafaela)
# incidente_antares.emprestar_livro(rafaela)
# teste1.emprestar_livro(rafaela)
# teste2.emprestar_livro(rafaela)
# teste3.emprestar_livro(rafaela)
        
# print(vars(rafaela))
# print(vars(rafaela))
# emprestimo1 = Biblioteca()
# emprestimo1.gerenciaremprestimo()

# ####################################################################################################################################################################################################################################

# class Usuario:
#     MAX_EMPRESTIMO = 5

#     def __init__(self, nome, id_usuario):
#         self.nome = nome
#         self.id_usuario = id_usuario
#         self.emprestimos = []

#     def emprestar(self, livro):
#         if len(self.emprestimos) < Usuario.MAX_EMPRESTIMO:
#             self.emprestimos.append(livro)
#             return True
#         return False

#     def devolver(self, livro):
#         if livro in self.emprestimos:
#             self.emprestimos.remove(livro)
#             return True
#         return False

# class Livro:
#     def __init__(self, titulo, autor, id_livro):
#         self.titulo = titulo
#         self.autor = autor
#         self.id_livro = id_livro
#         self.disponivel = True

#     def cadastrar(self):
#         return {"titulo": self.titulo, "autor": self.autor, "id_livro": self.id_livro}

# class Biblioteca:
#     usuarios = []
#     livros = []

#     @staticmethod
#     def cadastrar_usuario(nome, id_usuario):
#         usuario = Usuario(nome, id_usuario)
#         Biblioteca.usuarios.append(usuario)

#     @staticmethod
#     def cadastrar_livro(titulo, autor, id_livro):
#         livro = Livro(titulo, autor, id_livro)
#         Biblioteca.livros.append(livro)

#     @staticmethod
#     def listar_usuarios():
#         return [usuario.nome for usuario in Biblioteca.usuarios]

#     @staticmethod
#     def listar_livros():
#         return [livro.cadastrar() for livro in Biblioteca.livros]

#     @staticmethod
#     def emprestar_livro(id_usuario, id_livro):
#         usuario = next((u for u in Biblioteca.usuarios if u.id_usuario == id_usuario), None)
#         livro = next((l for l in Biblioteca.livros if l.id_livro == id_livro), None)

#         if usuario and livro and livro.disponivel:
#             if usuario.emprestar(livro):
#                 livro.disponivel = False
#                 return True
#         return False

#     @staticmethod
#     def devolver_livro(id_usuario, id_livro):
#         usuario = next((u for u in Biblioteca.usuarios if u.id_usuario == id_usuario), None)
#         livro = next((l for l in Biblioteca.livros if l.id_livro == id_livro), None)

#         if usuario and livro and not livro.disponivel:
#             if usuario.devolver(livro):
#                 livro.disponivel = True
#                 return True
#         return False

# class Interface:
#     @staticmethod
#     def criar_usuario(nome, id_usuario):
#         Biblioteca.cadastrar_usuario(nome, id_usuario)

#     @staticmethod
#     def criar_livro(titulo, autor, id_livro):
#         Biblioteca.cadastrar_livro(titulo, autor, id_livro)

#     @staticmethod
#     def listar_usuarios():
#         return Biblioteca.listar_usuarios()

#     @staticmethod
#     def listar_livros():
#         return Biblioteca.listar_livros()

#     @staticmethod
#     def emprestar_livro(id_usuario, id_livro):
#         return Biblioteca.emprestar_livro(id_usuario, id_livro)

#     @staticmethod
#     def devolver_livro(id_usuario, id_livro):
#         return Biblioteca.devolver_livro(id_usuario, id_livro)
