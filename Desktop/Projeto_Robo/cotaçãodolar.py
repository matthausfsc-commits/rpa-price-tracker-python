from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

def iniciar_navegador():
    # Mês 5: Configuração Pro (Instala o driver sozinho)
    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico)
    return navegador

def pesquisar_cotacao():
    driver = iniciar_navegador()
    
    try:
        print("🌐 Abrindo o Google...")
        driver.get("https://www.google.com")

        # Mês 1: Localizando o campo de busca (Interação)
        # O 'q' é o nome do campo de pesquisa do Google
        campo_busca = driver.find_element(By.NAME, "q")
        
        print("⌨️ Digitando pesquisa...")
        campo_busca.send_keys("cotação dolar hoje")
        campo_busca.send_keys(Keys.ENTER)

        # Espera um pouco para o site carregar (Mês 2)
        time.sleep(3)

        # Mês 2/5: Pegando o valor da tela com tratamento de erro
        valor_dolar = driver.find_element(By.CLASS_NAME, "SwHCTb").text
        print(f"💰 VALOR ENCONTRADO: R$ {valor_dolar}")

    except Exception as e:
        print(f"❌ Erro durante a navegação: {e}")
    
    finally:
        print("🔌 Fechando o navegador em 5 segundos...")
        time.sleep(5)
        driver.quit()

if __name__ == "__main__":
    pesquisar_cotacao()