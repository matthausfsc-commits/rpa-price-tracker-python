import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# [LOGGING] Configura o monitoramento do robô
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def executar_automacao():
    # [OPTIONS] Configurações do navegador
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_experimental_option("prefs", {"translate_enabled": False})

    driver = webdriver.Chrome(options=chrome_options)

    try:
        logging.info("Iniciando navegação...")
        driver.get("http://books.toscrape.com/")

        # [EXTRAÇÃO] Capturando título e preço para bater com sua descrição
        # Pegamos o primeiro livro da vitrine
        livro_element = driver.find_element(By.TAG_NAME, "h3").find_element(By.TAG_NAME, "a")
        titulo = livro_element.get_attribute("title")
        preco = driver.find_element(By.CLASS_NAME, "price_color").text

        logging.info(f"Dados capturados com sucesso!")
        logging.info(f"Livro: {titulo}")
        logging.info(f"Preço: {preco}")

    except Exception as e:
        # [INTERPRETAÇÃO DE ERROS] Foco da sua quinta-feira
        logging.error(f"Erro identificado na execução: {e}")

    finally:
        # [CLEANUP] Garante que o processo encerre corretamente
        print("\n" + "="*30)
        print("AUTOMAÇÃO CONCLUÍDA")
        print("="*30)
        input("Pressione ENTER no terminal para fechar o Chrome...")
        driver.quit()

if __name__ == "__main__":
    executar_automacao()