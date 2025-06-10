import requests

async def enviar_compra(payload):
    try:
        response = requests.post("http://localhost:8080/api/compras", json=payload, timeout=10)
        if response.status_code == 200:
            return True, "✅ Compra concluída com sucesso!"
        elif response.status_code == 400:
            return False, f"⚠️ Erro na requisição: {response.json().get('mensagem')}"
        else:
            return False, f"❌ Erro desconhecido: {response.status_code}"
    except requests.RequestException as e:
        return False, f"🔥 Falha na comunicação com o servidor: {str(e)}"

