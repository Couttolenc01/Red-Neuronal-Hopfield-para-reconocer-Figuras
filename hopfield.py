

def leer_patron(ruta):
    patron = []
    with open(ruta, 'r') as f:
        for linea in f:
            for valor in linea.strip().split():
                if valor == '1':
                    patron.append(1)
                else:
                    patron.append(-1)
    return patron


#Creación de matriz
def crear_matriz_pesos(patrones):
    n = len(patrones[0])
    W = [[0 for _ in range(n)] for _ in range(n)]

    for p in patrones:
        for i in range(n):
            for j in range(n):
                if i != j:
                    W[i][j] += p[i] * p[j]
    return W


def actualizar(W, estado):
    n = len(estado)
    nuevo_estado = estado[:]
    cambios = 0

    for i in range(n):
        suma = 0
        for j in range(n):
            suma += W[i][j] * estado[j]
        nuevo_valor = 1 if suma >= 0 else -1
        if nuevo_valor != estado[i]:
            cambios += 1
        nuevo_estado[i] = nuevo_valor
    return nuevo_estado, cambios

#Imprime un patrón en formato de matriz
def imprimir_patron(patron, filas, columnas):
    for i in range(filas):
        linea = ''
        for j in range(columnas):
            if patron[i * columnas + j] == 1:
                linea += '█'
            else:
                linea += ' '
        print(linea)
    print()


def main():
    p1 = leer_patron('Datasets/i.txt')
    p2 = leer_patron('Datasets/ii.txt')
    p3 = leer_patron('Datasets/iii.txt')
    p4 = leer_patron('Datasets/x.txt')

#Verificar que todos los patrones tengan la misma longitud
    print("Len i.txt:", len(p1))
    print("Len ii.txt:", len(p2))
    print("Len iii.txt:", len(p3))
    print("Len x.txt:", len(p4))


    patrones = [p1, p2, p3, p4]

    # Matriz de pesos
    W = crear_matriz_pesos(patrones)

    
    x = leer_patron('Datasets/ruido.txt')
    print("Longitud de ruido.txt:", len(x))

    print("Patrón de entrada (ruidoso):")
    imprimir_patron(x, 8, 5)

    
    iteraciones = 0
    while True:
        nuevo_x, cambios = actualizar(W, x)
        iteraciones += 1
        if cambios == 0:
            break
        x = nuevo_x

    print(f"Convergió en {iteraciones} iteraciones.\n")
    print("Patrón reconocido:")
    imprimir_patron(x, 8, 5)


if __name__ == '__main__':
    main()