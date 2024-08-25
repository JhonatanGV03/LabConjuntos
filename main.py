
def obtener_conjuntos():
    n = int(input("Ingrese la cantidad de conjuntos: "))
    conjuntos = {}
    for i in range(n):
        nombre = chr(65 + i)
        elementos = input(f"Ingrese los elementos del conjunto {nombre} separados por espacios: ").split()
        conjuntos[nombre] = set(elementos)
    return conjuntos


def unir_conjuntos(conjuntos):
    union = set()
    for conjunto in conjuntos.values():
        for elemento in conjunto:
            union.add(elemento)
    return union


def interseccion():
    if not conjuntos:
        return set()

    # Inicializamos la intersección con el primer conjunto
    interseccion = set(list(conjuntos.values())[0])

    # Iteramos sobre los demás conjuntos
    for conjunto in list(conjuntos.values())[1:]:
        nueva_interseccion = set()
        for elemento in interseccion:
            if elemento in conjunto:
                nueva_interseccion.add(elemento)
        interseccion = nueva_interseccion

    return interseccion


def diferencia():
    print("hello world")
    

def dif_simetrica():
    print("hello world")


def subconjuntos():
    print("hello world")


def superconjuntos():
    print("hello world")


# Llamado de metodos
conjuntos = obtener_conjuntos()  # Permite al usuario ingresar los conjuntos

union = unir_conjuntos(conjuntos)  # Obtiene la unión de todos los conjuntos

interseccion = interseccion()  # Obtiene la intersección de todos los conjuntos


# Imprimir conjuntos ingresados y operados
print("\nConjuntos ingresados:")
for nombre, conjunto in conjuntos.items():  # Muestra los conjuntos ingresados
    print(f"{nombre}: {conjunto}")

print("\nUnión de todos los conjuntos:")
print(union)  # Muestra la unión de todos los conjuntos

print("\nIntersección de todos los conjuntos:")
print(interseccion)  # Muestra la intersección de todos los conjuntos

