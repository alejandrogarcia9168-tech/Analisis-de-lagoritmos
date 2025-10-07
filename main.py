import numpy as np
import time
import matplotlib.pyplot as plt

ALGORITMOS = ["Bubble Sort", "Merge Sort", "Quick Sort"]

def medir_tiempo(func, *args, **kwargs):
    start = time.perf_counter()
    resultado = func(*args, **kwargs)
    end = time.perf_counter()
    duracion_ms = (end - start) * 1000  # Convertir a milisegundos
    return duracion_ms, resultado

def lista_aleatoria(tamano, minimo=0, maximo=10000):
    return np.random.randint(minimo, maximo, size=tamano).tolist()

# Bubble Sort
def orden_burbuja(arr):
    arr_copia = arr.copy()
    n = len(arr_copia)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr_copia[j] > arr_copia[j + 1]:
                arr_copia[j], arr_copia[j + 1] = arr_copia[j + 1], arr_copia[j]
    return arr_copia

# Merge Sort
def orden_merge(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    izquierda = orden_merge(arr[:mid])
    derecha = orden_merge(arr[mid:])
    return combinar(izquierda, derecha)

def combinar(izq, der):
    resultado = []
    i = j = 0
    while i < len(izq) and j < len(der):
        if izq[i] <= der[j]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1
    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    return resultado

# Quick Sort
def orden_quick(arr):
    if len(arr) <= 1:
        return arr
    pivote = arr[0]
    menores = [x for x in arr[1:] if x < pivote]
    iguales = [x for x in arr if x == pivote]
    mayores = [x for x in arr[1:] if x > pivote]
    return orden_quick(menores) + iguales + orden_quick(mayores)

# Gráfica de resultados
def graficar_rendimiento(nombres, tiempos, cantidades):
    plt.figure(figsize=(12, 7))
    estilos = ['-', '--', '-.']
    colores = ['#FF5733', '#33C1FF', '#33FF77']

    for idx, nombre in enumerate(nombres):
        plt.plot(cantidades, tiempos[idx], estilos[idx], color=colores[idx], marker='s', markersize=6, label=nombre)
    
    plt.title("Comparación de Algoritmos de Ordenamiento", fontsize=16)
    plt.xlabel("Número de elementos en la lista", fontsize=12)
    plt.ylabel("Tiempo de ejecución (ms)", fontsize=12)
    plt.grid(True, linestyle=':', linewidth=1.2)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    tamaños = list(range(50, 1050, 50))
    resultados_tiempo = []

    for algoritmo in ALGORITMOS:
        tiempos = []
        for tam in tamaños:
            lista = lista_aleatoria(tam)
            if algoritmo == "Bubble Sort":
                tiempo, _ = medir_tiempo(orden_burbuja, lista)
            elif algoritmo == "Merge Sort":
                tiempo, _ = medir_tiempo(orden_merge, lista)
            elif algoritmo == "Quick Sort":
                tiempo, _ = medir_tiempo(orden_quick, lista)
            tiempos.append(tiempo)
        resultados_tiempo.append(tiempos)

    graficar_rendimiento(ALGORITMOS, resultados_tiempo, tamaños)
