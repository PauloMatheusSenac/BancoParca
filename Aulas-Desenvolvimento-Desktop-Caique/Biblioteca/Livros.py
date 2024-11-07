import mysql.connector

class Livro():
    def __init__(self,titulo,autor,genero,cod_livro):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.status = "Disponivel"
        self.cod_livro = cod_livro
        self.usuario = None

    def emprestar_livro(self,usuario):
        if self.status != "Disponivel":
            return
        
        if len(usuario.lista_livros) == usuario.MAX_emprestimo:
            return "Maximo Atingido"

        self.usuario = usuario
        self.status = "Emprestado"

    def devolver_livro(self):
        if self.status != "Emprestado":
            return
        self.usuario = None
        self.status = "Disponivel"

    def criar_livro(self):
        teste = 0        
        teste.execute('INSERT INTO livro(titulo, autor, genero, status_livro, codigo) VALUES ("O pequeno principe", "Enzo", "Fantasia", "Disponivel", 5106106)') 
        teste.commit()
        print("Registro inserido com sucesso.")
    
