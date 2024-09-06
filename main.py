import matplotlib.pyplot as plt
from matplotlib_venn import venn2_unweighted, venn3_unweighted
from upsetplot import plot as upsetplot
from upsetplot import from_memberships
import pandas as pd





#Metodo encargado de leer n cantidad de conjuntos los cuales van a ser procesados
def obtener_conjuntos():

    n = int(input("Ingrese la cantidad de conjuntos: "))

    conjuntos = {}
    for i in range(n):
        nombre = chr(65 + i)
        elementos = input("Ingrese los elementos del conjunto {nombre} separados por espacios: ").split()
        conjuntos[nombre] = set(elementos)
    return conjuntos






#Metodo encargado de unir los elementos de la lista de conjuntos recorriendo uno a uno 
#los elementos de la cantidad de conjuntos que existen
def unir_conjuntos(conjuntos):
    union = set()
    for conjunto in conjuntos.values():
        for elemento in conjunto:
            union.add(elemento)
    return union






#Metodo encargado de realizar la interseccion de los conjuntos tomando como base el primer conjunto
def interseccion(conjuntos):

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







#Metodo que haya la diferencia del primer conjunto con respecto a todos los demas realizando una resta entre listas 
def diferencia(conjuntos):
  
    # Inicializamos la diferencia con el primer conjunto
    diferencia = set(list(conjuntos.values())[0])
    
    # Iteramos sobre los demás conjuntos y los restamos del primero
    for conjunto in list(conjuntos.values())[1:]:
        diferencia -= conjunto
    
    return diferencia
    






#Metodo encargado de encontrar la diferencia simetrica entre todos los conjuntos
def dif_simetrica(conjuntos):

    # Inicializamos la diferencia simétrica con el primer conjunto
    resultado = set(list(conjuntos.values())[0])
    
    # Iteramos sobre los demás conjuntos y aplicamos la diferencia simétrica 
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







#Metodo quie encuentra todos los subconjuntos del primer conjunto
def subconjuntos(conjuntos):
    # Obtener el primer conjunto del diccionario
    primer_conjunto = list(conjuntos.values())[0]
    
    subconjuntos_encontrados = []

    # Iteramos sobre los conjuntos a partir de la segunda posición 
    for conjunto in list(conjuntos.values())[1:]:
        es_subconjunto = True  #
        
        # Verificamos manualmente si todos los elementos de 'conjunto' están en 'primer_conjunto'
        for elemento in conjunto:
            if elemento not in primer_conjunto:
                es_subconjunto = False  
                break
        
        # Si el conjunto actual es subconjunto del primero, lo agregamos a la lista
        if es_subconjunto:
            subconjuntos_encontrados.append(conjunto)
    
    return subconjuntos_encontrados




#Metodo que encuentra todos los superconjuntos del primer conjunto
def superconjuntos(conjuntos):
    # Obtener el primer conjunto del diccionario
    primer_conjunto = list(conjuntos.values())[0]
    
    superconjuntos_encontrados = []

    # Iteramos sobre los conjuntos a partir de la segunda posición (omitir el primero)
    for conjunto in list(conjuntos.values())[1:]:
        es_superconjunto = True  
        
        # Verificamos manualmente si todos los elementos de 'primer_conjunto' están en 'conjunto'
        for elemento in primer_conjunto:
            if elemento not in conjunto:
                es_superconjunto = False  
                break
        
        # Si el conjunto actual es superconjunto del primero, lo agregamos a la lista
        if es_superconjunto:
            superconjuntos_encontrados.append(conjunto)
    
    return superconjuntos_encontrados







# Llamado de metodos
conjuntos = obtener_conjuntos()  # Permite al usuario ingresar los conjuntos

union = unir_conjuntos(conjuntos)  # Obtiene la unión de todos los conjuntos

interseccion = interseccion(conjuntos)  # Obtiene la intersección de todos los conjuntos

diferencia_resultado = diferencia(conjuntos)  # Obtiene la diferencia entre el primer conjunto y los demás

diferencia_simetrica_resultado = dif_simetrica(conjuntos)  # Obtiene la diferencia simétrica entre los conjuntos

subconjuntos_resultado = subconjuntos(conjuntos)  # Obtiene los subconjuntos del primer conjunto

superconjuntos_resultado = superconjuntos(conjuntos)  # Obtiene los superconjuntos del primer conjunto



def visualizar_conjuntos(conjuntos): # Genera el diagrama de Venn de los conjuntos
    n = len(conjuntos)
    if n == 2:
        set1, set2 = conjuntos['A'], conjuntos['B']
        v = venn2_unweighted(subsets=(set1, set2), set_labels=('A', 'B'))

        # Personalizar las etiquetas
        v.get_label_by_id('10').set_text('\n'.join(set1 - set2))
        v.get_label_by_id('01').set_text('\n'.join(set2 - set1))
        v.get_label_by_id('11').set_text('\n'.join(set1 & set2))

    elif n == 3:
        set1, set2, set3 = conjuntos['A'], conjuntos['B'], conjuntos['C']
        v = venn3_unweighted(subsets=(set1, set2, set3), set_labels=('A', 'B', 'C'))

        v.get_label_by_id('100').set_text('\n'.join(set1 - set2 - set3))
        v.get_label_by_id('010').set_text('\n'.join(set2 - set1 - set3))
        v.get_label_by_id('001').set_text('\n'.join(set3 - set1 - set2))
        v.get_label_by_id('110').set_text('\n'.join(set1 & set2 - set3))
        v.get_label_by_id('101').set_text('\n'.join(set1 & set3 - set2))
        v.get_label_by_id('011').set_text('\n'.join(set2 & set3 - set1))
        v.get_label_by_id('111').set_text('\n'.join(set1 & set2 & set3))

    else:
        print("La visualización solo está disponible para 2 o 3 conjuntos.")
        return

    plt.title("Diagrama de Venn de los conjuntos")
    plt.show()



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

visualizar_conjuntos(conjuntos) # Muestra el diagrama de Venn de los conjuntos