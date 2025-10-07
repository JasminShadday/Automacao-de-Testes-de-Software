from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os

# Configurar o driver (modo sem interface gráfica)
options = Options()
options.add_argument("--headless")

service = Service()
driver = webdriver.Chrome(service=service, options=options)

# Caminho absoluto para o arquivo local
caminho_arquivo = os.path.abspath("../src/exercicio.html")
driver.get(f"file:///{caminho_arquivo}")

# (a) Mostrar o título da página
print("Título da página:", driver.title)

driver.quit()
