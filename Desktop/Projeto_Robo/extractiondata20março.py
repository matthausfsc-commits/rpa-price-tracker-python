from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Mantém o navegador aberto
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

# 1. Abre o site
driver.get("https://www.google.com")

try:
    # 2. Identifica o campo de texto (usando o NAME, que é outra forma de ID)
    # No Google, o campo de busca tem o name='q'
    campo_busca = driver.find_element(By.NAME, "q")
    campo_busca.send_keys("Python Selenium curso")

    print("Encontrei o campo e digitei!")

    # 3. Identifica o botão de pesquisa (usando XPath para blindar)
    # Vamos buscar um botão que tenha o valor 'Pesquisa Google'
    botao_pesquisa = driver.find_element(By.XPATH, "//input[@value='Pesquisa Google']")

    time.sleep(1)  # Só pra você ver acontecendo
    botao_pesquisa.click()
    print("Botão identificado e clicado com sucesso!")

except Exception as e:
    print(f"Mano, deu erro na identificação: {e}")
