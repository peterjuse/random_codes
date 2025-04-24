from collections import deque

def dfs(matriz, movimientos, visitado, fila, columna):
    # Marcar la celda como visitada
    visitado[fila][columna] = True
    # Recorrer todos los movimientos posibles
    for dx, dy in movimientos:
        nfila, ncolumna = fila + dx, columna + dy
        # Verificar límites y si el vecino es un cero sin visitar
        if 0 <= nfila < len(matriz) and 0 <= ncolumna < len(matriz[0]) and \
           matriz[nfila][ncolumna] == 0 and not visitado[nfila][ncolumna]:
            dfs(matriz, movimientos, visitado, nfila, ncolumna)


# Función auxiliar para realizar BFS
def bfs(matriz, movimientos, visitado, fila, columna):
    # Crear una cola con la celda inicial
    cola = deque([(fila, columna)])
    visitado[fila][columna] = True
    while cola:
        actual_fila, actual_columna = cola.popleft()
        # Revisar todos los vecinos posibles
        for dx, dy in movimientos:
            nfila, ncolumna = actual_fila + dx, actual_columna + dy
            # Verificar límites y si el vecino es un cero sin visitar
            if 0 <= nfila < len(matriz) and 0 <= ncolumna < len(matriz[0]) and \
               matriz[nfila][ncolumna] == 0 and not visitado[nfila][ncolumna]:
                visitado[nfila][ncolumna] = True
                cola.append((nfila, ncolumna))


def contar_agujeros(matriz):
    # Definir los movimientos ortogonales (arriba, abajo, izquierda, derecha)
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # Inicializar matriz de celdas visitadas y contador de agujeros
    visitado = [[False for _ in range(len(matriz[0]))] for _ in range(len(matriz))]
    agujeros = 0
    # Recorrer toda la matriz
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            # Si encontramos un cero no visitado, es un nuevo agujero
            if matriz[i][j] == 0 and not visitado[i][j]:
                agujeros += 1
                #dfs(matriz, movimientos, visitado, i, j)  # Llamar a la función independiente dfs
                bfs(matriz, movimientos, visitado, i, j)
    return agujeros

# Ejemplo de uso
matriz = [
    [1, 0, 1, 1, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 0],
    [1, 1, 1, 0, 0],
    [1, 1, 1, 1, 1]
]

print(f"La matriz tiene {contar_agujeros(matriz)} agujeros.")
