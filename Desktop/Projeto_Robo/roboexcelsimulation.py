import logging
import pandas as pd

# Configuração do LOG
logging.basicConfig(filename="execucao_cotacoes.log", level=logging.INFO)

try:
    # Simulação da captura de dados
    dados = {"Moeda": ["USD", "EUR"], "Valor": [5.10, 5.50]}
    df = pd.DataFrame(dados)

    # Gerando o EXCEL
    df.to_excel("cotacoes_hoje.xlsx", index=False)
    logging.info("Sucesso: Arquivo Excel e cotações gerados corretamente.")

except Exception as e:
    logging.error(f"Falha na execução: {e}")
