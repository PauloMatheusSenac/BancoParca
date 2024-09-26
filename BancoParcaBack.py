import mysql.connector

class BancoDB:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="10.28.2.59",
            user="suporte",
            password="suporte",
            database="bancoparca"
        )
        self.cursor = self.conn.cursor()

    def autenticar_usuario(self, titular, senha):
        try:
            self.cursor.execute("SELECT tipo_perfil FROM perfis WHERE titular = %s AND senha = %s", (titular, senha))
            perfil = self.cursor.fetchone()
            return perfil[0] if perfil else None
        except mysql.connector.Error as err:
            print(f"Erro: {err}")
            return None

    def cadastrar_titular(self, titular, cpf, senha, tipo_perfil='Funcionário'):
        if self.verificar_cpf(cpf):
            print("CPF já cadastrado.")
            return False
        try:
            self.cursor.execute("INSERT INTO perfis (titular, cpf, senha, tipo_perfil) VALUES (%s, %s, %s, %s)", 
                                (titular, cpf, senha, tipo_perfil))
            self.conn.commit()
            return True
        except mysql.connector.Error as e:
            print(f"Erro ao cadastrar titular: {e}")
            self.conn.rollback()
            return False

    def criar_conta(self, titular, cpf, numero_conta, senha):
        if not self.verificar_cpf(cpf):
            if not self.cadastrar_titular(titular, cpf, senha):
                print("Falha ao cadastrar o titular. Conta não criada.")
                return False
        
        try:
            self.cursor.execute("INSERT INTO contas (titular, cpf, numero_conta, status, saldo) VALUES (%s, %s, %s, %s, %s)", 
                                (titular, cpf, numero_conta, 'Ativa', 0.0))  # Inicializa saldo como 0.0
            self.conn.commit()
            return True
        except mysql.connector.Error as err:
            print(f"Erro: {err}")
            self.conn.rollback()
            return False
        
    

    def excluir_conta(self, titular):
        try:
            self.cursor.execute("DELETE FROM contas WHERE titular = %s", (titular,))
            self.cursor.execute("DELETE FROM perfis WHERE titular = %s", (titular,))
            self.conn.commit()
            return True
        except mysql.connector.Error as err:
            print(f"Erro ao excluir conta: {err}")
            self.conn.rollback()
            return False

    def listar_contas(self):
        try:
            self.cursor.execute("SELECT * FROM contas")
            contas = self.cursor.fetchall()
            return [(titular, float(cpf), numero_conta, saldo, status) for (id_conta, titular, cpf, numero_conta, saldo, status) in contas]
        except mysql.connector.Error as err:
            print(f"Erro ao listar contas: {err}")
            return []

    def autorizar_conta(self, titular):
        try:
            self.cursor.execute("UPDATE contas SET status = 'Ativa' WHERE titular = %s", (titular,))
            self.conn.commit()
            return True
        except mysql.connector.Error as err:
            print(f"Erro ao autorizar conta: {err}")
            self.conn.rollback()
            return False

    def depositar(self, titular, valor):
        try:
            self.cursor.execute("UPDATE contas SET saldo = saldo + %s WHERE titular = %s AND status = 'Ativa'", (valor, titular))
            self.conn.commit()
            return True
        except mysql.connector.Error as err:
            print(f"Erro ao depositar: {err}")
            self.conn.rollback()
            return False

    def sacar(self, titular, valor):
        try:
            self.cursor.execute("SELECT saldo FROM contas WHERE titular = %s AND status = 'Ativa'", (titular,))
            saldo = self.cursor.fetchone()
            if saldo and saldo[0] >= valor:
                self.cursor.execute("UPDATE contas SET saldo = saldo - %s WHERE titular = %s", (valor, titular))
                self.conn.commit()
                return True
            else:
                print("Saldo insuficiente.")
                return False
        except mysql.connector.Error as err:
            print(f"Erro ao sacar: {err}")
            self.conn.rollback()
            return False

    def transferir(self, titular_origem, titular_destino, valor):
        if self.sacar(titular_origem, valor):
            return self.depositar(titular_destino, valor)
        return False
    
    def consultar_saldo(self, titular):
        try:
            self.cursor.execute("SELECT saldo FROM contas WHERE titular = %s", (titular,))
            saldo = self.cursor.fetchone()
            return saldo[0] if saldo else None
        except mysql.connector.Error as err:
            print(f"Erro ao consultar saldo: {err}")
            return None
    
    def listar_funcionarios(self):
        try:
            self.cursor.execute("SELECT * FROM perfis WHERE tipo_perfil = 'Funcionário'")
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            print(f"Erro ao listar funcionários: {err}")
            return []

    def solicitar_emprestimo(self, cpf_cliente, valor):
        try:
            self.cursor.execute("INSERT INTO emprestimos (cpf_cliente, valor) VALUES (%s, %s)", (cpf_cliente, valor))
            self.conn.commit()
            return True
        except mysql.connector.Error as err:
            print(f"Erro ao solicitar empréstimo: {err}")
            self.conn.rollback()
            return False

    def verificar_cpf(self, cpf):
        try:
            self.cursor.execute("SELECT COUNT(*) FROM perfis WHERE cpf = %s", (cpf,))
            return self.cursor.fetchone()[0] > 0
        except mysql.connector.Error as err:
            print(f"Erro ao verificar CPF: {err}")
            return False

    def fechar_conexao(self):
        self.cursor.close()
        self.conn.close()
