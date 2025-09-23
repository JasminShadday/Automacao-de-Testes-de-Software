import pytest
from calculadora_peso import obter_peso_ideal

# -------------------------------
# Testes com entradas válidas
# -------------------------------

def test_peso_ideal_masculino():
    # altura 1.80 m -> (72.7 * 1.80) - 58 = 72.46
    assert obter_peso_ideal(1.80, 'M') == pytest.approx(72.46, 0.01)

def test_peso_ideal_feminino():
    # altura 1.65 m -> (62.1 * 1.65) - 44.7 = 57.77
    assert obter_peso_ideal(1.65, 'F') == pytest.approx(57.77, 0.01)

def test_peso_ideal_limite_inferior():
    # altura mínima 1.0 m
    assert obter_peso_ideal(1.0, 'M') == pytest.approx(14.7, 0.01)
    assert obter_peso_ideal(1.0, 'F') == pytest.approx(17.4, 0.01)

def test_peso_ideal_limite_superior():
    # altura máxima 2.5 m
    assert obter_peso_ideal(2.5, 'M') == pytest.approx(123.75, 0.01)
    assert obter_peso_ideal(2.5, 'F') == pytest.approx(110.55, 0.01)
    
#rodar com: pytest -v test_calculadora_peso.py