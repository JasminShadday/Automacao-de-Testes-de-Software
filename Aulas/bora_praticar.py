# calcula o volume de uma caixa retangular
def calcula_volume(comprimento, largura, altura):
    return comprimento * largura * altura

# ct01
try:
    resultado = calcula_volume(10, 20, 30)
    assert resultado == 6000
    print ('Soma Correta')

except AssertionError:
    print('Soma Errada!')

# ct02
try:
    resultado = calcula_volume(1, 2, 3)
    assert resultado == 9
    print ('Soma Correta')

except AssertionError:
    print('Soma Errada!')

# ct03
try:
    resultado = calcula_volume(67, 67, 67)
    assert resultado == 300763
    print ('Soma Correta')

except AssertionError:
    print('Soma Errada!')