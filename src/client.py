import os
import requests
from dotenv import load_dotenv

load_dotenv()

def enviar_prompt_llm(texto_bruto: str) -> str:
    # Busca a chave do Gemini configurada no .env
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        return "❌ Erro: A chave 'GEMINI_API_KEY' não foi encontrada no arquivo .env."

    # Endpoint oficial do Gemini (URL limpa, sem comandos de terminal)
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent?key={api_key}"
    
    prompt_completo = (
        "Você é um assistente especializado em resumir conversas longas de WhatsApp. "
        "Devolva um resumo de até 3 linhas focando estritamente nas decisões tomadas e nas pendências/prazos. "
        "Não seja genérico, vá direto ao assunto.\n\n"
        f"Texto da conversa:\n{texto_bruto}"
    )

    # Estrutura JSON exigida pela documentação do Gemini
    payload = {
        "contents": [{
            "parts": [{"text": prompt_completo}]
        }],
        "generationConfig": {
            "temperature": 0.3
        }
    }

    headers = {
        "Content-Type": "application/json"
    }

    try:
        # A requisição POST junta a URL, o payload e os headers automaticamente
        resposta = requests.post(url, json=payload, headers=headers, timeout=30.0)
        resposta.raise_for_status()
        
        dados = resposta.json()
        # Navega no JSON de resposta do Gemini para extrair apenas o texto
        return dados["candidates"][0]["content"]["parts"][0]["text"].strip()
        
    except requests.exceptions.Timeout:
        return "❌ Erro de Conexão: A API demorou muito para responder (Timeout)."
    except requests.exceptions.HTTPError as e:
        if resposta.status_code == 400:
            return f"❌ Erro (400): Requisição inválida ou chave incorreta."
        return f"❌ Erro HTTP na API: {resposta.status_code} - {resposta.text}"
    except requests.exceptions.RequestException as e:
        return f"❌ Erro de Rede: Falha ao tentar conectar ao servidor. Detalhes: {e}"
    except KeyError:
        return f"❌ Erro inesperado ao ler a resposta da API: {dados}"