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
        database = "locadora"
    )

    cursor = banco.cursor()
    return banco, cursor

# Função para cadastrar os dados do funcionario

def cadastrar(nome, cargo, salario, data_contratacao):
    banco, cursor = conectar_banco()
    # Variavel para INSERIR os dados na tabela
    sql = "INSERT INTO funcionarios(nome, cargo, salario, data_contratacao)VALUES(%s,%s,%s,%s)"
    # Passando os valores para os parametros %s 
    val = (nome, cargo, salario, data_contratacao)
    # Vamos executar a consulta
    cursor.execute(sql,val)
    # confirmar a execução da consulta
    banco.commit()
    # fechar o cursor
    cursor.close()
    # fechar o banco
    banco.close()

# Função para selecionar os dados
def listar_clientes():
    banco, cursor = conectar_banco()
    # Variável para guardar o retorno do select
    sql = "SELECT * FROM funcionarios"
    cursor.execute(sql)
    resultado = cursor.fetchall()
    for i in resultado: 
        print(f"{i[0]}-{i[1]}-{i[2]}-{i[3]}-{i[4]}")

    # Fechar o cursor
    cursor.close()
    # Fechar o Banco
    banco.close()

# Função para realizar a atualização dos dados 
def atualizar_funcionarios(nome, cargo, salario, data_contratacao):
    banco, cursor = conectar_banco()
    sql = "UPDATE funcionarios SET nome=%s, cargo=%s, salario=%s, data_contratacao=%s, WHERE id_funcionario=%s" 
    val = (nome, cargo, salario, data_contratacao, id)
    cursor.execute(sql,val)
    banco.commit()
    cursor.close()
    banco.close()
    print("Os dados do funcionario foram atualizados!")

# Apagar o funcionario
def apagar_funcionario(id):
    banco, cursor = conectar_banco()
    sql = "DELETE FROM funcionarios WHERE id_funcionario=%s" 
    val = [id]
    cursor.execute(sql, val)
    banco.commit()
    cursor.close()
    banco.close()
    print("Os dados do funcionario foram apagados!")