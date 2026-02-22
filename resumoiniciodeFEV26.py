import pandas as pd
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException

# [QUINTA: LEITURA E INTERPRETAÇÃO DE ERROS]
# Configurando logs para o robô "falar" o que está acontecendo
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def run_price_bot():
    # [RESOLVENDO O ERRO DE ONTEM]
    # Configurando o Chrome para NÃO mostrar o pop-up de tradução
    chrome_options = Options()
    prefs = {"translate_enabled": False}
    chrome_options.add_experimental_option("prefs", prefs)
    
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        logging.info("Starting automation... (Fetching data)")
        driver.get("https://www.exemplo.com/precos") # Substitua pelo seu site alvo
        
        # [SEGUNDA: AUTOMAÇÃO WEB]
        # Tentando localizar o preço (Handling elements)
        price_element = driver.find_element(By.ID, "price-value")
        raw_data = price_element.text # Exemplo: "R$ 1.500,00"
        
        # [TERÇA: TRATAMENTO DE DADOS COM PANDAS]
        # Cleaning data: transformando o texto em número real
        df = pd.DataFrame({'Product': ['Automation Tool'], 'Price': [raw_data]})
        df['Price'] = df['Price'].str.replace('R$', '').str.replace('.', '').str.replace(',', '.').astype(float)
        
        logging.info(f"Success! Processed price: {df['Price'].iloc[0]}")
        
    except NoSuchElementException:
        logging.error("Error: Element not found. Check if the site layout changed.")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        
    finally:
        # Sêneca: O tempo é precioso. Fechando o navegador para poupar memória.
        driver.quit()
        logging.info("Bot finished and browser closed.")

if __name__ == "__main__":
    run_price_bot()