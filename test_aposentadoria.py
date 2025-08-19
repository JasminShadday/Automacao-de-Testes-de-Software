import unittest
from Aposentadoria import verificar_qualificacao_empregado

class TesteVerificarQualificacaoEmpregado(unittest.TestCase):
    def test_verificar_qualificacao_empregado(self):
        self.assertEqual(verificar_qualificacao_empregado(65, 30), 'Requerer aposentadoria')
        self.assertEqual(verificar_qualificacao_empregado(60, 25), 'Requerer aposentadoria')
        self.assertEqual(verificar_qualificacao_empregado(65, 25), 'Requerer aposentadoria')

    def test_verificar_qualificacao_empregado_nao_requerer(self):
        self.assertEqual(verificar_qualificacao_empregado(59, 20), 'Não requerer')
        self.assertEqual(verificar_qualificacao_empregado(50, 10), 'Não requerer')
        self.assertEqual(verificar_qualificacao_empregado(55, 15), 'Não requerer')

    def test_verificar_qualificacao_empregado_erro(self):
        self.assertRaises(TypeError, verificar_qualificacao_empregado, 10, '5')
        self.assertRaises(TypeError, verificar_qualificacao_empregado, '10', 5)
        self.assertRaises(TypeError, verificar_qualificacao_empregado, True, False)

if __name__ == '__main__':
    unittest.main()
