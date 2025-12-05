import random
import sys
sys.setrecursionlimit(10000)

def generar_matriz(filas, columnas):
    matriz = []
    for _ in range(filas):
        fila = [random.randint(1, 9) for _ in range(columnas)]
        matriz.append(fila)
    return matriz

def brute_force(matriz, i, j, costoActual, mejorCosto):
    filas = len(matriz)
    columnas = len(matriz[0])

    if i >= filas or j >= columnas:
        return mejorCosto

    costoActual += matriz[i][j]

    if i == filas - 1 and j == columnas - 1:
        return min(mejorCosto, costoActual)

    mejorCosto = brute_force(matriz, i, j + 1, costoActual, mejorCosto)
    mejorCosto = brute_force(matriz, i + 1, j, costoActual, mejorCosto)

    return mejorCosto


def calcular_brute_force(matriz):
    return brute_force(matriz, 0, 0, 0, float("inf"))

def calcular_dp(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])

    dp = [[0] * columnas for _ in range(filas)]

    dp[0][0] = matriz[0][0]

    for j in range(1, columnas):
        dp[j][j] = 99  

    for j in range(1, columnas):
        dp[0][j] = dp[0][j - 1] + matriz[0][j]

    for i in range(1, filas):
        dp[i][0] = dp[i - 1][0] + matriz[i][0]

    for i in range(1, filas):
        for j in range(1, columnas):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + matriz[i][j]

    return dp[filas - 1][columnas - 1]

def main():
    print("CAMINO DE COSTO MiNIMO")
    filas = int(input("Ingrese numero de filas: "))
    columnas = int(input("Ingrese número de columnas: "))

    matriz = generar_matriz(filas, columnas)

    print("\nMatriz generada:")
    for fila in matriz:
        print(fila)

    print("\nCalculando con FUERZA BRUTA...")
    costo_brute = calcular_brute_force(matriz)
    print("Costo mInimo (Brute Force):", costo_brute)

    print("\nCalculando con PROGRAMACION DINAMICA...")
    costo_dp = calcular_dp(matriz)
    print("Costo minimo (DP):", costo_dp)

    print("\nRESULTADO FINAL:")
    print("Fuerza bruta:", costo_brute)
    print("Programacion dinamica:", costo_dp)

main()
