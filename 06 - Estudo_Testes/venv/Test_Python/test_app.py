import pytest
import usuario as us 

# def test_cad():
#    rs = us.cadastrar_usuarios("marcia", "marcia.oliveira@gmail.com","12345678")
#    assert rs=="Cadastro efetuado com sucesso"

def test_at():
    rs = us.atualizar_usuarios()
    assert rs =="Atualizou"