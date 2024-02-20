def main():
    # Solicitar al usuario la cantidad de notas a ingresar
    num_notas = int(input("Ingrese la cantidad de notas a ingresar: "))

    # Inicializar una lista para almacenar las notas
    notas = []

    # Solicitar al usuario ingresar las notas una por una
    for i in range(num_notas):
        nota = float(input(f"Ingrese la nota {i + 1}: "))
        notas.append(nota)

    # Calcular el promedio de las notas
    promedio = sum(notas) / num_notas

    # Contar cuántas notas son mayores que el promedio
    notas_mayores_al_promedio = sum(nota > promedio for nota in notas)

    # Mostrar el resultado
    print(f"El promedio de las notas es: {promedio}")
    print(f"Número de notas mayores que el promedio: {notas_mayores_al_promedio}")

if __name__ == "__main__":
    main()