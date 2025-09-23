import pytest
from dosagem import calcular_dosagem

# Testes de adultos/adolescentes
def test_dosagem_adulto_peso_maior_ou_igual_60():
    assert calcular_dosagem(20, 70) == 1000

def test_dosagem_adulto_peso_menor_60():
    assert calcular_dosagem(15, 55) == 875

# Testes de crianças
def test_dosagem_crianca_5_a_9kg():
    assert calcular_dosagem(5, 7) == 125

def test_dosagem_crianca_9_1_a_16kg():
    assert calcular_dosagem(4, 12) == 250

def test_dosagem_crianca_16_1_a_24kg():
    assert calcular_dosagem(6, 20) == 375

def test_dosagem_crianca_24_1_a_30kg():
    assert calcular_dosagem(8, 28) == 500

def test_dosagem_crianca_maior_30kg():
    assert calcular_dosagem(10, 35) == 750

# Testes de entradas inválidas
def test_idade_invalida_menor():
    with pytest.raises(ValueError, match="Idade inválida"):
        calcular_dosagem(0, 10)

def test_idade_invalida_maior():
    with pytest.raises(ValueError, match="Idade inválida"):
        calcular_dosagem(131, 60)

def test_peso_invalido_menor():
    with pytest.raises(ValueError, match="Peso Inválido"):
        calcular_dosagem(5, 4)

def test_peso_invalido_maior():
    with pytest.raises(ValueError, match="Peso Inválido"):
        calcular_dosagem(30, 201)
