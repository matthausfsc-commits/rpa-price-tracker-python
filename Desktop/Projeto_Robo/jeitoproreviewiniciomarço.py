import os
import pandas as pd
from PyPDF2 import PdfReader
from datetime import datetime

# --- CONFIGURAÇÃO INTELIGENTE (Mês 5: Automação Real) ---
# O os.path.abspath(__file__) garante que o robô saiba onde está em qualquer PC
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PASTA_CATALOGOS = os.path.join(BASE_DIR, "catalogos")
ARQUIVO_EXCEL = os.path.join(BASE_DIR, "Relatorio_Paginas_Catalogos.xlsx")

def preparar_ambiente():
    """Verifica se a pasta existe. Se não existir, o robô cria sozinho!"""
    if not os.path.exists(PASTA_CATALOGOS):
        os.makedirs(PASTA_CATALOGOS)
        print(f"📂 Pasta '{PASTA_CATALOGOS}' criada automaticamente.")
    else:
        print("📂 Pasta de catálogos verificada e pronta.")

def contar_paginas_pdf(caminho_pdf):
    """Tenta ler o PDF e retorna o número de páginas ou o erro formatado."""
    try:
        reader = PdfReader(caminho_pdf)
        return len(reader.pages)
    except Exception as e:
        return f"Erro de Leitura: {str(e)}"

def executar_rpa_pro():
    print("\n🚀 --- INICIANDO PROCESSO DE CONTAGEM PRO ---")
    
    # 1. Preparar o terreno (Mês 5)
    preparar_ambiente()
    
    dados_finais = []
    arquivos_na_pasta = os.listdir(PASTA_CATALOGOS)
    
    # Filtra apenas ficheiros PDF
    pdfs = [f for f in arquivos_na_pasta if f.lower().endswith(".pdf")]

    if not pdfs:
        print("⚠️  AVISO: Coloca os teus PDFs na