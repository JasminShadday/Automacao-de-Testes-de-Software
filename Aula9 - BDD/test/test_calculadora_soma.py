"""Calculadora feature tests."""
from pytest import fixture

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
    )
from app.calculadora import soma

@fixture
def contexto():
    return {'num1': 0, 'num2': 0, 'resultado': 0}

#@scenario('features\calculadora.feature', 'Soma dois numeros')
def test_soma_dois_números():
    """Soma dois números."""

@given('eu também tenho o número 7 como entrada para a calculadora')
def eu_também_tenho_o_número_7_como_entrada_para_a_calculadora(contexto):
    """eu também tenho o número 7 como entrada para a calculadora."""
    contexto['num2'] = 7

@given('eu tenho o número 2 como entrada para a calculadora')
def eu_tenho_o_número_2_como_entrada_para_a_calculadora(contexto):
    """eu tenho o número 2 como entrada para a calculadora."""
    contexto['num1'] = 2

@when('eu solicito que realize a soma')
def eu_solicito_que_realize_a_soma(contexto):
    """eu solicito que realize a soma."""
    contexto['resultado'] = soma(contexto['num1'], contexto['num2'])

@then('o resultado deve ser 9')
def o_resultado_deve_ser_9(contexto):
    """o resultado deve ser 9."""
    assert contexto['resultado'] == 9