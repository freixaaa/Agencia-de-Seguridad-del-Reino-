"""
modulo: subconjuntos.py
problema 2 - gestion de recursos del reino (suma de subconjuntos)

determina que combinaciones de cargamentos de recursos suman
exactamente una cantidad objetivo, utilizando backtracking.
"""


def backtrack_subconjuntos(lista, objetivo, indice, suma_actual,
                            subconjunto_actual, soluciones):
    """
    funcion recursiva de backtracking. para cada elemento de la lista
    se decide si se incluye o no en el subconjunto que se esta construyendo.
    """
    # caso de exito: la suma actual coincide exactamente con el objetivo
    if suma_actual == objetivo:
        soluciones.append(subconjunto_actual.copy())
        return

    # poda: ya no quedan elementos por revisar, o la suma ya supero el objetivo
    if indice >= len(lista) or suma_actual > objetivo:
        return

    # opcion 1: incluir el elemento actual en el subconjunto
    subconjunto_actual.append(lista[indice])
    backtrack_subconjuntos(
        lista, objetivo, indice + 1,
        suma_actual + lista[indice],
        subconjunto_actual, soluciones
    )
    subconjunto_actual.pop()  # deshacer (backtrack)

    # opcion 2: no incluir el elemento actual
    backtrack_subconjuntos(
        lista, objetivo, indice + 1,
        suma_actual, subconjunto_actual, soluciones
    )


def resolver_subconjuntos(lista, objetivo):
    """
    punto de entrada para resolver el problema de suma de subconjuntos.

    retorna una lista con todos los subconjuntos cuya suma es exactamente
    igual al objetivo.
    """
    soluciones = []
    backtrack_subconjuntos(lista, objetivo, 0, 0, [], soluciones)
    return soluciones


def solicitar_lista_numeros():
    """
    solicita al usuario la lista de recursos disponibles, separados por
    comas o espacios, validando que todos los valores sean enteros.
    """
    while True:
        entrada = input(
            "ingrese los recursos disponibles separados por comas "
            "(ej. 3,4,5,7,10): "
        ).strip()

        partes = entrada.replace(",", " ").split()

        if not partes:
            print("error: debe ingresar al menos un numero.")
            continue

        try:
            numeros = [int(p) for p in partes]
            return numeros
        except ValueError:
            print("error: todos los valores deben ser numeros enteros.")


def solicitar_objetivo():
    """
    solicita al usuario la suma objetivo, validando que sea un entero.
    """
    while True:
        entrada = input("ingrese la suma objetivo: ").strip()
        try:
            return int(entrada)
        except ValueError:
            print("error: la suma objetivo debe ser un numero entero.")


def ejecutar_subconjuntos():
    """
    flujo completo del problema 2: solicita la lista de recursos y el
    objetivo, resuelve el problema con backtracking y muestra los
    resultados.
    """
    lista = solicitar_lista_numeros()
    objetivo = solicitar_objetivo()

    soluciones = resolver_subconjuntos(lista, objetivo)

    print("\n--- gestion de recursos del reino ---")
    print(f"recursos disponibles: {lista}")
    print(f"objetivo: {objetivo}\n")

    if len(soluciones) == 0:
        print("no existe ninguna combinacion de recursos que sume el objetivo.")
    else:
        print("subconjuntos encontrados:\n")
        for subconjunto in soluciones:
            print(subconjunto)

    print(f"\ncantidad total de soluciones encontradas: {len(soluciones)}")
