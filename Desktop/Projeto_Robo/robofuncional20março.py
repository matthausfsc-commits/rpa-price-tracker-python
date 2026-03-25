from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. CONFIGURAÇÃO DE BLINDAGEM (O que já aprendemos)
options = Options()
options.add_experimental_option("detach", True)
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(options=options)

# 2. AÇÃO: Abrir o site
driver.get("https://www.google.com")

try:
    # 3. BLINDAGEM DE ESPERA (Nível Pro)
    # Aqui dizemos: "Espere até 10 segundos para o elemento com NAME='q' aparecer"
    campo_busca = WebDriverWait(driver, 10).until(
        EC.presence_of_element_id_located((By.NAME, "q"))
    )

    # 4. INTERAÇÃO
    campo_busca.send_keys("Vagas Junior RPA Python Fortaleza")
    print("Mano, achei o campo e já digitei!")

    # Apertar ENTER é a forma mais segura de pesquisar sem erro de botão
    campo_busca.send_keys(Keys.ENTER)
    print("Pesquisa enviada com sucesso!")

except Exception as e:
    print(f"Opa, deu erro na blindagem: {e}")
