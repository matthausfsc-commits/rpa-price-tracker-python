from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 1. Configurações de Blindagem e Anti-Fechamento
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument(
    "--start-maximized"
)  # Abre em tela cheia (fica melhor no vídeo)

driver = webdriver.Chrome(options=chrome_options)

try:
    # 2. Navegação
    print("Iniciando o robô...")
    driver.get("https://scholar.google.com.br/")
    time.sleep(2)

    # 3. Localização do campo de busca por XPath Blindado
    # Procuramos o input que tem o nome 'q' (padrão do Google)
    busca = driver.find_element(By.XPATH, "//input[@name='q']")

    # 4. Ação de Digitação (Simulando humano)
    busca.send_keys("Automação RPA Python")
    time.sleep(1)
    busca.send_keys(Keys.ENTER)
    time.sleep(3)

    # 5. Extração de Dados (O momento "Uau" do vídeo)
    print("Extraindo títulos dos artigos encontrados:")
    # Pegamos todos os títulos que são links (tag 'h3')
    titulos = driver.find_elements(By.XPATH, "//h3/a")

    for i, titulo in enumerate(titulos[:5], 1):  # Pega os 5 primeiros
        print(f"{i}. {titulo.text}")

    print("\nTarefa concluída com sucesso!")

except Exception as e:
    print(f"Erro durante a execução: {e}")

# O navegador continuará aberto por causa do 'detach'
