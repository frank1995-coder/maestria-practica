
def sumar(a: int, b: int) -> int:
    return a + b

def restar(a: int, b: int) -> int:
    return a - b    

def multiplicar(a: int, b: int) -> int:
    return a * b

def dividir(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a / b

def main():
    print("Calculadora simple")
    print("Suma: ", sumar(5, 3))
    print("Resta: ", restar(5, 3))
    print("Multiplicación: ", multiplicar(5, 3))
    print("División: ", dividir(5, 3))

if __name__ == "__main__":
    main()

