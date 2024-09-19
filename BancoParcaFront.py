import tkinter as tk
from tkinter import messagebox
from BancoParcaBack import BancoDB

#'Gerente Geral', 'admin', 'senha_admin'
#'Cliente', 'cliente1', 'senha_cliente' 
#'Cliente', 'cliente2', 'senha_cliente2'
#'Cliente', 'paulo', 'paulo', '1234567895' 
#'Cliente', 'rafaela', 'rafaela', '1234567896'
#'Cliente', 'carlos', 'carlos', '1234567897'
#'Cliente', 'gabriel', 'gabriel', '1234567898'
#'Cliente', 'davi', 'davi', '1234567899'



class BancoApp:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Bem Vindo ao Banco Parça")
        self.raiz.geometry("350x200")
        self.db = BancoDB()

        self.criar_widgets_login()

    def criar_conta(self):
        titular = self.entry_titular.get()
        cpf = self.entry_cpf.get()
        numero_conta = self.entry_numero_conta.get()
        
        if self.db.criar_conta(titular, cpf, numero_conta):
            messagebox.showinfo("Sucesso", "Conta criada com sucesso!")
        else:
            messagebox.showerror("Erro", "Falha ao criar conta.")

    def consultar_conta(self):
        cpf = self.entry_cpf.get()
        numero_conta = self.entry_numero_conta.get()
        saldo = self.db.consultar_saldo(cpf=cpf) or self.db.consultar_saldo(numero_conta=numero_conta)
        
        if saldo is not None:
            messagebox.showinfo("Saldo", f"O saldo da conta é: R${saldo:.2f}")
        else:
            messagebox.showerror("Erro", "Conta não encontrada.")

    def excluir_conta(self):
        cpf = self.entry_cpf.get()
        numero_conta = self.entry_numero_conta.get()
        
        if self.db.excluir_conta(cpf=cpf) or self.db.excluir_conta(numero_conta=numero_conta):
            messagebox.showinfo("Sucesso", "Conta excluída com sucesso!")
        else:
            messagebox.showerror("Erro", "Falha ao excluir conta.")


    def criar_widgets_login(self):
        quadro = tk.Frame(self.raiz)
        quadro.place(relx=0.5, rely=0.5, anchor='center')

        self.label_titular_login = tk.Label(quadro, text="Titular:")
        self.label_titular_login.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.entry_titular_login = tk.Entry(quadro)
        self.entry_titular_login.grid(row=0, column=1, padx=10, pady=5)

        self.label_senha_login = tk.Label(quadro, text="Senha:")
        self.label_senha_login.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.entry_senha_login = tk.Entry(quadro, show="*")
        self.entry_senha_login.grid(row=1, column=1, padx=10, pady=5)

        self.botao_login = tk.Button(quadro, text="Login", command=self.login)
        self.botao_login.grid(row=2, column=0, columnspan=2, pady=10)

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

    def criar_widgets_cliente(self):
        self.label_titular = tk.Label(self.raiz, text="Titular:")
        self.label_titular.grid(row=0, column=0)
        self.entry_titular = tk.Entry(self.raiz)
        self.entry_titular.grid(row=0, column=1)

        self.label_valor = tk.Label(self.raiz, text="Valor:")
        self.label_valor.grid(row=1, column=0)
        self.entry_valor = tk.Entry(self.raiz)
        self.entry_valor.grid(row=1, column=1)

        self.label_destino = tk.Label(self.raiz, text="Destino (CPF ou Número da Conta):")
        self.label_destino.grid(row=2, column=0)
        self.entry_destino = tk.Entry(self.raiz)
        self.entry_destino.grid(row=2, column=1)

        self.botao_deposito = tk.Button(self.raiz, text="Depositar", command=self.depositar)
        self.botao_deposito.grid(row=3, column=0)

        self.botao_saque = tk.Button(self.raiz, text="Sacar", command=self.sacar)
        self.botao_saque.grid(row=3, column=1)

        self.botao_transferir = tk.Button(self.raiz, text="Transferir", command=self.transferir)
        self.botao_transferir.grid(row=4, column=0)

        self.botao_consultar_saldo = tk.Button(self.raiz, text="Consultar Saldo", command=self.consultar_saldo)
        self.botao_consultar_saldo.grid(row=4, column=1)


    def excluir_conta(self):
        titular = self.entry_titular.get()
        if self.db.excluir_conta(titular):
            messagebox.showinfo("Sucesso", "Conta excluída com sucesso!")
        else:
            messagebox.showerror("Erro", "Falha ao excluir conta.")

    def consultar_conta(self):
        titular = self.entry_titular.get()
        saldo = self.db.consultar_saldo(titular)
        if saldo is not None:
            messagebox.showinfo("Saldo", f"O saldo da conta é: R${saldo:.2f}")
        else:
            messagebox.showerror("Erro", "Conta não encontrada.")

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

        self.botao_criar_conta = tk.Button(self.raiz, text="Criar Conta", command=self.criar_conta)
        self.botao_criar_conta.grid(row=3, column=0, padx=20, pady=5, sticky="w")

        self.botao_excluir_conta = tk.Button(self.raiz, text="Excluir Conta", command=self.excluir_conta)
        self.botao_excluir_conta.grid(row=3, column=1, padx=10, pady=5, sticky="e")

        self.botao_listar_contas = tk.Button(self.raiz, text="Listar Contas", command=self.listar_contas)
        self.botao_listar_contas.grid(row=4, column=0, padx=20, pady=10, sticky="w")

        self.botao_consultar_conta = tk.Button(self.raiz, text="Consultar Conta", command=self.consultar_conta)
        self.botao_consultar_conta.grid(row=4, column=1, padx=10, pady=10, sticky="e")


    def criar_widgets_chefe(self):
        self.label_titular = tk.Label(self.raiz, text="Titular:")
        self.label_titular.grid(row=0, column=0)
        self.entry_titular = tk.Entry(self.raiz)
        self.entry_titular.grid(row=0, column=1)

        self.botao_criar_funcionario = tk.Button(self.raiz, text="Criar Funcionário", command=self.criar_funcionario)
        self.botao_criar_funcionario.grid(row=1, column=0, columnspan=2)

    def criar_widgets_funcionario(self):
        self.label_titular = tk.Label(self.raiz, text="Titular:")
        self.label_titular.grid(row=0, column=0)
        self.entry_titular = tk.Entry(self.raiz)
        self.entry_titular.grid(row=0, column=1)

        self.botao_autorizar_movimentacao = tk.Button(self.raiz, text="Autorizar Movimentação", command=self.autorizar_movimentacao)
        self.botao_autorizar_movimentacao.grid(row=1, column=0, columnspan=2)

    def depositar(self):
        titular = self.entry_titular.get()
        valor = float(self.entry_valor.get())
        if self.db.depositar(titular, valor):
            messagebox.showinfo("Sucesso", "Depósito realizado com sucesso!")
        else:
            messagebox.showerror("Erro", "Falha ao realizar depósito.")

    def sacar(self):
        titular = self.entry_titular.get()
        valor = float(self.entry_valor.get())
        if self.db.sacar(titular, valor):
            messagebox.showinfo("Sucesso", "Saque realizado com sucesso!")
        else:
            messagebox.showerror("Erro", "Falha ao realizar saque ou saldo insuficiente.")

    def transferir(self):
        titular_origem = self.entry_titular.get()
        valor = float(self.entry_valor.get())
        destino = self.entry_destino.get()

        
        if destino.isdigit() and len(destino) == 11:  
            if self.db.transferir(titular_origem, valor, cpf_destino=destino):
                messagebox.showinfo("Sucesso", "Transferência realizada com sucesso!")
            else:
                messagebox.showerror("Erro", "Falha ao realizar transferência.")
        elif destino.isalnum():  
            if self.db.transferir(titular_origem, valor, numero_conta_destino=destino):
                messagebox.showinfo("Sucesso", "Transferência realizada com sucesso!")
            else:
                messagebox.showerror("Erro", "Falha ao realizar transferência.")
        else:
            messagebox.showerror("Erro", "Formato de destino inválido.")





    def consultar_saldo(self):
        titular = self.entry_titular.get()
        saldo = self.db.consultar_saldo(titular)
        if saldo is not None:
            messagebox.showinfo("Saldo", f"O saldo da conta é: R${saldo:.2f}")
        else:
            messagebox.showerror("Erro", "Falha ao consultar saldo.")

    def criar_conta(self):
        titular = self.entry_titular.get()
        if self.db.criar_conta(titular):
            messagebox.showinfo("Sucesso", "Conta criada com sucesso!")
        else:
            messagebox.showerror("Erro", "Falha ao criar conta.")

    def listar_contas(self):
        contas = self.db.listar_contas()
        contas_str = "\n".join([f"Titular: {c[1]}, Saldo: R${c[2]:.2f}" for c in contas])
        messagebox.showinfo("Contas", contas_str)

    def criar_funcionario(self):
        pass

    def autorizar_movimentacao(self):
        pass

raiz = tk.Tk()
app = BancoApp(raiz)
raiz.mainloop()


