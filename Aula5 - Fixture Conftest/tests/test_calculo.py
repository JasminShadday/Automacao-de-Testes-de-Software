import pytest
from src.calcular_area import Calcular_area
from src.medidas import Medida

@pytest.fixture
def calculo():
    raio=Medida(2,3)
    calculo=Calcular_area('area', raio)
    return calculo

def test_passar_valor_raio_devolver_valor_area(calculo):
    assert calculo.calcular_area() == 12.56

def test_passar_valor_raio_devolver_valor_volume(calculo):
    assert calculo.calcular_volume() == 37.68


