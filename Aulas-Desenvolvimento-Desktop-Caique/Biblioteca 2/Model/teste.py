import mysql.connector
from mysql.connector import Error

try:
    # Tente conectar ao banco de dados
    conn = mysql.connector.connect(
        host="10.28.2.59",  # ou 127.0.0.1
        user="suporte",       # ou o seu usuário
        password="suporte",       # ou a sua senha, se houver
        database="biblioteca"  # nome do banco de dados
    )
    if conn.is_connected():
        print("Conectado ao MySQL com sucesso!")
except Error as e:
    print(f"Erro ao conectar ao MySQL: {e}")
finally:
    if conn.is_connected():
        conn.close()
