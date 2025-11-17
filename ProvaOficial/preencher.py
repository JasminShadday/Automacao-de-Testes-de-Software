from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Configuração do driver (certifique-se de ter o ChromeDriver instalado e no PATH)
driver = webdriver.Chrome()

try:
    # Abre a página HTML
    driver.get('C:\\Users\\jasmi\\OneDrive\\Documentos\\Jasmin\\Faculdade\\5 Semestre\\Automação de Testes de Software\\ProvaOficial\\index.html')  # Substitua pelo caminho correto
    
    # Aguarda a página carregar
    time.sleep(1)
    
    # Preenche o campo Nome
    nome_field = driver.find_element(By.ID, "nome")
    nome_field.send_keys("Jasmin Shadday")
    time.sleep(0.8)
    
    # Preenche o campo RA
    ra_field = driver.find_element(By.ID, "ra")
    ra_field.send_keys("2303142")
    time.sleep(0.8)
    
    # Preenche a data de nascimento
    dia_field = driver.find_element(By.ID, "dia")
    dia_field.send_keys("27")
    time.sleep(0.8)
    
    mes_field = driver.find_element(By.ID, "mes")
    mes_field.send_keys("05")
    time.sleep(0.8)
    
    ano_field = driver.find_element(By.ID, "ano")
    ano_field.send_keys("2004")
    time.sleep(0.8)
    
    # Seleciona o curso
    curso_select = Select(driver.find_element(By.ID, "curso"))
    curso_select.select_by_visible_text("Sistemas de Informação")
    time.sleep(0.8)
    
    # Seleciona o aproveitamento
    aproveitamento_select = Select(driver.find_element(By.ID, "aproveitamento"))
    aproveitamento_select.select_by_value("8")
    time.sleep(0.8)
    
    # Preenche as sugestões
    sugestoes_field = driver.find_element(By.ID, "sugestoes")
    sugestoes_field.send_keys("Sugiro que seja que seu carisma e risada continue assim, pois é muito bom para o ambiente de aprendizado. :)")
    time.sleep(0.8)
    
    # Preenche as observações (opcional)
    observacoes_field = driver.find_element(By.ID, "observacoes")
    observacoes_field.send_keys("O material disponibilizado foi muito útil, especialmente os exercícios práticos.")
    time.sleep(0.8)
    
    # Clica no botão de enviar
    enviar_btn = driver.find_element(By.ID, "enviar")
    enviar_btn.click()
    time.sleep(2)
    
    print("Formulário preenchido com sucesso!")
    
except Exception as e:
    print(f"Ocorreu um erro: {e}")
    
finally:
    # Fecha o navegador
    driver.quit()