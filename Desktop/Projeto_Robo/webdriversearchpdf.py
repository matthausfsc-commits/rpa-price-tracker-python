from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def iniciar_navegador_blindado():
    chrome_options = Options()
    
    # 1. FAZ O ROBÔ MAIS RÁPIDO: Não carrega imagens (opcional)
    # chrome_options.add_argument("--blink-settings=imagesEnabled=false") 
    
    # 2. DISFARCE: Evita que o site perceba que é um robô
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    
    # 3. VELOCIDADE: Usa o perfil do seu PC para carregar mais rápido
    chrome_options.add_argument("--start-maximized")

    servico = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=servico, options=chrome_options)
    
    # Comando extra de disfarce
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
    })
    
    return driver

# ... restante do código de busca