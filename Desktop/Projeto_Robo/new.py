import requests
import logging
from datetime import datetime

# Configuração de Log (Maintenance & Legacy)
logging.basicConfig(filename='robot_log.log', level=logging.INFO)

def busca_dados():
    try:
        response = requests.get("https://api.exemplo.com/v1/data", timeout=10)
        response.raise_for_status() # Gera erro se o status não for 200
        return response.json()
    except requests.exceptions.RequestException as e:
        # Aqui entra a leitura e interpretação do erro
        logging.error(f"{datetime.now()} - Erro na API: {e}")
        return None

def salvar_relatorio(dados):
    if dados:
        with open('relatorio_final.csv', 'a') as f:
            f.write(f"{datetime.now()};{dados['valor']}\n")
        print("Dados salvos com sucesso.")

# Execução do Ciclo
if __name__ == "__main__":
    dados = busca_dados()
    salvar_relatorio(dados)