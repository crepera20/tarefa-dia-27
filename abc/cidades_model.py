from Banco import Banco

class cidade:
    def _init_(self):
        self.banco = Banco()

    def inserir(self, nome, uf):
        cursor = self.banco.conexao.cursor()
        cursor.execute('''
            INSERT INTO cidade (nome, uf)
            VALUES (?, ?)
        ''', (nome, uf))
        self.banco.conexao.commit()

    def alterar(self, idCidade, nome, uf):
        cursor = self.banco.conexao.cursor()
        cursor.execute('''
            UPDATE cidade SET nome=?, uf=?
            WHERE idcid=?
        ''', (nome, uf, idCidade))
        self.banco.conexao.commit()

    def excluir(self, idCidade):
        cursor = self.banco.conexao.cursor()
        cursor.execute('DELETE FROM cidade WHERE idcid=?', (idCidade,))
        self.banco.conexao.commit()

    def buscar(self, idCidade):
        cursor = self.banco.conexao.cursor()
        cursor.execute('SELECT * FROM cidade WHERE idcid=?', (idCidade,))
        return cursor.fetchone()