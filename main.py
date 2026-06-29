"""
tarea programada 2: agencia de seguridad del reino
universidad lead

programa principal con menu interactivo.

problema 1: vigilancia del castillo (n-reinas)
problema 2: gestion de recursos del reino (suma de subconjuntos)

ambos problemas se resuelven utilizando la tecnica de backtracking,
implementada manualmente sin librerias externas.
"""

from n_reinas import ejecutar_n_reinas
from subconjuntos import ejecutar_subconjuntos


def mostrar_menu():
    print("\n========================================")
    print(" agencia de seguridad del reino - hyrule")
    print("========================================")
    print("1. vigilancia del castillo (n-reinas)")
    print("2. gestion de recursos del reino (subconjuntos)")
    print("3. salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("seleccione una opcion: ").strip()

        if opcion == "1":
            ejecutar_n_reinas()
        elif opcion == "2":
            ejecutar_subconjuntos()
        elif opcion == "3":
            print("\nsaliendo del programa. hasta la proxima, guardia real!")
            break
        else:
            print("\nopcion invalida. por favor seleccione 1, 2 o 3.")


if __name__ == "__main__":
    main()
