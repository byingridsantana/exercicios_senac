import re
import mysql.connector as mysql

# Para estabelecer a conexão com o banco de dados mysql 
# será necessário passar algumas configurações, tais como:
# endereço do servidor banco de dados(host), porta de comunicação(3380)
# usuário do banco(root), senha de acesso(123@senac) e o nome do banco de dados (dbusuarios)

con = mysql.connect(
    port = 3380,
    user ="root",
    host ="127.0.0.1",
    password ="123@senac",
    database ="dbusuarios"
)

# Vamos criar três funções, sendo:
# 1º cadastrar_usuarios
# 2º atualizar_usuarios
# 3º autenticar_usuarios

def cadastrar_usuarios(nome,email,senha):

    # Criar uma variavel chamada msg para nos ajudar 
    # a retornar uma mensagem. Caso tenha cadastrado ou tenha dado algum erro.

    msg = ""

    # Vamos validar a quantidade de caracteres e, para isso 
    # iremos usar o comando len. Este comando tem a capacidade
    # de contar quantos caracteres há em uma variavel

    if(len(senha) < 8):
        return "Sua senha deve ter no mínimo 8 caracteres"

    
    # Vamos fazer uma validação no nome de usuario para não aceitar 
    # caracteres especiais. Utilizaremos a expressão regular para isso

    padrao = r"^[a-z]+$"
    # A expressao regular acima valida a entrada de caracteres não especiais e não númericos de a até z mínusculos.
    # O elemento ^ indica início da string e caractere $ indica o fim da string
    # entre colchetes estamos indicando quais caracteres serão aceitos
    # neste caso estamos definindo a-z ou seja, serão aceitos caracteres de a até z e o sinal de + indica 
    # as letras podem repetir em algum momento

    # Usando o comando match() analisa o padrão da expressão regular
    # e a variável nome para saber os caracteres combinam em sua configuração,
    # ou seja, se eles são minusculos, não são especiais e não númericos.
    # o comando match pode retornar que os dois elementos combinam ou retornar nenhum (none),
    # Para descartar a possibilidade do None, utilizamos a expressão "is not none"
    nome_valido = re.match(padrao,nome) is not None 
    if(nome_valido==False):
        return "Nome de usuário inválido. Use apenas letras minúsculas"
    
    # validação dos campos, nome, email e senha
    # verificar se há caracteres nas variaveis
    # caso esteja vazio, não realizar o cadastro

    # comando strip retira o excesso de espaço na variável 
    if(nome.strip()=="" or email.strip()=="" or senha.strip()==""):
        msg = "Você deve preencher todos os campos"
    else:

        # Definir um cursor que irá fazer a movimentação na
        # Tabela de usuário e, assim poderá ler, cadastrar,
        # Atualizar e deletar dados.
        cursor = con.cursor()

        # Verificar se o e-mail do usuário já existe no banco de dados
        sqlConsulta = f"SELECT email FROM tbl_usuarios WHERE email ='{email}' OR nome='{nome}'"
        cursor.execute(sqlConsulta)
        # Para saber se o email existe ou não na tabela, estamos usando o comando fetchall->fetch(buscar) all(todos)
        # busca todos os dados que estão no select da consulta e caso tenha dado ele irá retorna o dado existente 
        # nesse caso, o email já está cadastrado.
        # caso não tenha email cadastrado, a linha retorna vazia.
        # o comando onde comparamos com if linha[0], significa que o select tem apenas um item de retorno que o email.
        # Assim, sua posição na consulta: #SELECT email FROM tbl_usuarios é 0, por ser o primeiro e o único campo de retorno da consulta

        # Pegamos, então, a linha na posição zero(0) e comparamos com ""(vazio)
        # e se linha[0] for diferente(!=) de aspas aspas(""), significa que foi encontrado algo no banco e,
        # portanto, temos um e-mail já cadastrado.

        # Isso fará com que a mensagem "E-mail já cadastrado" seja retornada e o usuário não será cadastrado.
        # caso contrário, ou seja se ao fazer a comparação linha[0] não retornar nada, iremos realizar o cadastro 
        # do novo usuário com seus dados, inclusive email.  

        linha = cursor.fetchall()
        if(linha!=[]):
            msg = "E-mail ou Usuário já cadastrado. Não é possivel cadastrar"
        else:
            # Criar variavel que guarda a consulta de cadastro de usuarios
            sql = f"INSERT INTO tbl_usuarios(nome,email,senha) VALUES ('{nome}','{email}','{senha}')"
            # Vamos executar a consulta utilizando o comando execute com o parâmetro 
            # sql(variavel criada acima para o comando INSERT)
            cursor.execute(sql)
            # Confirmar a execução da consulta com o comando commit para conexão(con)
            con.commit()
            msg = "Cadastro efetuado com sucesso"
            # Fechar a movimentação do cursor com o comando close
            cursor.close()
            # Fechar a conexão com o banco de dados com o comando close
            con.close()
    return msg

