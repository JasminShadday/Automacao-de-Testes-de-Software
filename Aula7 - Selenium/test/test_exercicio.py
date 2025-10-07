import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os

class TestExercicio01(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = Options()
        options.add_argument("--headless")
        cls.driver = webdriver.Chrome(service=Service(), options=options)
        caminho_arquivo = os.path.abspath("../src/exercicio.html")
        cls.driver.get(f"file:///{caminho_arquivo}")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_titulo_pagina(self):
        """Verifica se o título da página está correto"""
        self.assertEqual(self.driver.title, "Exercicio 01")

    def test_conteudo_paragrafo_tag_name(self):
        """Verifica o conteúdo do parágrafo via TAG_NAME"""
        p = self.driver.find_element("tag name", "p")
        self.assertEqual(p.text, "O conteudo do site vem aqui")

    def test_conteudo_paragrafo_css_selector(self):
        """Verifica o conteúdo do parágrafo via CSS_SELECTOR"""
        p = self.driver.find_element("css selector", "p.content")
        self.assertEqual(p.text, "O conteudo do site vem aqui")


if __name__ == "__main__":
    unittest.main()
