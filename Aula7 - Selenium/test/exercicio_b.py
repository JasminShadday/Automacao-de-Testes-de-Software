from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os

options = Options()
options.add_argument("--headless")

service = Service()
driver = webdriver.Chrome(service=service, options=options)

caminho_arquivo = os.path.abspath("../src/exercicio.html")
driver.get(f"file:///{caminho_arquivo}")

# (b) Localizar parágrafo pelo nome da TAG
paragrafo = driver.find_element("tag name", "p")
print("Conteúdo do parágrafo (TAG_NAME):", paragrafo.text)

driver.quit()