def atualizar_usuarios(id,nome,email,senha):

    # Criar uma variavel chamada msg para nos ajudar 
    # a retornar uma mensagem. Caso tenha cadastrado ou tenha dado algum erro.

    msg = ""

    # Vamos validar a quantidade de caracteres e, para isso 
    # iremos usar o comando len. Este comando tem a capacidade
    # de contar quantos caracteres há em uma variavel

    if(len(senha) < 8):
        return "Sua senha deve ter no mínimo 8 caracteres"
    
    # Vamos fazer uma validação no nome de usuario para não aceitar 
    # caracteres especiais. Utilizaremos a expressão regular para isso

    padrao = r"^[a-z]+$"
    # A expressao regular acima valida a entrada de caracteres não especiais e não númericos de a até z mínusculos.
    # O elemento ^ indica início da string e caractere $ indica o fim da string
    # entre colchetes estamos indicando quais caracteres serão aceitos
    # neste caso estamos definindo a-z ou seja, serão aceitos caracteres de a até z e o sinal de + indica 
    # as letras podem repetir em algum momento

    # Usando o comando match() analisa o padrão da expressão regular
    # e a variável nome para saber os caracteres combinam em sua configuração,
    # ou seja, se eles são minusculos, não são especiais e não númericos.
    # o comando match pode retornar que os dois elementos combinam ou retornar nenhum (none),
    # Para descartar a possibilidade do None, utilizamos a expressão "is not none"
    nome_valido = re.match(padrao,nome) is not None 
    if(nome_valido==False):
        return "Nome de usuário inválido. Use apenas letras minúsculas"
    
    # validação dos campos, nome, email e senha
    # verificar se há caracteres nas variaveis
    # caso esteja vazio, não realizar o cadastro

    # comando strip retira o excesso de espaço na variável 
    
    if(nome.strip()=="" or email.strip()=="" or senha.strip()==""):
        msg = "Você deve preencher todos os campos"
    else:

        # Definir um cursor que irá fazer a movimentação na
        # Tabela de usuário e, assim poderá ler, cadastrar,
        # Atualizar e deletar dados.
        cursor = con.cursor()

        # Verificar se o e-mail do usuário já existe no banco de dados
        sqlConsulta = f"SELECT email FROM tbl_usuarios WHERE email ='{email}' OR nome='{nome}'"
        cursor.execute(sqlConsulta)
    
    linha = cursor.fetchall()
    if(linha!=[]):
        msg = "E-mail ou Usuário já cadastrado. Não é possivel cadastrar"
    else:        
        # Criar um cursor que fazer a movimentação dentro da tabela
        # tbl_usuarios e, assim poderá realizar as consultas do tipo 
        # select, insert, update, e delete dos dados dos usuários
        cursor = con.cursor()
        # criar uma variável que irá guardar a consulta de atualizacao
        # dos dados dos usuários
        sql=f"UPDATE tbl_usuarios SET nome='{nome}', email='{email}', senha='{senha}' WHERE id={id}"
        # executar a consulta com o comando execute
        cursor.execute(sql)
        # Confirmar a execução da consulta com o comando commit 
        con.commit()

        # fechar a movimentação do cursor com o comando close
        cursor.close()

        # fechar a conexao com o banco de dados
        con.close()
    return "Atualizou"

def autenticar_usuarios(nome,email,senha):
    # Criar um cursor para realizar a movimentação dentro da tabela
    # tbl_usuarios e, assim poderá selecionar, inserir, atualizar, e
    # apagar os dados dos usuarios
    cursor = con.cursor()
    # Criar uma consulta que irá realizar a pesquisa no banco de dados
    # em busca do usuário e sua senha correspondente
    # vamos usar o nome de usuario ou o email e a senha para realizar
    # o processo de autenticação
    sql=f"SELECT nome,email FROM tbl_usuarios WHERE nome='{nome}' OR email='{email}' AND senha='{senha}'"
    # executar a consulta com o comando execute
    cursor.execute(sql)

    # confirmar a execução da consulta
    con.commit()

    # o resultado obtido com o comando select deverá ser guardado em uma variavel
    # o comando fetchall é utilizado para armazenar o resultado da consulta select
    # o termo fetch significa buscar e all todos. Busca e armazena todos os dados
    # do comando select. O resultado será apenas um nome e email de usuário 
    rs = cursor.fetchall()
    # fechar o cursor
    cursor.close()
    # fecha a conexao com o banco de dados
    con.close()

    if(rs[0]==""):
        return "Usuário ou senha incorreto"
    else: 
        return True 
    