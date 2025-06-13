import requests
import json

async def enviar_compra(payload):
    try:
        print(f"Enviando payload: {json.dumps(payload, indent=2)}")
        response = requests.post("http://localhost:8080/api/compras", json=payload, timeout=10)
        print(f"Status code: {response.status_code}")
        print(f"Response: {response.text}")
        
        if response.status_code == 200:
            # Supondo que a resposta JSON tenha um campo 'order_id'
            response_data = response.json()
            order_id = response_data.get("order_id", None)  # Tenta obter o ID do pedido da resposta
            if order_id:
                return True, "✅ Compra concluída com sucesso!", order_id  # Retorna também o ID do pedido
            else:
                return False, "⚠️ Compra realizada, mas não foi possível obter o ID do pedido.", None

        elif response.status_code == 400:
            try:
                error_data = response.json()
                return False, f"⚠️ Erro na requisição: {error_data.get('mensagem', 'Erro desconhecido')}", None
            except:
                return False, f"⚠️ Erro na requisição: {response.text}", None
        else:
            return False, f"❌ Erro do servidor: {response.status_code} - {response.text}", None

    except requests.RequestException as e:
        return False, f"🔥 Falha na comunicação com o servidor: {str(e)}", None
    except Exception as e:
        return False, f"🔥 Erro inesperado: {str(e)}", None
