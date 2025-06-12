import requests
import json

async def enviar_compra(payload):
    try:
        print(f"Enviando payload: {json.dumps(payload, indent=2)}")
        response = requests.post("http://localhost:8080/api/compras", json=payload, timeout=10)
        print(f"Status code: {response.status_code}")
        print(f"Response: {response.text}")
        
        if response.status_code == 200:
            return True, "✅ Compra concluída com sucesso!"
        elif response.status_code == 400:
            try:
                error_data = response.json()
                return False, f"⚠️ Erro na requisição: {error_data.get('mensagem', 'Erro desconhecido')}"
            except:
                return False, f"⚠️ Erro na requisição: {response.text}"
        else:
            return False, f"❌ Erro do servidor: {response.status_code} - {response.text}"
    except requests.RequestException as e:
        return False, f"🔥 Falha na comunicação com o servidor: {str(e)}"
    except Exception as e:
        return False, f"🔥 Erro inesperado: {str(e)}"

