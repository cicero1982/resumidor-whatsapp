import sys
from src.client import enviar_prompt_llm

def executar_cli():
    print("=== Resumidor de Mensagens do WhatsApp ===")
    print("Cole o texto longo da conversa abaixo.")
    print("Para enviar, pressione Enter e depois:")
    print("  • Windows: Ctrl+Z seguido de Enter")
    print("  • Mac/Linux: Ctrl+D\n")
    
    # sys.stdin.read() permite colar múltiplas linhas de uma só vez
    texto_bruto = sys.stdin.read().strip()
    
    if not texto_bruto:
        print("\nNenhum texto foi inserido. Encerrando...")
        return
        
    print("\n⏳ Analisando a conversa e gerando o resumo...\n")
    
    try:
        # Chama a função do client.py enviando o texto colado
        resumo = enviar_prompt_llm(texto_bruto)
        
        print("=== RESUMO (Decisões e Pendências) ===")
        print(resumo)
        print("======================================")
        
    except Exception as e:
        print(f"\n❌ Ocorreu um erro de comunicação: {e}")

if __name__ == "__main__":
    executar_cli()