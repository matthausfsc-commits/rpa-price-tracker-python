import requests
import pandas as pd
import os
from datetime import datetime

# --- CONFIGURAÇÃO DE AMBIENTE (REVISÃO MÊS 5) ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARQUIVO_LOG = os.path.join(BASE_DIR, "diario_do_robo.txt")
ARQUIVO_EXCEL = os.path.join(BASE_DIR, "Relatorio_Final_Revisao.xlsx")

def registrar_log(mensagem):
    """Função para registrar tudo o que o robô faz (Auditoria)"""
    horario = datetime.now().strftime('%H:%M:%S')
    with open(ARQUIVO_LOG, "a", encoding="utf-8") as f:
        f.write(f"[{horario}] {mensagem}\n")
    print(f"📢 LOG: {mensagem}")

def buscar_dados_mercado():
    """Busca dados de API (Revisão Mês 4/5)"""
    url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL"
    registrar_log("Iniciando busca de dados na API...")
    
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Erro na API: Status {response.status_code}")

def processar_revisao():
    registrar_log("--- INICIANDO RITUAL DE REVISÃO ---")
    
    try:
        # 1. TESTE DE BUSCA
        dados = buscar_dados_mercado()
        dolar = float(dados['USDBRL']['bid'])
        euro = float(dados['EURBRL']['bid'])
        
        # 2. ESTRUTURA DE DADOS (REVISÃO MÊS 1)
        # Criando uma lista de dicionários (o que o Pandas ama)
        lista_estudo = [
            {"Tópico": "Mês 1: Base", "Status": "Concluído", "Detalhe": "Variáveis e Funções"},
            {"Tópico": "Mês 5: Real", "Status": "Em Revisão", "Detalhe": "Logs e Agendamento"},
            {"Tópico": "Mercado: Dólar", "Status": "Ativo", "Detalhe": f"R$ {dolar:.2f}"},
            {"Tópico": "Mercado: Euro", "Status": "Ativo", "Detalhe": f"R$ {euro:.2f}"}
        ]
        
        # 3. GERANDO EXCEL (REVISÃO MÊS 3)
        df = pd.DataFrame(lista_estudo)
        df.to_excel(ARQUIVO_EXCEL, index=False)
        registrar_log(f"Sucesso! Planilha gerada: {ARQUIVO_EXCEL}")

    except Exception as e:
        # 4. INTERPRETAÇÃO DE ERRO (O SEU DIFERENCIAL)
        erro_detalhado = f"ERRO CRÍTICO ENCONTRADO: {str(e)}"
        registrar_log(erro_detalhado)
        print("\n" + "!"*30)
        print(f"FOCO NO ERRO: {e}")
        print("!"*30 + "\n")

    finally:
        registrar_log("--- FIM DO PROCESSO DE REVISÃO ---")

if __name__ == "__main__":
    processar_revisao()