#'''
# função: obter_peso_ideal()
# entrada: altura, sexo
# saída: O valor do peso ideal
#Valores válidos:
#- altura (entre 1,0 m e 2,5 m)
#- sexo (string 'M' ou 'F'

def obter_peso_ideal(altura, sexo):
    if sexo == 'M':
        return (72.7 * altura) - 58
    else:
        return (62.1 * altura) - 44.7
    
