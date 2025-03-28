# ejercicios 2 - modelado y programacion
from collections import Counter

# checa si nota se puede armar con texto
def puede_generar_nota(nota: str, texto: str) -> bool:
    cuenta_texto = Counter(texto)
    cuenta_nota = Counter(nota)
    for letra in cuenta_nota:
        if cuenta_nota[letra] > cuenta_texto.get(letra, 0):
            return False
    return True

# checa si hay duplicados cercanos
def duplicado_cercano(arr, k):
    vistos = set()
    for i in range(len(arr)):
        if arr[i] in vistos:
            return True
        vistos.add(arr[i])
        if len(vistos) > k:
            vistos.remove(arr[i - k])
    return False

# checa si un num es feliz
def es_feliz(n):
    visitados = set()
    def suma_cuadrados(num):
        return sum(int(d)**2 for d in str(num))
    while n != 1 and n not in visitados:
        visitados.add(n)
        n = suma_cuadrados(n)
    return n == 1

# busca s en t 
def encontrar_subcadena(s: str, t: str) -> int:
    for i in range(len(t) - len(s) + 1):
        coincide = True
        for j in range(len(s)):
            if t[i + j] != s[j]:
                coincide = False
                break
        if coincide:
            return i
    return -1

# Pruebas Unitarias 
def pruebas_unitarias():
    assert puede_generar_nota('aa', 'ab') == False
    assert puede_generar_nota('aa', 'aba') == True
    assert duplicado_cercano([1, 2, 3, 1], 3) == True
    assert duplicado_cercano([1, 2, 3, 1, 2, 3], 2) == False
    assert es_feliz(19) == True
    assert es_feliz(2) == False
    assert encontrar_subcadena("tristes", "trestristestigrestragabantrigoenuntrigal") == 4
    assert encontrar_subcadena("tigresa", "trestristestigrestragabantrigoenuntrigal") == -1
    print("Todo ok en pruebas")

# Ejemplos 
if __name__ == '__main__':
    pruebas_unitarias()
    print("\nejemplos de ejecucion visual:")
    
    # Ejercicio 1
    print("\nejercicio 1:")
    print(puede_generar_nota('aa', 'ab'))   
    print(puede_generar_nota('aa', 'aba'))

    # Ejercicio 2
    print("\nejercicio 2:")
    print(duplicado_cercano([1, 2, 3, 1], 3)) 
    print(duplicado_cercano([1, 2, 3, 1, 2, 3], 2)) 

    # Ejercicio 3
    print("\nejercicio 3:")
    print(es_feliz(19))  
    print(es_feliz(2))   

    # Ejercicio 4
    print("\nejercicio 4:")
    print(encontrar_subcadena("tristes", "trestristestigrestragabantrigoenuntrigal"))  
    print(encontrar_subcadena("tigresa", "trestristestigrestragabantrigoenuntrigal"))  