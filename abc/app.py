import tkinter as tk
from tkinter import messagebox
import os
import sys
from usuarios_model import Usuario

class Application:
    def __init__(self, root):
        self.usuario = Usuario()

        self.root = root
        self.root.title("Cadastro de Usuários")
        self.root.state("zoomed")  # Aumenta o tamanho da janela

        # Frame para centralizar os widgets
        self.frame = tk.Frame(root)
        self.frame.pack(expand=True)  # Expande para ocupar o espaço disponível

        # Widgets
        self.lblIdUsuario = tk.Label(self.frame, text="idUsuario:", font=("Arial", 18))  # Aumenta a fonte
        self.lblIdUsuario.grid(row=0, column=0, padx=10, pady=10, sticky="e")  # Adiciona espaçamento e alinha à direita
        self.txtIdUsuario = tk.Entry(self.frame, font=("Arial", 18))  # Aumenta a fonte
        self.txtIdUsuario.grid(row=0, column=1, padx=10, pady=10)

        self.btnBuscar = tk.Button(self.frame, text="Buscar", command=self.buscar_usuario, font=("Arial", 18))  # Aumenta a fonte
        self.btnBuscar.grid(row=0, column=2, padx=10, pady=10)

        self.lblNome = tk.Label(self.frame, text="Nome:", font=("Arial", 18))  # Aumenta a fonte
        self.lblNome.grid(row=1, column=0, padx=10, pady=10, sticky="e")  # Alinha à direita
        self.txtNome = tk.Entry(self.frame, font=("Arial", 18))  # Aumenta a fonte
        self.txtNome.grid(row=1, column=1, padx=10, pady=10)

        self.lblTelefone = tk.Label(self.frame, text="Telefone:", font=("Arial", 18))  # Aumenta a fonte
        self.lblTelefone.grid(row=2, column=0, padx=10, pady=10, sticky="e")  # Alinha à direita
        self.txtTelefone = tk.Entry(self.frame, font=("Arial", 18))  # Aumenta a fonte
        self.txtTelefone.grid(row=2, column=1, padx=10, pady=10)

        self.lblEmail = tk.Label(self.frame, text="E-mail:", font=("Arial", 18))  # Aumenta a fonte
        self.lblEmail.grid(row=3, column=0, padx=10, pady=10, sticky="e")  # Alinha à direita
        self.txtEmail = tk.Entry(self.frame, font=("Arial", 18))  # Aumenta a fonte
        self.txtEmail.grid(row=3, column=1, padx=10, pady=10)

        self.lblUsuario = tk.Label(self.frame, text="Usuário:", font=("Arial", 18))  # Aumenta a fonte
        self.lblUsuario.grid(row=4, column=0, padx=10, pady=10, sticky="e")  # Alinha à direita
        self.txtUsuario = tk.Entry(self.frame, font=("Arial", 18))  # Aumenta a fonte
        self.txtUsuario.grid(row=4, column=1, padx=10, pady=10)

        self.lblSenha = tk.Label(self.frame, text="Senha:", font=("Arial", 18))  # Aumenta a fonte
        self.lblSenha.grid(row=5, column=0, padx=10, pady=10, sticky="e")  # Alinha à direita
        self.txtSenha = tk.Entry(self.frame, font=("Arial", 18), show="*")  # Aumenta a fonte
        self.txtSenha.grid(row=5, column=1, padx=10, pady=10)

        # Botões
        self.btnInserir = tk.Button(self.frame, text="Inserir", command=self.inserir_usuario, font=("Arial", 18))  # Aumenta a fonte
        self.btnInserir.grid(row=6, column=0, padx=10, pady=10)

        self.btnAlterar = tk.Button(self.frame, text="Alterar", command=self.alterar_usuario, font=("Arial", 18))  # Aumenta a fonte
        self.btnAlterar.grid(row=6, column=1, padx=10, pady=10)

        self.btnExcluir = tk.Button(self.frame, text="Excluir", command=self.excluir_usuario, font=("Arial", 18))  # Aumenta a fonte
        self.btnExcluir.grid(row=6, column=2, padx=10, pady=10)

        self.lblMensagem = tk.Label(self.frame, text="", font=("Arial", 18))  # Aumenta a fonte
        self.lblMensagem.grid(row=7, column=0, columnspan=3, padx=10, pady=10)

        # Bind para detectar o fechamento da janela
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def buscar_usuario(self):
        idUsuario = self.txtIdUsuario.get()
        resultado = self.usuario.buscar(idUsuario)
        if resultado:
            self.txtNome.delete(0, tk.END)
            self.txtNome.insert(tk.END, resultado[1])
            self.txtTelefone.delete(0, tk.END)
            self.txtTelefone.insert(tk.END, resultado[2])
            self.txtEmail.delete(0, tk.END)
            self.txtEmail.insert(tk.END, resultado[3])
            self.txtUsuario.delete(0, tk.END)
            self.txtUsuario.insert(tk.END, resultado[4])
            self.txtSenha.delete(0, tk.END)
            self.txtSenha.insert(tk.END, resultado[5])
            self.lblMensagem.config(text="Busca realizada com sucesso!")
        else:
            self.lblMensagem.config(text="Usuário não encontrado!")

    def inserir_usuario(self):
        nome = self.txtNome.get()
        telefone = self.txtTelefone.get()
        email = self.txtEmail.get()
        usuario = self.txtUsuario.get()
        senha = self.txtSenha.get()
        self.usuario.inserir(nome, telefone, email, usuario, senha)
        self.lblMensagem.config(text="Usuário inserido com sucesso!")

    def alterar_usuario(self):
        idUsuario = self.txtIdUsuario.get()
        nome = self.txtNome.get()
        telefone = self.txtTelefone.get()
        email = self.txtEmail.get()
        usuario = self.txtUsuario.get()
        senha = self.txtSenha.get()
        self.usuario.alterar(idUsuario, nome, telefone, email, usuario, senha)
        self.lblMensagem.config(text="Usuário alterado com sucesso!")

    def excluir_usuario(self):
        idUsuario = self.txtIdUsuario.get()
        self.usuario.excluir(idUsuario)
        self.lblMensagem.config(text="Usuário excluído com sucesso!")

    def on_closing(self):
        self.root.destroy()
        os.system('python principal.py')  # Reabre o principal.py ao fechar a janela

# Execução da interface
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()