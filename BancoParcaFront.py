import tkinter as tk
from tkinter import messagebox
from BancoParcaBack import BancoDB
import random

#usuarios criados
#Tipo de Conta: Gerente Geral / Usuário: admin / Senha: senha_admin
#Tipo de Conta: Chefe de Setor / Usuário: chefe1 / Senha: senha_chefe
#Tipo de Conta: Funcionário / Usuário: funcionario1 / Senha: senha_funcionario
#Tipo de Conta: Cliente / Usuário: cliente1 / Senha: senha_cliente / Saldo: R$ 1.500,00
#Tipo de Conta: Cliente / Usuário: cliente2 / Senha: senha_cliente2 / Saldo: R$ 2.500,00
#Tipo de Conta: Cliente / Usuário: paulo / Senha: paulo / Saldo: R$ 3.000,00
#Tipo de Conta: Cliente / Usuário: rafaela / Senha: rafaela / Saldo: R$ 1.200,00
#Tipo de Conta: Cliente / Usuário: carlos / Senha: carlos / Saldo: R$ 1.800,00
#Tipo de Conta: Cliente / Usuário: gabriel / Senha: gabriel / Saldo: R$ 2.200,00
#Tipo de Conta: Cliente / Usuário: davi / Senha: davi / Saldo: R$ 1.600,00




