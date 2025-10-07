from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os

options = Options()
options.add_argument("--headless")

service = Service()
driver = webdriver.Chrome(service=service, options=options)

# Caminho correto (ajustado ao seu projeto)
caminho_arquivo = os.path.abspath("../src/exercicio.html")
driver.get(f"file:///{caminho_arquivo}")

# Localiza o parágrafo pela classe CSS
paragrafo = driver.find_element("css selector", "p.content")
print("Conteúdo do parágrafo (CSS_SELECTOR):", paragrafo.text)

driver.quit()
