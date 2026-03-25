import pandas as pd
import requests
import logging
from tqdm import tqdm

# Configuração de Log
logging.basicConfig(
    filename="robot_api.log", level=logging.INFO, format="%(asctime)s - %(message)s"
)


def buscar_cotacao_real(moeda):
    """Busca a cotação atualizada via API pública."""
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    try:
        response = requests.get(url)
        data = response.json()
        # A API retorna um dicionário, pegamos o valor de 'bid' (compra)
        return float(data[f"{moeda}BRL"]["bid"])
    except Exception as e:
        logging.error(f"Erro ao buscar {moeda}: {e}")
        return None


def executar_robo_pro():
    moedas_alvo = ["USD", "EUR", "BTC"]
    resultados = []

    print("\n🌐 Conectando ao mercado financeiro...")

    for m in tqdm(moedas_alvo, desc="Capturando Cotações Reais", colour="cyan"):
        valor = buscar_cotacao_real(m)
        if valor:
            resultados.append({"Moeda": m, "Valor Atual (R$)": valor})

    if resultados:
        df = pd.DataFrame(resultados)
        df.to_excel("cotacoes_reais.xlsx", index=False)
        print("\n✅ Planilha atualizada com valores do mercado!")
        logging.info("Cotações reais salvas com sucesso.")
    else:
        print("\n❌ Não foi possível obter dados reais.")


if __name__ == "__main__":
    executar_robo_pro()
