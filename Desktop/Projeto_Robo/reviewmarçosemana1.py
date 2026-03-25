import os
import pandas as pd
from PyPDF2 import PdfReader # Biblioteca para ler PDFs
from datetime import datetime

# --- CONFIGURAÇÃO (Mês 5: Caminhos Inteligentes) ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PASTA_CATALOGOS = os.path.join(BASE_DIR, "catalogos") # Coloque seus PDFs aqui
ARQUIVO_LOG = os.path.join(BASE_DIR, "log_processamento.txt")

def contar_paginas_pdf(caminho_pdf):
    """Função que abre o PDF e conta as páginas (Mês 1: Funções)"""
    try:
        reader = PdfReader(caminho_pdf)
        return len(reader.pages)
    except Exception as e:
        return f"Erro: {str(e)}"

def executar_rpa():
    print("🚀 Iniciando Leitura de Catálogos...")
    dados_finais = []
    
    # Verifica se a pasta existe
    if not os.path.exists(PASTA_CATALOGOS):
        print(f"❌ Erro: A pasta {PASTA_CATALOGOS} não foi encontrada!")
        return

    # Loop para ler todos os arquivos (Mês 1: Estruturas de Repetição)
    for arquivo in os.listdir(PASTA_CATALOGOS):
        if arquivo.lower().endswith(".pdf"):
            caminho_completo = os.path.join(PASTA_CATALOGOS, arquivo)
            
            print(f"📄 Processando: {arquivo}...")
            num_paginas = contar_paginas_pdf(caminho_completo)
            
            # Mês 5: Criando a estrutura para o relatório
            dados_finais.append({
                "Nome do Catálogo": arquivo,
                "Quantidade de Páginas": num_paginas,
                "Data do Processamento": datetime.now().strftime("%d/%m/%Y")
            })

    # Gerando o Excel (Mês 3: Pandas)
    if dados_finais:
        df = pd.DataFrame(dados_finais)
        df.to_excel("Relatorio_Paginas_Catalogos.xlsx", index=False)
        print("✅ Relatório gerado com sucesso!")
    else:
        print("⚠️ Nenhum PDF encontrado para processar.")

if __name__ == "__main__":
    executar_rpa()