import pandas as pd


def robo_autossuficiente():
    try:
        # 1. Cria os dados primeiro
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
        df = pd.DataFrame(dados)
        limite_preco = 200

        # 2. Filtra e Ordena (Tudo aqui dentro da função!)
        df_filtrado = df[df["Preco"] > limite_preco]
        df_filtrado = df_filtrado.sort_values(by="Preco", ascending=False)

        # 3. Salva o arquivo
        df_filtrado.to_excel("relatorio_final.xlsx", index=False)

        # 4. EXIBE NO TERMINAL (Isso é o que falta para você ver o resultado!)
        print("\n✅ RELATÓRIO GERADO COM SUCESSO!")
        print(df_filtrado)

    except Exception as e:
        print(f"❌ Erro dentro da função: {e}")


# O "Gatilho" para o robô começar a trabalhar
if __name__ == "__main__":
    robo_autossuficiente()
