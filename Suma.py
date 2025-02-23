def suma_recursiva(arr, n):
    if n == 0:
        return 0
    return arr[n - 1] + suma_recursiva(arr, n - 1)
arreglo = [1, 2, 3, 4, 5]
resultado = suma_recursiva(arreglo, len(arreglo))
print("La suma es:", resultado)