import psycopg2 as pg
import Banco

bc = Banco.Banco()

print('Conexão com o banco postgres em orientação a objeto')


def menu():
    """Menu para a escolha da operação no banco
    """
    while True:
        try:
            print(
                '1-Criar tabela\n2-Inserir Livro\n3-Listar Livro\n4-Atualizar Livro\n5-Deletar\n6-Sair')
            op = int(input())
            if op == 1:
                bc.criar_tabela()
            elif op == 2:
                nome_livro = str(input('Qual o nome do livro? '))
                bc.inserir_livro(nome_livro)
            elif op == 3:
                bc.exibir()
            elif op == 4:
                id_livro = int(input("Qual o id que você quer atualizar? "))
                nome_livro = str(
                    input("Qual o nome do livro que você deseja inserir? "))
                bc.atualizar(id_livro, nome_livro)
            elif op == 5:
                id_livro = int(input("Qual o id que você quer deletar? "))
                bc.deletar(id_livro)
            elif op == 6:
                exit()
            else:
                print("OPÇÃO INVÁLIDA")
        except Exception as e:
            print("Digite números")


menu()
