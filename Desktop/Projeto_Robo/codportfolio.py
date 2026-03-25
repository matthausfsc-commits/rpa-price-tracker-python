import requests
import logging
import csv
from datetime import datetime

# 1. Configuração de Maintenance (Legado)
logging.basicConfig(filename='automacao.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def executar_robo():
    url = "https://jsonplaceholder.typicode.com/todos/1" # API de teste real
    
    try:
        print("🤖 Iniciando busca de dados...")
        response = requests.get(url, timeout=5)
        response.raise_for_status() # Interpretação de erro (404, 500, etc)
        dados = response.json()
        
        # 2. Uso do 'with open' para salvar (Segurança de dados)
        with open('relatorio_vendas.csv', 'a', newline='') as f:
            escritor = csv.writer(f)
            # Salvando: Data, ID do Pedido e Status
            escritor.writerow([datetime.now(), dados['id'], dados['title']])
        
        logging.info("Sucesso: Dados processados e salvos no CSV.")
        print("✅ Processo finalizado com sucesso!")

    except Exception as e:
        # 3. Tratamento de erro que "não explode" o terminal
        logging.error(f"Falha na automação: {e}")
        print(f"❌ Erro detectado. Verifique o arquivo 'automacao.log' para detalhes.")

if __name__ == "__main__":
    executar_robo()