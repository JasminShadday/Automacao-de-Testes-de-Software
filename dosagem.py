'''
função: calcular_dosagem
entrada: idade e peso
saída: dosagem de um determinado medicamento
Valores válidos:
- idade (entre 1 ano a 130 anos)
- peso (entre 5 kg a 200 kg)
'''
def calcular_dosagem(idade, peso):
    if idade < 1 or idade > 130:
        raise ValueError('Idade inválida')
  
    if peso < 5 or peso > 200:
        raise ValueError('Peso Inválido')

    if idade >= 12:
        if peso >= 60:
            return 1000
        else:
            return 875
    else:
        if peso >= 5 and peso <= 9:
            return 125
        elif peso >= 9.1 and peso <= 16:
            return 250
        elif peso >= 16.1 and peso <= 24:
            return 375
        elif peso >= 24.1 and peso <= 30:
            return 500
        elif peso >= 30:
            return 750