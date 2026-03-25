import requests
import time

# 1. SIMULAÇÃO DOS DADOS (O que viria do CSV ou JSON)
lead_exemplo = {
    "nome": "João Silva",
    "empresa": "Fortaleza Tech",
    "interesse": "Automação de processos com Python",
}


def simular_ia(dados):
    """Simula a chamada para a API da OpenAI (ChatGPT)"""
    print(f"🤖 IA analisando o interesse do lead: {dados['nome']}...")
    timesleep(2)
    # Aqui a IA classificaria o lead baseado no texto
    return "Lead com alto potencial - Interessado em RPA"


def enviar_para_crm_webhook(resultado):
    """Simula o envio dos dados processados para o CRM via Webhook"""
    # Em um projeto real, aqui seria a URL do HubSpot, Pipedrive, etc.
    webhook_url = "https://webhook.site/seu-id-unico"

    payload = {
        "status": "Sucesso",
        "analise_ia": resultado,
        "data_processamento": time.strftime("%Y-%m-%d %H:%M:%S"),
    }

    print(f"🚀 Enviando resultado para o CRM via Webhook...")
    # requests.post(webhook_url, json=payload) # <--- Linha que faria o envio real
    time.sleep(1)
    print(f✅ Dados integrados com sucesso: {payload}")


# --- EXECUÇÃO DO FLUXO ---
print("--- INICIANDO SCRIPT DE INTEGRAÇÃO ---")

# Passo 1: Analisar com IA
resultado_ia = simular_ia(lead_exemplo)

# Passo 2: Enviar para o CRM
enviar_para_crm_webhook(resultado_ia)

print("--- PROCESSO FINALIZADO ---")
