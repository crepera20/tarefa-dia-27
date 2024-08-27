import tkinter as tk
from tkinter import messagebox
import os
import sys

# Supondo que você tenha uma classe Cidade definida em cidades_model
from cidades_model import Cidade

class Application:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Cidade")
        self.root.state("zoomed")  # Aumenta o tamanho da janela

        # Frame para centralizar os widgets
        self.frame = tk.Frame(root)
        self.frame.pack(expand=True)  # Expande para ocupar o espaço disponível

        # Widgets
        self.lblNome = tk.Label(self.frame, text="Nome:", font=("Arial", 18))
        self.lblNome.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.txtNome = tk.Entry(self.frame, font=("Arial", 18))
        self.txtNome.grid(row=0, column=1, padx=10, pady=10)

        self.lblTelefone = tk.Label(self.frame, text="Telefone:", font=("Arial", 18))
        self.lblTelefone.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.txtTelefone = tk.Entry(self.frame, font=("Arial", 18))
        self.txtTelefone.grid(row=1, column=1, padx=10, pady=10)

        self.lblEmail = tk.Label(self.frame, text="E-mail:", font=("Arial", 18))
        self.lblEmail.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.txtEmail = tk.Entry(self.frame, font=("Arial", 18))
        self.txtEmail.grid(row=2, column=1, padx=10, pady=10)

        self.lblUsuario = tk.Label(self.frame, text="Usuário:", font=("Arial", 18))
        self.lblUsuario.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        self.txtUsuario = tk.Entry(self.frame, font=("Arial", 18))
        self.txtUsuario.grid(row=3, column=1, padx=10, pady=10)

        self.lblSenha = tk.Label(self.frame, text="Senha:", font=("Arial", 18))
        self.lblSenha.grid(row=4, column=0, padx=10, pady=10, sticky="e")
        self.txtSenha = tk.Entry(self.frame, font=("Arial", 18), show="*")
        self.txtSenha.grid(row=4, column=1, padx=10, pady=10)

        # Botões
        self.btnInserir = tk.Button(self.frame, text="Inserir", command=self.inserir_usuario, font=("Arial", 18))
        self.btnInserir.grid(row=5, column=0, padx=10, pady=10)

        self.btnAlterar = tk.Button(self.frame, text="Alterar", command=self.alterar_usuario, font=("Arial", 18))
        self.btnAlterar.grid(row=5, column=1, padx=10, pady=10)

        self.btnExcluir = tk.Button(self.frame, text="Excluir", command=self.excluir_usuario, font=("Arial", 18))
        self.btnExcluir.grid(row=5, column=2, padx=10, pady=10)

        self.lblMensagem = tk.Label(self.frame, text="", font=("Arial", 18))
        self.lblMensagem.grid(row=6, column=0, columnspan=3, padx=10, pady=10)

        # Bind para detectar o fechamento da janela
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def inserir_usuario(self):
        nome = self.txtNome.get()
        telefone = self.txtTelefone.get()
        email = self.txtEmail.get()
        usuario = self.txtUsuario.get()
        senha = self.txtSenha.get()
        # Aqui você deve chamar o método para inserir o usuário na sua lógica
        self.lblMensagem.config(text="Usuário inserido com sucesso!")

    def alterar_usuario(self):
        # Implemente a lógica para alterar o usuário
        self.lblMensagem.config(text="Usuário alterado com sucesso!")

    def excluir_usuario(self):
        # Implemente a lógica para excluir o usuário
        self.lblMensagem.config(text="Usuário excluído com sucesso!")

    def on_closing(self):
        self.root.destroy()
        os.system('python principal.py')  # Reabre o principal.py ao fechar a janela

# Execução da interface
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
