def soma(a,b):
    return a + b

# Programa Principal
try:
    resultado = soma(10, 20)
    assert resultado == 30
    print ('Soma Correta')

except AssertionError:
    print('Soma Errada!')