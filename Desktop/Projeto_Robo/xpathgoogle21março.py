from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://www.google.com")

try:
    # --- ANÁLISE DO XPATH BOM ---

    # Jeito Ruim (Caminho Absoluto): /html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea
    # Jeito Bom (Relativo pela Alma):
    xpath_blindado = "//textarea[@title='Pesquisar']"

    # Tradução: "Busque em QUALQUER LUGAR (//) uma CAIXA DE TEXTO (textarea)
    # que tenha o TÍTULO (@title) exatamente como 'Pesquisar'"

    campo = driver.find_element(By.XPATH, xpath_blindado)
    campo.send_keys("Python RPA")
    print(
        "XPath funcionou! Ele achou o elemento pela característica, não pelo caminho."
    )

except Exception as e:
    print(f"Erro: {e}")
