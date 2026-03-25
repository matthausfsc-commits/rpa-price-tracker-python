import pandas as pd
import requests
import logging
import time
from datetime import datetime
from tqdm import tqdm

# 1. Configuração de Log (Para o seu caderno: Rastreabilidade)
logging.basicConfig(
    filename="robot_log.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def buscar_cotacao(moeda):
    """Busca o valor real na API."""
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        return float(data[f"{moeda}BRL"]["bid"])
    except Exception as e:
        logging.error(f"Erro ao buscar {moeda}: {e}")
        return None


def executar_automacao():
    # 2. Sua lista personalizada (Pode aumentar aqui!)
    moedas_alvo = ["USD", "EUR", "BTC", "GBP", "JPY", "CAD", "ARS", "ETH", "CHF"]
    resultados = []

    print(
        f"\n🚀 Iniciando Robô de Cotações - {datetime.now().strftime('%d/%m/%Y %H:%M')}"
    )

    # 3. Barra de Progresso (UX)
    for m in tqdm(moedas_alvo, desc="Capturando Dados Reais", colour="green"):
        valor = buscar_cotacao(m)
        if valor:
            resultados.append({"Moeda": m, "Valor Atual (R$)": valor})
        time.sleep(0.3)  # Pequeno delay para a API não bloquear

    if resultados:
        df = pd.DataFrame(resultados)

        # 4. Nome do arquivo com Data e Hora (Organização)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
        nome_arquivo = f"relatorio_{timestamp}.xlsx"

        # 5. Tentativa de salvamento (Resiliência)
        try:
            df.to_excel(nome_arquivo, index=False)
            print(f"\n✅ Sucesso! Gerado: {nome_arquivo}")
            logging.info(f"Arquivo gerado: {nome_arquivo}")
        except PermissionError:
            print(f"\n❌ ERRO: O arquivo {nome_arquivo} está aberto no Excel. Feche-o!")
            logging.warning("Falha ao salvar: Arquivo aberto pelo usuário.")
    else:
        print("\n❌ Nenhuma cotação foi capturada.")


if __name__ == "__main__":
    executar_automacao()
