from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# 1. Configurações de Blindagem e Visual
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument(
    "--window-size=900,1000"
)  # Tamanho ideal para dividir a tela

# Disfarce básico para o robô
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(options=chrome_options)

try:
    # 2. Navegação para o site de teste de países
    print("Iniciando coleta de dados estruturados...")
    driver.get("https://www.scrapethissite.com/pages/simple/")
    time.sleep(3)  # Tempo para você começar a gravação

    # 3. Localização dos dados via XPath Blindado
    # Vamos pegar o nome dos países (tag 'h3' com classe 'country-name')
    paises = driver.find_elements(By.XPATH, "//h3[@class='country-name']")
    capitais = driver.find_elements(By.XPATH, "//span[@class='country-capital']")

    print(f"Sucesso! Encontrados {len(paises)} registros.")
    print("-" * 30)

    # 4. Extração e exibição no console (O momento do vídeo!)
    for i in range(5):  # Pega os 5 primeiros para o vídeo ser rápido
        nome = paises[i].text.strip()
        capital = capitais[i].text.strip()
        print(f"País: {nome} | Capital: {capital}")
        time.sleep(0.5)  # Efeito visual pro cliente ver o robô "lendo"

    print("-" * 30)
    print("Extração concluída. Dados prontos para Excel/Banco de Dados.")

except Exception as e:
    print(f"Erro na automação: {e}")
