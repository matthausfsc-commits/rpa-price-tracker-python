import pandas as pd
import logging
import time
import os

# Configuração de Log Profissional (com data e hora)
logging.basicConfig(
    filename="robot_execucao.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def salvar_excel_robusto(df, nome_arquivo, tentativas=3):
    """Tenta salvar o arquivo, mas lida com o erro se o Excel estiver aberto."""
    for i in range(tentativas):
        try:
            df.to_excel(nome_arquivo, index=False)
            print(f"✅ Arquivo '{nome_arquivo}' salvo com sucesso!")
            return True
        except PermissionError:
            print(
                f"⚠️ Erro: O arquivo '{nome_arquivo}' está aberto! Feche-o agora. Tentativa {i+1}/{tentativas}"
            )
            time.sleep(5)  # Dá 5 segundos para o humano fechar o arquivo
        except Exception as e:
            logging.error(f"Erro fatal ao salvar: {e}")
            break
    return False


def rodar_robo():
    print("🤖 Iniciando Robô de Cotações (Modo Resiliente)...")

    # 1. Simulação de captura (Aqui entraria seu scraping)
    try:
        # Simulando uma falha de conexão aleatória
        dados = {"Moeda": ["USD", "EUR", "BTC"], "Valor": [5.12, 5.54, 320000]}
        df = pd.DataFrame(dados)
        logging.info("Dados capturados com sucesso.")

        # 2. Tentativa de salvamento robusto
        sucesso = salvar_excel_robusto(df, "cotacoes_hoje.xlsx")

        if sucesso:
            print("🍺 Processo finalizado com sucesso.")
        else:
            print("❌ O robô desistiu após várias tentativas.")

    except Exception as e:
        print(f"💥 Erro crítico no motor do robô: {e}")
        logging.critical(f"Erro no motor: {e}")


if __name__ == "__main__":
    rodar_robo()
