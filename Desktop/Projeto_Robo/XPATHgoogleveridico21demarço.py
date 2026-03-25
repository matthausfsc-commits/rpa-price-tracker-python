from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 1. Criamos as configurações (Options)
options = Options()

# 2. A "TRAVA": Diz pro Chrome não fechar quando o Python terminar
options.add_experimental_option("detach", True)

# 3. Passamos as opções para o driver
driver = webdriver.Chrome(options=options)

driver.get("https://www.google.com")

print("O robô terminou, mas a janela ficou aberta. Pode inspecionar à vontade!")

driver = webdriver.Chrome()
driver.get("https://www.google.com")

try:
    # Vamos buscar o body pela alma que aparece no seu print!
    # A gente usa o asterisco '*' para dizer: "Ache qualquer elemento que tenha esse jsmodel"
    elemento_alma = driver.find_element(By.XPATH, "//*[@jsmodel='hspDDf']")

    print("Mano, o robô encontrou a alma do body com sucesso!")

except Exception as e:
    print(f"Erro ao caçar a alma: {e}")