class BancoApp:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Bem Vindo ao Banco Parça")
        self.raiz.geometry("400x350")
        self.db = BancoDB()
        self.criar_widgets_login()

    def criar_widgets_login(self):
        quadro = tk.Frame(self.raiz)
        quadro.place(relx=0.5, rely=0.5, anchor='center')

        tk.Label(quadro, text="Titular:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.entry_titular_login = tk.Entry(quadro)
        self.entry_titular_login.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(quadro, text="Senha:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.entry_senha_login = tk.Entry(quadro, show="*")
        self.entry_senha_login.grid(row=1, column=1, padx=10, pady=5)

        tk.Button(quadro, text="Login", command=self.login).grid(row=2, column=0, columnspan=2, pady=10)

    def login(self):
        titular = self.entry_titular_login.get()
        senha = self.entry_senha_login.get()
        perfil = self.db.autenticar_usuario(titular, senha)
        if perfil:
            messagebox.showinfo("Sucesso", f"Usuário autenticado como: {perfil}")
            self.criar_widgets_principal(perfil)
        else:
            messagebox.showerror("Erro", "Falha na autenticação.")

    def criar_widgets_principal(self, perfil):
        for widget in self.raiz.winfo_children():
            widget.destroy()

        if perfil == 'Cliente':
            self.criar_widgets_cliente()
        elif perfil == 'Gerente Geral':
            self.criar_widgets_gerente()
        elif perfil == 'Chefe de Setor':
            self.criar_widgets_chefe()
        elif perfil == 'Funcionário':
            self.criar_widgets_funcionario()
        elif perfil == 'Administrador':
            self.criar_widgets_administrador()

    def criar_widgets_administrador(self):
        label = tk.Label(self.raiz, text="Bem-vindo, Administrador!")
        label.pack(pady=20)

        # Adicione ações para o administrador aqui
        tk.Button(self.raiz, text="Gerenciar Funcionários", command=self.gerenciar_funcionarios).pack(pady=5)
        tk.Button(self.raiz, text="Sair", command=self.sair).pack(pady=5)

    def gerenciar_funcionarios(self):
        # Placeholder para gerenciamento de funcionários
        messagebox.showinfo("Gerenciar Funcionários", "Funcionalidade em desenvolvimento!")

    def sair(self):
        self.raiz.destroy()  # Fecha a aplicação

    def criar_widgets_cliente(self):
        self.label_titular = tk.Label(self.raiz, text="Titular:")
        self.label_titular.grid(row=0, column=0)
        self.entry_titular = tk.Entry(self.raiz)
        self.entry_titular.grid(row=0, column=1)

        self.label_cpf = tk.Label(self.raiz, text="CPF:")
        self.label_cpf.grid(row=1, column=0)
        self.entry_cpf = tk.Entry(self.raiz)
        self.entry_cpf.grid(row=1, column=1)

        self.label_numero_conta = tk.Label(self.raiz, text="Número da Conta:")
        self.label_numero_conta.grid(row=2, column=0)
        self.entry_numero_conta = tk.Entry(self.raiz)
        self.entry_numero_conta.grid(row=2, column=1)

        tk.Label(self.raiz, text="Valor:").grid(row=3, column=0)
        self.entry_valor = tk.Entry(self.raiz)
        self.entry_valor.grid(row=3, column=1)

        tk.Button(self.raiz, text="Depositar", command=self.depositar).grid(row=4, column=0)
        tk.Button(self.raiz, text="Sacar", command=self.sacar).grid(row=4, column=1)
        tk.Button(self.raiz, text="Transferir", command=self.transferir).grid(row=5, column=0)
        tk.Button(self.raiz, text="Consultar Saldo", command=self.consultar_saldo).grid(row=5, column=1)
        tk.Button(self.raiz, text="Solicitar Empréstimo", command=self.solicitar_emprestimo).grid(row=6, column=0)

        tk.Label(self.raiz, text="Destinatário (para Transferir):").grid(row=7, column=0)
        self.entry_destino = tk.Entry(self.raiz)
        self.entry_destino.grid(row=7, column=1)

    def depositar(self):
        titular = self.entry_titular.get()
        try:
            valor = float(self.entry_valor.get())
            if self.db.depositar(titular, valor):
                messagebox.showinfo("Sucesso", "Depósito realizado com sucesso!")
            else:
                messagebox.showerror("Erro", "Falha ao realizar depósito.")
        except ValueError:
            messagebox.showerror("Erro", "Valor inválido.")

    def sacar(self):
        titular = self.entry_titular.get()
        try:
            valor = float(self.entry_valor.get())
            if not self.db.sacar(titular, valor):
                messagebox.showwarning("Aviso", "Saldo insuficiente. Você deseja solicitar um empréstimo?")
        except ValueError:
            messagebox.showerror("Erro", "Valor inválido.")

    def transferir(self):
        titular_origem = self.entry_titular.get()
        titular_destino = self.entry_destino.get()
        try:
            valor = float(self.entry_valor.get())
            if self.db.transferir(titular_origem, titular_destino, valor):
                messagebox.showinfo("Sucesso", "Transferência realizada com sucesso!")
            else:
                messagebox.showerror("Erro", "Falha ao realizar transferência.")
        except ValueError:
            messagebox.showerror("Erro", "Valor inválido.")

    def consultar_saldo(self):
        titular = self.entry_titular.get()
        saldo = self.db.consultar_saldo(titular)
        if saldo is not None:
            messagebox.showinfo("Saldo", f"O saldo da conta é: R${saldo:.2f}")
        else:
            messagebox.showerror("Erro", "Conta não encontrada.")

    def solicitar_emprestimo(self):
        titular = self.entry_titular.get()
        try:
            valor = float(self.entry_valor.get())
            if self.db.solicitar_emprestimo(titular, valor):
                messagebox.showinfo("Sucesso", "Solicitação de empréstimo realizada com sucesso!")
            else:
                messagebox.showerror("Erro", "Falha ao solicitar empréstimo.")
        except ValueError:
            messagebox.showerror("Erro", "Valor inválido.")

    def criar_widgets_gerente(self):
        self.label_titular = tk.Label(self.raiz, text="Titular:")
        self.label_titular.grid(row=0, column=0)
        self.entry_titular = tk.Entry(self.raiz)
        self.entry_titular.grid(row=0, column=1)

        self.label_cpf = tk.Label(self.raiz, text="CPF:")
        self.label_cpf.grid(row=1, column=0)
        self.entry_cpf = tk.Entry(self.raiz)
        self.entry_cpf.grid(row=1, column=1)

        self.label_numero_conta = tk.Label(self.raiz, text="Número da Conta:")
        self.label_numero_conta.grid(row=2, column=0)
        self.entry_numero_conta = tk.Entry(self.raiz)
        self.entry_numero_conta.grid(row=2, column=1)

        tk.Label(self.raiz, text="Senha:").grid(row=3, column=0)
        self.entry_senha = tk.Entry(self.raiz, show="*")
        self.entry_senha.grid(row=3, column=1)

        tk.Button(self.raiz, text="Criar Conta", command=self.criar_conta).grid(row=4, column=0)
        tk.Button(self.raiz, text="Autorizar Conta", command=self.autorizar_conta).grid(row=4, column=1)

        tk.Button(self.raiz, text="Excluir Conta", command=self.excluir_conta).grid(row=5, column=1, padx=10, pady=5, sticky="e")
        tk.Button(self.raiz, text="Listar Contas", command=self.listar_contas).grid(row=5, column=0, padx=20, pady=10, sticky="w")

    def criar_conta(self):
        titular = self.entry_titular.get()
        cpf = self.entry_cpf.get()
        numero_conta = self.entry_numero_conta.get()
        senha = self.entry_senha.get()

        if not self.db.verificar_cpf(cpf):
            if self.db.criar_conta(titular, cpf, numero_conta, senha):
                messagebox.showinfo("Sucesso", "Conta criada com sucesso!")
            else:
                messagebox.showerror("Erro", "Falha ao criar conta.")
        else:
            messagebox.showerror("Erro", "CPF já cadastrado.")

    

    def autorizar_conta(self):
        titular = self.entry_titular.get()
        if self.db.autorizar_conta(titular):
            messagebox.showinfo("Sucesso", "Conta autorizada com sucesso!")
        else:
            messagebox.showerror("Erro", "Falha ao autorizar conta.")

    def excluir_conta(self):
        titular = self.entry_titular.get()
        if self.db.excluir_conta(titular):
            messagebox.showinfo("Sucesso", "Conta excluída com sucesso!")
        else:
            messagebox.showerror("Erro", "Falha ao excluir conta.")

    def listar_contas(self):
        contas = self.db.listar_contas()
        if contas:
            contas_texto = "\n".join([f"Usuario: {titular}, Saldo: R${cpf}, CPF: {numero_conta}, Numero da Conta: {saldo}, Status: {status}" for (titular, cpf, numero_conta, saldo, status) in contas])
            messagebox.showinfo("Contas", contas_texto)
        else:
            messagebox.showinfo("Contas", "Nenhuma conta encontrada.")

    def criar_widgets_chefe(self):
        # Interface placeholder para chefe de setor
        label = tk.Label(self.raiz, text="Bem-vindo, Chefe de Setor!")
        label.pack(pady=20)

    def criar_widgets_funcionario(self):
        # Interface placeholder para funcionário
        label = tk.Label(self.raiz, text="Bem-vindo, Funcionário!")
        label.pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = BancoApp(root)
    root.mainloop()
