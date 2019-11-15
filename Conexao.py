import psycopg2 as pdb


class Conexao:

    def criar_conexao(self):

        try:
            con = pdb.connect(
                database="teste_python",
                user="postgres",
                password="1a2s3d",
                host="127.0.0.1",
                port="5432"
            )

        except Exception as erro:
            print(erro)
            exit(1)
        return con
