
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





def subconjuntos(conjuntos):
    if not conjuntos:
        return []

    primer_conjunto = list(conjuntos.values())[0]
    subconjuntos_encontrados = []

    # Iteramos sobre todos los conjuntos para encontrar los subconjuntos del primer conjunto
    for conjunto in conjuntos.values():
        if conjunto.issubset(primer_conjunto):
            subconjuntos_encontrados.append(conjunto)
    
    return subconjuntos_encontrados





def superconjuntos(conjuntos):
    if not conjuntos:
        return []

    primer_conjunto = list(conjuntos.values())[0]
    superconjuntos_encontrados = []

    # Iteramos sobre todos los conjuntos para encontrar los superconjuntos del primer conjunto
    for conjunto in conjuntos.values():
        if conjunto.issuperset(primer_conjunto):
            superconjuntos_encontrados.append(conjunto)
    
    return superconjuntos_encontrados


# Llamado de metodos
conjuntos = obtener_conjuntos()  # Permite al usuario ingresar los conjuntos

union = unir_conjuntos(conjuntos)  # Obtiene la unión de todos los conjuntos

interseccion = interseccion()  # Obtiene la intersección de todos los conjuntos

diferencia_resultado = diferencia()  # Obtiene la diferencia entre el primer conjunto y los demás

diferencia_simetrica_resultado = dif_simetrica()  # Obtiene la diferencia simétrica entre los conjuntos

subconjuntos_resultado = subconjuntos(conjuntos)  # Obtiene los subconjuntos del primer conjunto

superconjuntos_resultado = superconjuntos(conjuntos)  # Obtiene los superconjuntos del primer conjunto




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

print("\nSubconjuntos del primer conjunto:")
print(subconjuntos_resultado)  # Muestra los subconjuntos del primer conjunto

print("\nSuperconjuntos del primer conjunto:")
print(superconjuntos_resultado)  # Muestra los superconjuntos del primer conjunto