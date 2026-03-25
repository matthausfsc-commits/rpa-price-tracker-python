from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
campo = espera.until(EC.presence_of_element_located((By.ID, "APjFqb")))
from webdriver_manager.chrome import ChromeDriverManager

def iniciar_robo_veloz():
    chrome_options = Options()
    
    # --- CONFIGURAÇÕES DE VELOCIDADE ---
    chrome_options.add_argument("--disable-gpu") # Desativa processamento gráfico pesado
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--blink-settings=imagesEnabled=false") # NÃO CARREGA IMAGENS (Voa!)
    
    # --- DISFARCE ANTI-CAPTCHA ---
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    
    servico = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=servico, options=chrome_options)
    return driver

def executar_busca_rapida():
    driver = iniciar_robo_veloz()
    # Criamos um "Vigia" que espera até 20 segundos
    espera = WebDriverWait(driver, 20)
    
    try:
        print("⚡ Indo direto ao ponto...")
        driver.get("https://www.google.com")

        # Em vez de sleep, o robô espera o campo de busca 'existir' na tela
        campo = espera.until(EC.presence_of_element_id("APjFqb")) # ID real da busca do Google
        
        campo.send_keys("Python RPA")
        campo.submit()
        
        print("✅ Busca concluída com sucesso!")

    except Exception as e:
        print(f"❌ Ocorreu um erro: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    executar_busca_rapida()