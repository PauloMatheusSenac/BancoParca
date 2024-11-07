from Model.livros import Livros
from Model.usuario import Usuario
from biblioteca import Biblioteca
import mysql.connector

class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database


    def conectar(self):
        self.conexao = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database

        )
        self.cursor = self.conexao.cursor()

    def desconectar(self):
        self.conexao.close()


    
        
# rafaelatonta = Database("192.168.0.59","suporte","suporte","biblioteca")     
# rafaelatonta.conectar()
# print(vars(rafaelatonta.conexao))
# rafaelatonta.cursor.execute("select * from livro")
# print(rafaelatonta.cursor.fetchall())

# # print(vars(rafaelatonta.conexao))
# rafaelatonta.desconectar()
# print(vars(rafaelatonta.conexao))

# criar uma classe ControllerLivro
# sera responsavel por executar as querys SQL chamando o banco de dados e o livro
# ajustar a classe livro para que implemente um crud (a classe )