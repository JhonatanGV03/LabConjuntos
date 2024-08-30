
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
    if not conjuntos:
        return set()
    
    # Inicializamos la diferencia con el primer conjunto
    diferencia = set(list(conjuntos.values())[0])
    
    # Iteramos sobre los demás conjuntos y los restamos del primero
    for conjunto in list(conjuntos.values())[1:]:
        diferencia -= conjunto
    
    return diferencia
    

def dif_simetrica():
    if not conjuntos:
        return set()
    
    # Inicializamos la diferencia simétrica con el primer conjunto
    resultado = set(list(conjuntos.values())[0])
    
    # Iteramos sobre los demás conjuntos y aplicamos la diferencia simétrica manualmente
    for conjunto in list(conjuntos.values())[1:]:
        nueva_dif_sim = set()
        # Elementos en 'resultado' pero no en 'conjunto'
        for elemento in resultado:
            if elemento not in conjunto:
                nueva_dif_sim.add(elemento)
        # Elementos en 'conjunto' pero no en 'resultado'
        for elemento in conjunto:
            if elemento not in resultado:
                nueva_dif_sim.add(elemento)
        # Actualizamos el resultado con la nueva diferencia simétrica
        resultado = nueva_dif_sim
    
    return resultado


def subconjuntos():
    print("hello world")


def superconjuntos():
    print("hello world")


# Llamado de metodos
conjuntos = obtener_conjuntos()  # Permite al usuario ingresar los conjuntos

union = unir_conjuntos(conjuntos)  # Obtiene la unión de todos los conjuntos

interseccion = interseccion()  # Obtiene la intersección de todos los conjuntos

diferencia_resultado = diferencia()  # Obtiene la diferencia entre el primer conjunto y los demás

diferencia_simetrica_resultado = dif_simetrica()  # Obtiene la diferencia simétrica entre los conjuntos



# Imprimir conjuntos ingresados y operados
print("\nConjuntos ingresados:")
for nombre, conjunto in conjuntos.items():  # Muestra los conjuntos ingresados
    print(f"{nombre}: {conjunto}")


print("\nUnión de todos los conjuntos:")
print(union)  # Muestra la unión de todos los conjuntos

print("\nIntersección de todos los conjuntos:")
print(interseccion)  # Muestra la intersección de todos los conjuntos

print("\nDiferencia entre el primer conjunto y los demás:")
print(diferencia_resultado)  # Muestra la diferencia entre el primer conjunto y los demás

print("\nDiferencia simétrica de todos los conjuntos:")
print(diferencia_simetrica_resultado)  # Muestra la diferencia simétrica de todos los conjuntos