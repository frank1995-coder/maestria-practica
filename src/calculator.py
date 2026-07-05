
def sumar(a, b) :
    return a + b

def restar(a, b) :
    return a - b

def multiplicar(a: int, b: int) -> int:
    return a * b

def dividir(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a / b

def calcular(operacion: str, a: int, b: int):
    if operacion == "sumar":
        return sumar(a, b)
    elif operacion == "restar":
        return restar(a, b)
    elif operacion == "multiplicar":
        return multiplicar(a, b)
    elif operacion == "dividir":
        return dividir(a, b)
    else:
        raise ValueError("Operación no válida.")

def main():
    print("Calculadora simple")
    print("Suma: ", sumar(5, 3))
    print("Resta: ", restar(5, 3))
    print("Multiplicación: ", multiplicar(5, 3))
    print("División: ", dividir(5, 3))

if __name__ == "__main__":
    main()

