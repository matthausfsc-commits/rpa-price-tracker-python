import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# --- CONFIGURAÇÃO PRO (Mês 5: Robustez) ---
def iniciar_driver():
    chrome_options = Options()
    # Disfarce para o Google não sacar que é robô de cara
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    
    # Se quiser que seja ULTRA rápido, descomente a linha abaixo (tira as imagens)
    # chrome_options.add_argument("--blink-settings=imagesEnabled=false")

    servico = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=servico, options=chrome_options)
    return driver

def realizar_busca_profissional(termo):
    driver = iniciar_driver()
    # O "Vigia": Espera até 15 segundos por um elemento
    wait = WebDriverWait(driver, 15)
    
    try:
        print(f"🚀 Iniciando busca por: {termo}")
        driver.get("https://www.google.com")

        # Mês 2: Localizando o campo de busca de forma segura
        # Aqui corrigimos o erro de atributo que deu no seu print!
        busca_input = wait.until(EC.presence_of_element_located((By.NAME, "q")))
        
        busca_input.send_keys(termo)
        busca_input.submit()

        # Mês 3: Extraindo títulos dos resultados
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h3")))
        titulos = driver.find_elements(By.CSS_SELECTOR, "h3")
        
        lista_resultados = []
        for t in titulos[:5]: # Pega os top 5
            if t.text:
                lista_resultados.append({"Título": t.text, "Fonte": "Google Search"})

        # Gerando o Excel (Diferencial Jr.)
        df = pd.DataFrame(lista_resultados)
        df.to_excel("Resultados_Busca_RPA.xlsx", index=False)
        print("✅ Sucesso! Relatório gerado com os dados da web.")

    except Exception as e:
        print(f"⚠️ Erro capturado: {e}")
    
    finally:
        print("🔌 Fechando navegador em 5s...")
        time.sleep(5)
        driver.quit()

if __name__ == "__main__":
    realizar_busca_profissional("Vagas RPA Python Júnior")