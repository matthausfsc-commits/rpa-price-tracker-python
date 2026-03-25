from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

def meu_primeiro_scraping_real():
    chrome_options = Options()
    # Ativando o modo rápido (sem imagens)
    chrome_options.add_argument("--blink-settings=imagesEnabled=false")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    wait = WebDriverWait(driver, 10)
    
    try:
        print("🌐 Acessando site de câmbio...")
        # Vamos usar um site simples de ler para começar
        driver.get("https://www.infomoney.com.br/ferramentas/cambio/")

        # MÊS 2: Esperar a tabela de moedas carregar
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "value")))
        
        # Pegando os valores (Exemplo de lógica para você testar)
        valores = driver.find_elements(By.CLASS_NAME, "value")
        moedas = ["Dólar", "Euro", "Libra", "Bitcoin"] # Mês 1: Lista
        
        dados_finais = []
        for i in range(len(moedas)):
            # Mês 1: Dicionário
            dados_finais.append({
                "Moeda": moedas[i],
                "Valor": valores[i].text
            })

        # MÊS 3: Gerar o Excel
        df = pd.DataFrame(dados_finais)
        df.to_excel("Cotacoes_Mercado.xlsx", index=False)
        print("📊 SUCESSO! Arquivo 'Cotacoes_Mercado.xlsx' gerado.")

    except Exception as e:
        print(f"❌ Erro na missão: {e}")
    
    finally:
        driver.quit()

if __name__ == "__main__":
    meu_primeiro_scraping_real()