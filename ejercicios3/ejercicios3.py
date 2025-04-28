# Ejercicios 3 - Modelado y Programacion
# Alfredo B

# EJERCICIO 1: 
# Busca los ceros y pone en cero su fila y columna
# Complejidad: O(m * n)

def poner_ceros(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    zero_rows = set()
    zero_cols = set()

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)

    for i in range(rows):
        for j in range(cols):
            if i in zero_rows or j in zero_cols:
                matrix[i][j] = 0
    return matrix

# EJERCICIO 2:
# Une los intervalos que se empalman
# Complejidad: O(n log n)

def unir_intervalos(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    res = [intervals[0]]
    for start, end in intervals[1:]:
        last_end = res[-1][1]
        if start <= last_end:
            res[-1][1] = max(last_end, end)
        else:
            res.append([start, end])
    return res

# EJERCICIO 3:
# Usa dos punteros para ver si hay ciclo
# Complejidad: O(n)

class NodoLigado:
    def __init__(self, valor=0, siguiente=None):
        self.valor = valor
        self.siguiente = siguiente

def detectar_ciclo(head):
    visitados = set()
    actual = head
    while actual:
        if actual in visitados:
            return True
        visitados.add(actual)
        actual = actual.siguiente
    return False

# EJERCICIO 4:
# Usa XOR para encontrar el que esta solo
# Complejidad: O(n)

def numero_unico(nums):
    conteo = {}
    for num in nums:
        if num in conteo:
            conteo[num] += 1
        else:
            conteo[num] = 1
    for num, veces in conteo.items():
        if veces == 1:
            return num

# -------------------------------
# PRUEBAS UNITARIAS

def prueba_poner_ceros():
    matriz = [[1,1,1],[1,0,1],[1,1,1]]
    assert poner_ceros(matriz) == [[1,0,1],[0,0,0],[1,0,1]]
    matriz = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    assert poner_ceros(matriz) == [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

def prueba_unir_intervalos():
    assert unir_intervalos([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
    assert unir_intervalos([[1,4],[5,6]]) == [[1,4],[5,6]]

def prueba_detectar_ciclo():
    nodo1 = NodoLigado(3)
    nodo2 = NodoLigado(2)
    nodo3 = NodoLigado(0)
    nodo4 = NodoLigado(-4)
    nodo1.siguiente = nodo2
    nodo2.siguiente = nodo3
    nodo3.siguiente = nodo4
    nodo4.siguiente = nodo2
    assert detectar_ciclo(nodo1) == True

    nodo5 = NodoLigado(1)
    nodo6 = NodoLigado(2)
    nodo5.siguiente = nodo6
    assert detectar_ciclo(nodo5) == False

def prueba_numero_unico():
    assert numero_unico([2,2,1]) == 1
    assert numero_unico([4,1,2,1,2]) == 4

if __name__ == "__main__":
    prueba_poner_ceros()
    prueba_unir_intervalos()
    prueba_detectar_ciclo()
    prueba_numero_unico()
    print("Todas las pruebas pasaron yupi")
