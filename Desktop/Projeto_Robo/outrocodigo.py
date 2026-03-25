def robo_autossuficiente():
    try:
        # 1. PRIMEIRO: Cria a base de dados (O 'df' nasce aqui)
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

        # 2. SEGUNDO: Define o limite (O 'limite_preco' nasce aqui)
        limite_preco = 200

        # 3. TERCEIRO: Agora sim você filtra (Porque o 'df' e o 'limite' já existem!)
        df_filtrado = df[df["Preco"] > limite_preco]

        # 4. QUARTO: Ordena e Salva
        df_filtrado = df_filtrado.sort_values(by="Preco", ascending=False)
        df_filtrado.to_excel("relatorio_final.xlsx", index=False)

        print("✅ Sucesso! O relatório ordenado foi gerado.")
        print(df_filtrado)

    except Exception as e:
        print(f"❌ Erro: {e}")
