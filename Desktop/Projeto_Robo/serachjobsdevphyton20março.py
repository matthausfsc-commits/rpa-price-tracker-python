from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # Para apertar Enter
import time

# 1. CONFIGURAÇÃO (O que mantém aberto e disfarça o robô)
options = Options()
options.add_experimental_option("detach", True)
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(options=options)

# 2. IR ATÉ O SITE
driver.get("https://www.google.com")

try:
    # 3. ESPERAR O SITE CARREGAR (Blindagem de tempo)
    time.sleep(2)

    # 4. ENCONTRAR A "ALMA" DO CAMPO (O nome dele no Google é 'q')
    campo_busca = driver.find_element(By.NAME, "q")

    # 5. INTERAGIR
    campo_busca.send_keys("Vagas Junior RPA Python Fortaleza")
    print("Mano, achei o campo e digitei a busca!")

    # 6. EXECUTAR (Apertar Enter é mais seguro que procurar o botão de lupa)
    campo_busca.send_keys(Keys.ENTER)
    print("Busca realizada com sucesso!")

except Exception as e:
    # Se o Google mudar o 'name', ele cai aqui e te avisa
    print(f"Opa, a blindagem falhou: {e}")
