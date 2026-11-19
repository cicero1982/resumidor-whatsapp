import sys
from src.client import enviar_prompt_llm

def executar_cli():
    print("=== Resumidor de Mensagens do WhatsApp ===")
    print("Cole o texto longo da conversa abaixo.")
    print("Para enviar, prima 'Enter' e depois 'Ctrl+D' (Mac/Linux) ou 'Ctrl+Z' seguido de 'Enter' (Windows):\n")
    
    # sys.stdin.read() permite colar múltiplas linhas de uma só vez
    texto_bruto = sys.stdin.read().strip()
    
    if not texto_bruto:
        print("\nNenhum texto foi inserido. A encerrar...")
        return
        
    print("\n⏳ A analisar a conversa e a gerar o resumo...\n")
    
    try:
        # Chama a função do client.py enviando o texto colado
        resumo = enviar_prompt_llm(texto_bruto)
        
        print("=== RESUMO (Decisões e Pendências) ===")
        print(resumo)
        print("======================================")
        
    except Exception as e:
        print(f"\n❌ Ocorreu um erro de comunicação: {e}")

# Esta é a parte que faz o código rodar quando você digita "python -m src.app"
if __name__ == "__main__":
    executar_cli()