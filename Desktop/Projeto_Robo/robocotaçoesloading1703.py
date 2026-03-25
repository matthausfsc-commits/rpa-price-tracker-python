import pandas as pd
import time
from tqdm import tqdm  # A estrela do show
import logging

logging.basicConfig(filename="robot_log.log", level=logging.INFO)


def buscar_cotacoes_PRO():
    moedas = ["USD", "EUR", "GBP", "JPY", "CAD", "AUD", "BTC", "ETH", "CHF"]
    dados_finais = []

    print("\n🌐 Acessando API de Cotações...")

    # O 'tqdm' cria a barra de progresso baseada no tamanho da lista
    for moeda in tqdm(moedas, desc="Baixando Moedas", unit="moeda", colour="green"):
        # Simula o tempo de resposta do servidor (0.5 segundos por moeda)
        time.sleep(0.5)

        # Simulação de captura
        valor_fake = 5.0 + (time.time() % 1)
        dados_finais.append({"Moeda": moeda, "Valor": round(valor_fake, 2)})

    return pd.DataFrame(dados_finais)


def executar():
    try:
        df = buscar_cotacoes_PRO()

        print("\n💾 Gerando relatórios...")
        df.to_excel("relatorio_final.xlsx", index=False)

        print("✅ Tudo pronto! O robô finalizou a missão.")

    except Exception as e:
        print(f"\n❌ Falha crítica: {e}")


if __name__ == "__main__":
    executar()
