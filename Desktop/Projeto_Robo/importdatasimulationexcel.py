import logging
import pandas as pd
import os  # Biblioteca para verificar arquivos

logging.basicConfig(filename="execucao_cotacoes.log", level=logging.INFO)

try:
    print("🚀 Iniciando o robô de cotações...")

    dados = {"Moeda": ["USD", "EUR"], "Valor": [5.10, 5.50]}
    df = pd.DataFrame(dados)

    nome_arquivo = "cotacoes_hoje.xlsx"
    df.to_excel(nome_arquivo, index=False)

    # Verificação física do arquivo
    if os.path.exists(nome_arquivo):
        print(f"✅ Sucesso! O arquivo '{nome_arquivo}' foi criado na pasta.")
        print(
            f"📄 Verifique também o arquivo 'execucao_cotacoes.log' para o histórico."
        )

    logging.info("Execução concluída com sucesso.")

except Exception as e:
    print(f"❌ ERRO IDENTIFICADO: {e}")
    logging.error(f"Erro na execução: {e}")
