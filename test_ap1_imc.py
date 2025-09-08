import unittest
from ap1_imc import calcular_imc 

class TestCalcularIMC(unittest.TestCase):

    def test_tipo_invalido_altura(self):
        resultado = calcular_imc("1.75", 70, "Jasmin")
        self.assertEqual(resultado, "altura e peso devem ser números.")

    def test_tipo_invalido_peso(self):
        resultado = calcular_imc(1.75, "70", "Jasmin")
        self.assertEqual(resultado, "altura e peso devem ser números.")

    def test_imc_peso_normal(self):
        resultado = calcular_imc(1.75, 70, "Jasmin")
        esperado = "Jasmin, seu IMC é 22.86 e sua classificação é: Peso normal"
        self.assertEqual(resultado, esperado)

    def test_imc_obesidade_2(self):
        resultado = calcular_imc(1.60, 95, "Carlos")
        esperado = "Carlos, seu IMC é 37.11 e sua classificação é: Obesidade grau II"
        self.assertEqual(resultado, esperado)


if __name__ == "__main__":
    unittest.main()
