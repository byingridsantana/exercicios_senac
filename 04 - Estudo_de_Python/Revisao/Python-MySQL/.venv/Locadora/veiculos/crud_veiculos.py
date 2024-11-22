import mysql.connector as mc

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

# Função para cadastrar o veiculo
def cadastrar(marca, modelo, ano, placa, cor, tipo_combustivel, quilomentragem, status):
    banco, cursor = conectar_banco()
    # Variavel para Inserir os dados na tabela
    sql = "INSERT INTO aluno (marca, modelo, ano, placa, cor, tipo_combustivel, quilomentragem, status)VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
    # Passando os valores para os parametros %s
    val = (marca, modelo, ano, placa, cor, tipo_combustivel, quilomentragem, status)
    # Vamos executar a consulta
    cursor.execute(sql,val)
    # Confirmar a execução da consulta
    banco.commit()
    # Fechar o cursor
    cursor.close()
    # Fechar o banco
    banco.close()

# Função para selecionar os dados
def listar_veiculo():
    banco, cursor = conectar_banco()
    # Variável para guardar o retorno do SELECT
    sql = "SELECT * FROM veiculos"
    cursor.execute(sql)
    resultado = cursor.fetchall()
    for i in resultado:
        print(f"{i[0]}-{i[1]}-{i[2]}-{i[3]}-{i[4]}-{i[5]}-{i[6]}-{i[7]}-{i[8]}")
    # Fechar o cursor
    cursor.close()
    # Fechar o Banco
    banco.close()

# Função para realizar a atualização dos dados
def atualizar_veiculo(marca, modelo, ano, placa, cor, tipo_combustivel, quilomentragem, status):
    banco, cursor = conectar_banco()
    sql = "UPDATE aluno SET marca=%s, modelo=%s, ano=%s, placa=%s, cor=%s, tipo_combustivel=%s, quilomentragem=%s, status=%s WHERE id_veiculos=%s" 
    val = (marca, modelo, ano, placa, cor, tipo_combustivel, quilomentragem, status, id)
    cursor.execute(sql,val)
    banco.commit()
    cursor.close()
    banco.close()
    print("Os dados do veiculo foram atualizados!")

# Apagar o veiculo
def apagar_aluno(id):
    banco, cursor = conectar_banco()
    sql = "DELETE FROM Veiculos WHERE id_veiculos=%s" 
    val = [id]
    cursor.execute(sql, val)
    banco.commit()
    cursor.close()
    banco.close()
    print("Os dados do veiculo foram apagados!")