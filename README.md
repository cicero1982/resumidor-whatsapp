
# Resumidor de Mensagens de WhatsApp

Aplicação de linha de comando em Python que resume textos longos de conversas,
com foco nas decisões tomadas, pendências e prazos.

## Funcionalidades

- Recebe texto colado no terminal ou lido de um arquivo `.txt`.
- Gera um resumo de até três linhas.
- Usa a API do Google Gemini.
- Mantém a chamada HTTP da IA separada da interface CLI.

## Tecnologias

- Python 3.11+
- API REST do Google Gemini
- `requests`
- `python-dotenv`

## Configuração

1. Clone o repositório e entre na pasta:

   