"""
    ATENÇÃO – CÓDIGO EDUCACIONAL (NÃO UTILIZAR EM PRODUÇÃO)

    Este código foi desenvolvido exclusivamente para fins didáticos,
    no contexto da disciplina Tecnologias e Programação Integrada.

    O objetivo é demonstrar o uso de LLMs/SLMs com tool calling, permitindo
    que um modelo de linguagem decida qual função Python executar a
    partir de uma entrada em linguagem natural.

    IMPORTANTE:
    - Este código NÃO possui guardrails de segurança.
    - Não há validação robusta de entrada.
    - Não há controle de permissões ou autenticação.
    - Não há proteção contra uso indevido, chamadas indevidas ou escrita não autorizada.
    - NÃO deve ser executado em ambientes de produção.

    Antes de qualquer uso real, seria necessário implementar:
    - Validações de entrada
    - Controle de acesso
    - Limitação de escopo das tools
    - Logs, auditoria e monitoramento
    - Tratamento de erros e exceções
    - Políticas de segurança e compliance

    Autor: Prof. Victor

"""
import os
import json
from tools import mult,div,sub,somar
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq()


tools = [
    {
        "type": "function",
        "function": {
            "name": "somar",
            "description": "Soma dois números",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "number"},
                    "b": {"type": "number"}
                },
                "required": ["a", "b"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "mult",
            "description": "Multiplica dois números",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "number"},
                    "b": {"type": "number"}
                },
                "required": ["a", "b"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "div",
            "description": "Divide dois números",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "number"},
                    "b": {"type": "number"}
                },
                "required": ["a", "b"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "sub",
            "description": "Subtrai dois números",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "number"},
                    "b": {"type": "number"}
                },
                "required": ["a", "b"]
            }
        }
    }
]

def perguntar(pergunta: str):
    response = client.chat.completions.create(
        # model="gpt-4o-mini",
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "system", "content": "Você é um assistente que decide qual função usar."},
            {"role": "user", "content": pergunta}
        ],
        tools=tools,
        tool_choice="auto",
        temperature=0
    )

    message = response.choices[0].message

    if message.tool_calls:
        tool_call = message.tool_calls[0]
        tool_name = tool_call.function.name
        args = json.loads(tool_call.function.arguments)

        print(f"Tool chamada: {tool_name}")
        print(f"Argumentos: {args}")

        if tool_name == "somar":
            return somar(**args)

        if tool_name == "mult":
            return mult(**args)
        
        if tool_name == "div":
            return div(**args)

        if tool_name == "sub":
            return sub(**args)



    return message.content


print(perguntar("Qual é a div de 10 e 20"))
