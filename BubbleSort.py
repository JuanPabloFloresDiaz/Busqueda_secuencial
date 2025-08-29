def bubble_sort(lista, key=lambda x: x, reverse=False):
    """
    Ordena la lista utilizando el método de la burbuja.

    Parámetros:
      - lista: Lista de datos a ordenar.
      - key: Función para identificar el criterio de comparación.
      - reverse: Define su orden si es True, ordena en orden descendente.

    Retorna la lista ordenada.
    """
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Esta condición determina si se deben intercambiar los elementos lista[j] y lista[j+1].
            if (
                # Orden ascendente (reverse es False)
                # Comparamos el valor de lista[j] con el de lista[j+1] usando la función key.
                # Si el valor de lista[j] es mayor que el de lista[j+1], y no estamos ordenando en reversa,
                # entonces los elementos están en el orden incorrecto para un orden ascendente.
                key(lista[j]) > key(lista[j + 1]) and not reverse
            ) or (
                # Orden descendente (reverse es True)
                # Comparamos el valor de lista[j] con el de lista[j+1] usando la función key.
                # Si el valor de lista[j] es menor que el de lista[j+1], y estamos ordenando en reversa,
                # entonces los elementos están en el orden incorrecto para un orden descendente.
                key(lista[j]) < key(lista[j + 1]) and reverse
            ):
                # Si la condición del if es verdadera, significa que los elementos
                # deben ser intercambiados para avanzar hacia el ordenamiento correcto.
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista