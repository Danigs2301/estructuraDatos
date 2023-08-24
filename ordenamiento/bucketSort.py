def bucket_sort(arr):
    if len(arr) == 0:
        return []

    # Encontrar el valor máximo y mínimo en el arreglo
    max_value = max(arr)
    min_value = min(arr)
    
    # Calcular el rango de cada bucket
    bucket_range = (max_value - min_value) / len(arr)
    
    # Crear los buckets
    num_buckets = len(arr)
    buckets = [[] for _ in range(num_buckets)]
    
    # Colocar elementos en los buckets correspondientes
    for num in arr:
        index = int((num - min_value) / bucket_range)
        buckets[index].append(num)
    
    # Ordenar cada bucket y combinar los resultados
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))
    
    return sorted_arr