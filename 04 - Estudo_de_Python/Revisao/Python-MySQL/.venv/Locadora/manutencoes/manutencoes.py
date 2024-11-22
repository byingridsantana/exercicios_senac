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

# Função para cadastrar os dados da manutenção

def cadastrar(data_ultima_revisao, proxima_revisao, descricao, valor):
    banco, cursor = conectar_banco()
    # Variavel para INSERIR os dados na tabela
    sql = "INSERT INTO manutencoes (data_ultima_revisao, proxima_revisao, descricao, valor)VALUES(%s,%s,%s,%s)"
    # Passando os valores para os parametros %s 
    val = (data_ultima_revisao, proxima_revisao, descricao, valor)
    # Vamos executar a consulta
    cursor.execute(sql,val)
    # confirmar a execução da consulta
    banco.commit()
    # fechar o cursor
    cursor.close()
    # fechar o banco
    banco.close()

# Função para selecionar os dados
def listar_manutencoes():
    banco, cursor = conectar_banco()
    # Variável para guardar o retorno do select
    sql = "SELECT * FROM manutencoes"
    cursor.execute(sql)
    resultado = cursor.fetchall()
    for i in resultado: 
        print(f"{i[0]}-{i[1]}-{i[2]}-{i[3]}-{i[4]}")

    # Fechar o cursor
    cursor.close()
    # Fechar o Banco
    banco.close()

# Função para realizar a atualização dos dados 
def atualizar_locacoes(data_ultima_revisao, proxima_revisao, descricao, valor):
    banco, cursor = conectar_banco()
    sql = "UPDATE manutencoes SET data_inicio=%s, data_ultima_revisao=%s, proxima_revisao=%s, descricao=%s,valor=%s WHERE id_manutencao=%s" 
    val = (data_ultima_revisao, proxima_revisao, descricao, valor, id)
    cursor.execute(sql,val)
    banco.commit()
    cursor.close()
    banco.close()
    print("Os dados da manutenção foram atualizados!")

# Apagar a manutenção
def apagar_locacoes(id):
    banco, cursor = conectar_banco()
    sql = "DELETE FROM manutencoes WHERE id_manutencao=%s" 
    val = [id]
    cursor.execute(sql, val)
    banco.commit()
    cursor.close()
    banco.close()
    print("Os dados da manutenção foram apagados!")