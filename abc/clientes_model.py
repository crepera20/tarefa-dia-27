from Banco import Banco

class Cliente:
    def _init_(self):
        self.banco = Banco()

    def inserir(self, nome, telefone, email):
        cursor = self.banco.conexao.cursor()
        cursor.execute('''
            INSERT INTO cliente (nome, telefone, email)
            VALUES (?, ?, ?, ?, ?)
        ''', (nome, telefone, email))
        self.banco.conexao.commit()

    def alterar(self, idcli, nome, telefone, email):
        cursor = self.banco.conexao.cursor()
        cursor.execute('''
            UPDATE cliente SET nome=?, telefone=?, email=?
            WHERE idcli=?
        ''', (nome, telefone, email, usuario))
        self.banco.conexao.commit()

    def excluir(self, idUsuario):
        cursor = self.banco.conexao.cursor()
        cursor.execute('DELETE FROM cliente WHERE idcli=?', (idcli,))
        self.banco.conexao.commit()

    def buscar(self, idUsuario):
        cursor = self.banco.conexao.cursor()
        cursor.execute('SELECT * FROM cliente WHERE idcli=?', (idcli,))
        return cursor.fetchone()