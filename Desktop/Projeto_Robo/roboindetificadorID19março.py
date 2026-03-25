from selenium import webdriver
from selenium.common.exceptions import WebDriverException

driver = webdriver.Chrome()

# Guardamos a URL em uma variável para ficar fácil de conferir
minha_url = "https://www.google.com"  # <--- Cole a sua URL real aqui entre as aspas

try:
    print(f"Tentando acessar: {minha_url}")
    driver.get(minha_url)
    print("Boa! O site carregou com sucesso.")

    # AGORA SIM, depois que o site abriu, a gente busca o ID
    # elemento = driver.find_element(By.ID, "meu-id")

except WebDriverException as e:
    print("\n--- OPA, ERRO DE CONEXÃO ---")
    print(f"Mano, o site {minha_url} não abriu.")
    print("Dica: Verifique se digitou o 'https://' certinho ou se o site existe.")
    # Aqui o código não "crasha" o PC, ele apenas te avisa o que houve.

# driver.quit() # Só descomente se quiser que o navegador feche sozinho
