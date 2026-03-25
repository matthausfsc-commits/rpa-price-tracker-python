from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
# Remove a barra que diz "O Chrome está sendo controlado..."
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

# Disfarça a propriedade 'navigator.webdriver' (que os sites checam)
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(options=options)
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 1. Criamos as configurações
options = Options()

# 2. Ativamos o 'detach' (desacoplar)
options.add_experimental_option("detach", True)

# 3. Passamos as configurações para o driver
driver = webdriver.Chrome(options=options)

driver.get("https://www.google.com")
from selenium.webdriver.common.keys import Keys  # Importante para apertar 'Enter'
import time

try:
    # 1. LOCALIZANDO O CAMPO DE BUSCA (A "ALMA")
    # No Google, o campo de texto tem o atributo name='q'. É super estável.
    busca = driver.find_element(By.NAME, "q")

    # 2. AÇÃO HUMANA: Digitar devagar
    busca.send_keys("Como ser um Junior RPA Developer em Fortaleza")
    print("Digitei a busca!")

    # 3. BLINDAGEM DO BOTÃO (O PULO DO GATO)
    # Às vezes o ID do botão de pesquisa some ou muda.
    # Vamos usar XPath para buscar qualquer 'input' que tenha o texto 'Pesquisa Google'
    # ou usar o próprio 'Enter' do teclado para não depender do clique.

    time.sleep(1)  # Espera um pouco para parecer humano
    busca.send_keys(Keys.ENTER)  # Apertar Enter é a forma mais blindada de pesquisar!

    print("Busca realizada com sucesso!")

except Exception as e:
    # INTERPRETAÇÃO DE ERRO: Se der erro, o Python te avisa aqui
    print(f"Mano, o robô se perdeu: {e}")
print("Pode mexer no VS Code, a página vai continuar aberta!")
