import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def run_professional_bot():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        logging.info("Acessando site de livros para capturar preços...")
        driver.get("http://books.toscrape.com/") 
        
        wait = WebDriverWait(driver, 10)
        
        # [CAPTURANDO O PREÇO]
        # Localiza o preço do primeiro livro usando a classe CSS do site
        price_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "price_color")))
        
        raw_price = price_element.text
        logging.info(f"Sucesso! Preço encontrado: {raw_price}")
        
        # Aqui entra a parte de CONVERSÃO que falamos:
        # Removendo o símbolo de libra (£) para virar número
        clean_price = float(raw_price.replace("£", ""))
        logging.info(f"Preço convertido para cálculo: {clean_price}")

    except Exception as e:
        logging.error(f"Erro durante a execução: {e}")
        
    finally:
        print("\n--- TESTE DE CAMPO CONCLUÍDO ---")
        input("Pressione ENTER para fechar o navegador...")
        driver.quit()

if __name__ == "__main__":
    run_professional_bot()