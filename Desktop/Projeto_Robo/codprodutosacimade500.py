import pandas as pd
import os


def super_robo_pandas():
    nome_arquivo = "teste_automacao.xlsx"

    try:
        # --- OPÇÃO B: LER UM ARQUIVO EXISTENTE ---
        print(f"🔍 Tentando ler o arquivo: {nome_arquivo}...")
        df = pd.read_excel(nome_arquivo)

        # --- OPÇÃO A: FILTRAR DADOS ---
        # Vamos filtrar apenas produtos que custam MAIS de 500 reais
        print("Filterando produtos caros (acima de R$ 500)...")
        df_filtrado = df[df["Preco"] > 500]

        if df_filtrado.empty:
            print("⚠️ Nenhum produto acima de R$ 500 encontrado.")
        else:
            print("✅ Produtos encontrados:")
            print(df_filtrado)

            # Salva o resultado do filtro em um novo arquivo
            df_filtrado.to_excel("relatorio_caros.xlsx", index=False)
            print("\n💾 Relatório de produtos caros gerado com sucesso!")

    # --- OPÇÃO C: TRATAR ERROS ESPECÍFICOS ---
    except FileNotFoundError:
        print(f"❌ ERRO DE LEITURA: O arquivo '{nome_arquivo}' não foi encontrado!")
        print("Dica: Rode o código anterior primeiro para criar o arquivo inicial.")

    except Exception as e:
        print(f"⚠️ Ocorreu um erro inesperado: {e}")


if __name__ == "__main__":
    super_robo_pandas()
