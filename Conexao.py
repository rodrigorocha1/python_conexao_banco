import psycopg2 as pdb


class Conexao:

    def criar_conexao(self):

        try:
            con = pdb.connect(
                database="teste_python",
                user="postgres",
                password="",
                host="",
                port="5432"
            )

        except Exception as erro:
            print(erro)
            exit(1)
        return con
