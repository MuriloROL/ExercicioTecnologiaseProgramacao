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
"""

def buscar_produto(nome_produto):
    produtos = {
        "notebook": 4500,
        "mouse": 80,
        "teclado": 150
    }

    if nome_produto.lower() in produtos:
        return produtos[nome_produto.lower()]
    
    return "Produto não encontrado"