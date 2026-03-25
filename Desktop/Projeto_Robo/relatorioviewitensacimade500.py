import pandas as pd
import os


def robo_autossuficiente():
    arquivo_entrada = "dados_mercado.xlsx"
    arquivo_saida = "relatorio_final.xlsx"

    try:
        # --- PASSO 1: O ROBÔ CRIA OS PRÓPRIOS DADOS ---
        # Isso garante que você nunca mais receba aquele erro de "Arquivo não encontrado"
        print("⚙️ Gerando base de dados inicial...")
        dados = {
            "Produto": [
                "Mouse",
                "Teclado",
                "Monitor",
                "Cadeira Gamer",
                "Fone",
                "Webcam",
                "teclado mecanico",
            ],
            "Preco": [150, 250, 1200, 850, 300, 600, 350],
            "Estoque": [15, 10, 5, 8, 20, 12, 5],
        }
        df_base = pd.DataFrame(dados)
        df_base.to_excel(arquivo_entrada, index=False)

        # --- PASSO 2: LEITURA E EDIÇÃO ---
        print(f"📖 Lendo arquivo: {arquivo_entrada}")
        df = pd.read_excel(arquivo_entrada)

        # EDITAR AQUI: Se quiser mudar o valor do filtro, troque o 500 abaixo
        limite_preco = 200
        print(f"⚖️ Filtrando produtos acima de R$ {limite_preco}...")

        df_filtrado = df[df["Preco"] > limite_preco].copy()

        # --- PASSO 3: CRIANDO NOVA INFORMAÇÃO ---
        # Aqui o robô calcula o valor total investido por item
        df_filtrado["Valor_Total_Estoque"] = (
            df_filtrado["Preco"] * df_filtrado["Estoque"]
        )

        # --- PASSO 4: EXPORTAÇÃO ---
        df_filtrado.to_excel(arquivo_saida, index=False)
        print(f"✅ SUCESSO! Relatório '{arquivo_saida}' gerado com os itens caros.")
        print("\n--- PRÉVIA DOS DADOS FILTRADOS ---")
        print(df_filtrado)

    except Exception as e:
        print(f"❌ Ops, algo deu errado: {e}")


if __name__ == "__main__":
    robo_autossuficiente()
# Filtra os dados
# Use o 'df' (base original) para criar o 'df_filtrado'
df_filtrado = df[df["Preco"] > limite_preco]

# ORDENAÇÃO: Coloca o mais caro no topo do Excel
df_filtrado = df_filtrado.sort_values(by="Preco", ascending=False)

# Salva o arquivo já bonitinho e ordenado
df_filtrado.to_excel("relatorio_ordenado.xlsx", index=False)
