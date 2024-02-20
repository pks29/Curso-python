# Diccionario de palabras y sus significados en español
diccionario = {
    "yellow": "Amarillo",
    "greem": "Verde",
    "blue": "Azul",
    "naranjo": "orange",
    "purple": "Violeta",
    "red": "Rojo"
}

def traducir_palabra(palabra):
    if palabra in diccionario:
        return diccionario[palabra]
    else:
        return None

def main():
    while True:
        palabra = input("Ingrese Un color primario o segundario en ingles (o 'salir' para cerrar el programa): ").lower()
        
        if palabra == 'salir':
            print("¡Gracias por usar el programa!")
            break
        
        significado = traducir_palabra(palabra)
        
        if significado:
            print(f"La traducción de '{palabra}' es '{significado}'.")
        else:
            print(f"No se encontró la traducción de '{palabra}'.")
            continuar = input("¿Desea buscar otra palabra? (s/n): ")
            if continuar.lower() != 's':
                print("¡Gracias por usar el programa!")
                break

if __name__ == "__main__":
    main()
