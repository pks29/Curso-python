def main():
    notas = []

    # Pedir al usuario que ingrese las 5 notas
    for i in range(5):
        while True:
            try:
                nota = float(input(f"Ingrese la nota {i+1} (entre 0 y 10): "))
                if nota < 0 or nota > 10:
                    print("Ingrese un valor entre 0 y 10.")
                    continue
                notas.append(nota)
                break
            except ValueError:
                print("Por favor, ingrese solo valores numéricos.")

    # Mostrar todas las notas
    print("Las notas ingresadas son:")
    for nota in notas:
        print(nota, end=" ")
    print()

    # Calcular la nota media
    nota_media = sum(notas) / len(notas)
    print(f"Nota media: {nota_media:.2f}")

    # Encontrar la nota más alta y la más baja
    nota_mas_alta = max(notas)
    nota_mas_baja = min(notas)
    print(f"Nota más alta: {nota_mas_alta}")
    print(f"Nota más baja: {nota_mas_baja}")

if __name__ == "__main__":
    main()