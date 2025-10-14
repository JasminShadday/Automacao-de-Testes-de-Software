import pyautogui
import time
import webbrowser

# 1. Abrir o navegador e acessar o Facebook
webbrowser.open('https://www.facebook.com/r.php')
time.sleep(5)  # Aguarde a página carregar

# 2. Preencher o formulário
# OBS: Os valores de x, y devem ser ajustados conforme a posição dos campos na sua tela

# Nome
pyautogui.click(x=472, y=309)
pyautogui.write('SeuNome', interval=0.1)

# Sobrenome
pyautogui.click(x=650, y=317)
pyautogui.write('SeuSobrenome', interval=0.1)

# Email
pyautogui.click(x=541, y=506)
pyautogui.write('seuemail@exemplo.com', interval=0.1)

# Senha
pyautogui.click(x=475, y=557)
pyautogui.write('SuaSenhaForte', interval=0.1)

# GENERO
pyautogui.click(x=662, y=464)

# Dia Nascimento
pyautogui.click(x=554, y=388)
pyautogui.click(x=486, y=618)

# Mes Nascimento
pyautogui.click(x=690, y=383)
pyautogui.click(x=623, y=576)

# Ano Nascimento
pyautogui.click(x=821, y=388)
pyautogui.click(x=829, y=451)
pyautogui.scroll(-1500)
pyautogui.click(x=745, y=728)

# 3. Clicar no botão "Cadastre-se"
#pyautogui.click(x=622, y=721)

# Aguarde para ver o resultado
time.sleep(10)
