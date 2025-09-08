def calcular_imc(altura, peso, nome):
    if not isinstance(altura, (int, float)) or not isinstance(peso, (int, float)):
        return "altura e peso devem ser números."
    if altura <= 0 or peso <= 0:
        return "altura e peso devem ser maiores que zero."
    
    # Fórmula do IMC
    imc = peso / (altura ** 2)
    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif 18.5 <= imc <= 24.9:
        classificacao = "Peso normal"
    elif 25.0 <= imc <= 29.9:
        classificacao = "Sobrepeso"
    elif 30.0 <= imc <= 34.9:
        classificacao = "Obesidade grau I"
    elif 35.0 <= imc <= 39.9:
        classificacao = "Obesidade grau II"
    else:
        classificacao = "Obesidade grau III"
    
    return f"{nome}, seu IMC é {imc:.2f} e sua classificação é: {classificacao}"
