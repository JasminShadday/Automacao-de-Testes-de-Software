# Este arquivo contém testes unitários para a função avaliar_notas do módulo escolar.py.
# Ele verifica se a função retorna os conceitos corretos e se lida com erros de entrada.
import unittest
from Escolar import avaliar_notas

class TesteAvaliarNotas(unittest.TestCase):
    def test_avaliar_notas(self):
        self.assertEqual(avaliar_notas(10, 10, 10, 10), 'A')
        self.assertEqual(avaliar_notas(9, 9, 9, 9), 'A')
        self.assertEqual(avaliar_notas(8, 8, 8, 8), 'B')
    
    def test_avaliar_notas_erro(self):
        self.assertRaises(ValueError, avaliar_notas, 11, 10, 10, 10)
        self.assertRaises(ValueError, avaliar_notas, 10, 11, 10, 10)
        self.assertRaises(ValueError, avaliar_notas, 10, 10, 11, 10)
        self.assertRaises(ValueError, avaliar_notas, 10, 10, 10, 11)

    def test_avaliar_notas_erro_media_exercicios(self):
        self.assertRaises(ValueError, avaliar_notas, 10, 10, 10, 11)
        self.assertRaises(ValueError, avaliar_notas, 10, 10, 10, -1)
        self.assertRaises(ValueError, avaliar_notas, 10, 10, 10, 12)

        
if __name__ == '__main__':    
    unittest.main()


