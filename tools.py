"""
def somar(a, b):
    return {a + b}

def sub(a, b):
    return {a - b}

def mult(a, b):
    return {a * b}

def div(a,b):
    return {a / b}


def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32


def fahrenheit_para_celsius(f):
    return (f - 32) * 5/9


def buscar_produto(nome_produto):
    produtos = {
        "notebook": 4500,
        "mouse": 80,
        "teclado": 150
    }



def buscar_produto(nome_produto):
    estoque = {
        "notebook": 5,
        "mouse": 3,
        "teclado": 10
    }
    
    return "Produto não encontrado"



eventos = []

def criar_evento(titulo, data):
    evento = {
        "titulo": titulo,
        "data": data
    }

    eventos.append(evento)

    return f"Evento '{titulo}' criado para {data}"


def listar_eventos():
    if not eventos:
        return "Nenhum evento encontrado"

    resultado = ""

    for e in eventos:
        resultado += f"{e['titulo']} - {e['data']}\n"

    return resultado


"""""
def buscar_clima(cidade: str):
    clima = {
        "sao paulo": "24°C e nublado",
        "bauru": "30°C e ensolarado",
        "curitiba": "18°C e chuvoso"
    }
    return clima.get(cidade, "Cidade não encontrado")