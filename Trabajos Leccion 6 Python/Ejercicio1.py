from FuncionesEjercicio1 import pares, impares

def main():
    while True:
        try:
            numero = int(input("Ingrese un número del 2 al 100 (0 para salir): "))
            
            if numero == 0:
                print("Saliendo del programa...")
                break
                
            if numero < 2 or numero > 100:
                print("El número ingresado no está en el rango permitido (2-100). Intente nuevamente.")
                continue
                
            if numero % 2 == 0:
                pares(numero)
            else:
                impares(numero)
                
            break  # Salir del bucle después de imprimir los números
        except ValueError:
            print("Por favor, ingrese solo valores numéricos.")

if __name__ == "__main__":
    main()
