def obtener_dias_y_nombre_mes(numero_mes):
    nombres_meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio",
                     "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    dias_meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    nombre_mes = nombres_meses[numero_mes - 1]
    dias_mes = dias_meses[numero_mes - 1]
    
    return nombre_mes, dias_mes

def main():
    while True:
        try:
            numero_mes = int(input("Ingrese un número de mes (1-12): "))
            if numero_mes < 1 or numero_mes > 12:
                print("Ingrese un número entre 1 y 12.")
                continue
        except ValueError:
            print("Ingrese un número entero entre 1 y 12.")
            continue

        nombre_mes, dias_mes = obtener_dias_y_nombre_mes(numero_mes)
        
        print(f"El mes de {nombre_mes} tiene {dias_mes} días.")
        
        opcion = input("¿Desea ingresar otro número de mes? (S/N): ")
        if opcion.lower() != 's':
            print("Saliendo del programa...")
            break

if __name__ == "__main__":
    main()
