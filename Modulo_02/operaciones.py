def suma(a, b):
    """Función para sumar dos números"""
    return a + b

def resta(a, b):
    """Función para restar dos números"""
    return a - b

def multiplicacion(a, b):
    """Función para multiplicar dos números"""
    return a * b

def division(a, b):
    """Función para dividir dos números"""
    if b == 0:
        return "Error: No se puede dividir por cero"
    return a / b