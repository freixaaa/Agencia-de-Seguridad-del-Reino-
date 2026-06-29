"""
modulo: n_reinas.py
problema 1 - vigilancia del castillo (n-reinas)

resuelve el problema de las n-reinas utilizando backtracking.
cada "guardia" (reina) vigila su fila, columna y diagonales,
por lo que no puede haber dos guardias que se observen entre si.
"""


def es_posicion_valida(columnas_reinas, fila, columna):
    """
    verifica si es seguro colocar un guardia en (fila, columna),
    dado que los guardias en filas anteriores ya estan ubicados.
    """
    for fila_anterior in range(fila):
        columna_anterior = columnas_reinas[fila_anterior]

        # misma columna -> se vigilan entre si
        if columna_anterior == columna:
            return False

        # misma diagonal (principal o secundaria)
        if abs(columna_anterior - columna) == abs(fila_anterior - fila):
            return False

    return True


def backtrack_n_reinas(columnas_reinas, fila, n, soluciones):
    """
    funcion recursiva de backtracking. intenta ubicar un guardia
    en cada fila del tablero, una fila a la vez.

    columnas_reinas[i] = columna donde esta el guardia de la fila i.
    """
    # caso base: se colocaron guardias validos en todas las filas
    if fila == n:
        soluciones.append(columnas_reinas.copy())
        return

    for columna in range(n):
        if es_posicion_valida(columnas_reinas, fila, columna):
            columnas_reinas[fila] = columna            # probar
            backtrack_n_reinas(columnas_reinas, fila + 1, n, soluciones)
            columnas_reinas[fila] = -1                  # deshacer (backtrack)


def resolver_n_reinas(n):
    """
    punto de entrada para resolver el problema de las n-reinas.

    retorna una lista con todas las soluciones encontradas. cada solucion
    es una lista donde el indice representa la fila y el valor la columna
    en la que se ubica el guardia.
    """
    soluciones = []
    columnas_reinas = [-1] * n
    backtrack_n_reinas(columnas_reinas, 0, n, soluciones)
    return soluciones


def imprimir_tablero(solucion, n):
    """
    representa visualmente una solucion del tablero n x n.
    q = guardia
    . = casilla vacia
    """
    for fila in range(n):
        casillas = []
        for columna in range(n):
            if solucion[fila] == columna:
                casillas.append("Q")
            else:
                casillas.append(".")
        print(" ".join(casillas))


def solicitar_tamano_tablero():
    """
    solicita al usuario el tamano n del tablero, validando que sea
    un entero positivo.
    """
    while True:
        entrada = input("ingrese el tamano del tablero (n): ").strip()

        if not entrada.isdigit():
            print("error: debe ingresar un numero entero positivo.")
            continue

        n = int(entrada)

        if n <= 0:
            print("error: n debe ser mayor que 0.")
            continue

        if n > 12:
            confirmacion = input(
                f"n = {n} puede tardar bastante en calcular todas las "
                "soluciones. desea continuar? (s/n): "
            ).strip().lower()
            if confirmacion != "s":
                continue

        return n


def ejecutar_n_reinas():
    """
    flujo completo del problema 1: solicita el tamano del tablero,
    resuelve el problema con backtracking y muestra los resultados.
    """
    n = solicitar_tamano_tablero()
    soluciones = resolver_n_reinas(n)

    print(f"\n--- vigilancia del castillo (n = {n}) ---\n")

    if len(soluciones) == 0:
        print("no existe ninguna solucion valida para este tamano de tablero.")
    else:
        print("una solucion valida encontrada:\n")
        imprimir_tablero(soluciones[0], n)

    print(f"\ncantidad total de soluciones encontradas: {len(soluciones)}")
