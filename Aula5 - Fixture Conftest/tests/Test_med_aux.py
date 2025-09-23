import pytest

from src.medidas import Medida


def test_passar_valor_area():
    raio=Medida(2,3)
    assert raio.get_raio()==2

def test_passar_valor_altura():
    raio=Medida(2,3)
    assert raio.get_alt()==3


    
