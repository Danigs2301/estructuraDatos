def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # Inicializar el tamaño del intervalo (gap)

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp

        gap //= 2  # Reducir el tamaño del intervalo a la mitad