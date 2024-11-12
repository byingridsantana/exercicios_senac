import pytest 
import usuario as us 

rs = us.cadastrar_usuarios("marcia","marcia@terra.com.br","12345678")

# Vamos utilizar o comando assert para verificar se o retorno 
# do cadastro de usuario é a mensagem "Cadastrou"

assert rs=="Cadastro efetuado com sucesso"



#us.atualizar_usuarios (2,"Paula Oliveira","paula@uol.com.br","456")

# us.autenticar_usuarios 