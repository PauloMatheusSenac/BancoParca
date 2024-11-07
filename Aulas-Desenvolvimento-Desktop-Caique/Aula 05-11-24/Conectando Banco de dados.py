# Crie uma classe Database, a mesma deve instanciar um novo objeto utilizando o mysql connector;
# Deve ter um metodo para conectar e desconectar 
import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
            )

            if self.connection.is_connected():
                print(f"Conectado ao banco de dados {self.database} com sucesso.")
                
        except Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            self.connection = None

    def disconnect(self):
        if self.connection is not None and self.connection.is_connected():
            self.connection.close()
            print(f"Desconectado do banco de dados {self.database}.")
        else:
            print("Nenhuma conexão ativa para desconectar.")


db = Database(host='10.28.2.59', user='suporte', password='suporte', database='conexao')
db.connect()
db.disconnect()







