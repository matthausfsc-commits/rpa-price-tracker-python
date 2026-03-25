import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def meu_primeiro_scraping_real():
    chrome_options = Options()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    
    servico = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=servico, options=chrome_options)
    wait = WebDriverWait(driver, 15)
    
    try:
        print("🌐 Acessando site de câmbio...")
        driver.get("https://www.infomoney.com.br/ferramentas/cambio/")

        # Bloco do Cookie (Alinhado com o driver.get)
        try:
            print("🍪 Tentando fechar o aviso de cookies...")
            botao_cookie = wait.until(EC.element_to_be_clickable((By.ID, "v_cookies-term-button")))
            botao_cookie.click()
            print("✅ Cookies aceitos!")
        except:
            print("⚠️ Sem pop-up de cookies.")

        # Bloco da Tabela (Alinhado com o try anterior)
        print("📊 Lendo dados da tabela...")
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "value")))
        
        elementos_valores = driver.find_elements(By.CLASS_NAME, "value")
        moedas = ["Dólar", "Euro", "Libra", "Bitcoin"] 
        
        dados_finais = []
        for i in range(len(moedas)):
            valor_limpo = elementos_valores[i].text
            dados_finais.append({"Moeda": moedas[i], "Valor": valor_limpo})
            print(f"💰 {moedas[i]}: {valor_limpo}")

        df = pd.DataFrame(dados_finais)
        df.to_excel("Cotacoes_Mercado.xlsx", index=False)
        print("\n🔥 SUCESSO! Arquivo gerado.")

    except Exception as e:
        print(f"❌ Erro: {e}")
    
    finally:
        driver.quit()

if __name__ == "__main__":
    meu_primeiro_scraping_real()