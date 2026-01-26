xp_maximo = 500 # Corrigi para 500 pq 50 era muito pouco perto do atual!
xp_atual = 350
largura_total_pixels = 200

ganho_base = 50
bonus = 2 

# Atualizando o XP atual com o bônus
xp_atual = xp_atual + (ganho_base * bonus)

# Aumentando o XP máximo em 10% (usando PONTO e sem acento)
xp_maximo = xp_maximo * 1.10

# Calculando a largura proporcional da barra
largura_preenchida = (xp_atual * largura_total_pixels) / xp_maximo

print(f"Novo XP máximo: {xp_maximo}")
print(f"Novo XP Atual: {xp_atual}")
print(f"Largura da Barra: {largura_preenchida:.2f}px") # O :.2f arredonda o resultado