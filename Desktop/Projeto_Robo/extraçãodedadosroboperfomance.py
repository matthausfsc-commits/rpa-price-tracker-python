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
    # --- CONFIGURAÇÃO DO NAVEGADOR ---
    chrome_options = Options()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    # Descomente a linha abaixo se quiser que o robô seja mais rápido (sem carregar imagens)
    # chrome_options.add_argument("--blink-settings=imagesEnabled=false")
    
    servico = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=servico, options=chrome_options)
    wait = WebDriverWait(driver, 15)
    
    try:
        print("🌐 Acessando site de câmbio...")
        driver.get("https://www.infomoney.com.br/ferramentas/cambio/")

        # --- MÊS 2: TRATANDO O POP-UP DE COOKIES ---
        try:
            print("🍪 Tentando fechar o aviso de cookies...")
            # Aguarda o botão de cookie ser clicável
            botao_cookie = wait.until(EC.element_to_be_clickable((By.ID, "v_cookies-term-button")))
            botao_cookie.click()
            print("✅ Cookies aceitos!")
        except Exception:
            print("⚠️ Pop-up de cookies não apareceu ou já estava fechado.")

        # --- MÊS 2: ESPERANDO A TABELA ---
        print("📊 Lendo dados da tabela...")
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "value")))
        
        # Localizando os valores e nomes das moedas
        elementos_valores = driver.find_elements(By.CLASS_NAME, "value")
        moedas = ["Dólar", "Euro", "Libra", "Bitcoin"] 
        
        dados_finais = []
        # MÊS 1: Loop para organizar os dados
        for i in range(len(moedas)):
            valor_limpo = elementos_valores[i].text
            dados_finais.append({
                "Moeda": moedas[i],
                "Valor": valor_limpo
            })
            print(f"💰 {moedas[i]}: {valor_limpo}")

        # --- MÊS 3: GERANDO O EXCEL ---
        df = pd.DataFrame(dados_finais)
        df.to_excel("Cotacoes_Mercado.xlsx", index=False)
        print("\n🔥 SUCESSO! Arquivo 'Cotacoes_Mercado.xlsx' gerado com sucesso.")

    except Exception as e:
        # MÊS 5: INTERPRETAÇÃO DE ERRO
        print(f"❌ Ocorreu um erro durante a execução: {e}")
    
    finally:
        print("🔌 Fechando o navegador em 5 segundos...")
        time.sleep(5)
        driver.quit()

if __name__ == "__main__":
    meu_primeiro_scraping_real()