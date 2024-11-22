# Importar o drive de comunicação do Python com MySQL
import mysql.connector as mc 

# Vamos criar uma função para estabelecer a conexão com o banco de dados 
# todas as vezes que for executar uma consulta em uma das tabelas, 
# esta função pode ser utilizada. 

def conectar_banco():
    banco = mc.connect(
        host = "127.0.0.1",
        port = 3307,
        user = "root",
        password = "",
        database = "biblioteca"
    )

    cursor = banco.cursor()
    return banco, cursor

# Função para cadastrar os dados do bibliotecario

def cadastrar(data_devolucao_prevista, data_devolucao_real, id_publicacao, id_aluno, id_bibliotecario):
    banco, cursor = conectar_banco()
    # Variavel para INSERIR os dados na tabela
    sql = "INSERT INTO emprestimo(data_devolucao_prevista, data_devolucao_real, id_publicacao, id_aluno, id_bibliotecario)VALUES(%s,%s,%s,%s,%s)"
    # Passando os valores para os parametros %s 
    val = (data_devolucao_prevista, data_devolucao_real, id_publicacao, id_aluno, id_bibliotecario)
    # Vamos executar a consulta
    cursor.execute(sql,val)
    # confirmar a execução da consulta
    banco.commit()
    # fechar o cursor
    cursor.close()
    # fechar o banco
    banco.close()

# Função para selecionar os dados
def listar_emprestimo():
    banco, cursor = conectar_banco()
    # Variável para guardar o retorno do select
    sql = "SELECT * FROM emprestimo"
    cursor.execute(sql)
    resultado = cursor.fetchall()
    for i in resultado: 
        print(f"{i[0]}-{i[1]}-{i[2]}-{i[3]}-{i[4]}-{i[5]}{i[6]}")

    # Fechar o cursor
    cursor.close()
    # Fechar o Banco
    banco.close()

# Função para realizar a atualização dos dados 
def atualizar_emprestimo(data_devolucao_real, id):
    banco, cursor = conectar_banco()
    sql = "UPDATE emprestimo SET data_devolucao_real=%s WHERE id_emprestimo=%s"  
    val = (data_devolucao_real, id)
    cursor.execute(sql, val)
    banco.commit()
    cursor.close()
    banco.close()
    print("Os dados do emprestimo foram atualizados!")

# Apagar o bibliotecario 
def apagar_emprestimo(id):
    banco, cursor = conectar_banco()
    sql = "DELETE FROM emprestimo WHERE id_emprestimo=%s" 
    val = [id]
    cursor.execute(sql, val)
    banco.commit()
    cursor.close()
    banco.close()
    print("Os dados do emprestimo foram apagados!")