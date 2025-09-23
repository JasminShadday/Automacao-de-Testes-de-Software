import pytest
from src.medidas import Medida

@pytest.fixture
def medida():
    return  Medida(2,3)
 
