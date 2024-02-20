def pares(numero):
    print("Los números pares siguientes son:")
    for i in range(numero + 2, 101, 2):
        print(i, end=' ')
    print()

def impares(numero):
    print("Los números impares siguientes son:")
    for i in range(numero + 2, 100, 2):
        print(i, end=' ')
    print()