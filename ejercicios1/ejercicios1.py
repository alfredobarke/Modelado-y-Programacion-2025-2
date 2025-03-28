import unittest

def encontrar_numeros(matriz):
    """
    Encuentra el número repetido y el número faltante en la matriz.

    Complejidad: O(n^2)  
    - Se recorren todos los elementos de la matriz (O(n^2)).
    - Se usa un conjunto para verificar duplicados (O(1) por inserción).
    """
    n = len(matriz)
    numeros = set(range(1, n * n + 1))
    vistos = set()
    repetido = None
    
    for fila in matriz:
        for num in fila:
            if num in vistos:
                repetido = num
            vistos.add(num)
    
    faltante = list(numeros - vistos)[0]
    return repetido, faltante

def prefijo_comun(cadenas):
    """
    Encuentra el prefijo común más largo.

    Complejidad: O(m*n)  
    - m: Longitud de la cadena más corta.
    - n: Número de cadenas.
    - Se compara cada cadena con el prefijo (O(m*n) en el peor caso).
    """
    if not cadenas:
        return ""
    
    prefijo = cadenas[0]
    for palabra in cadenas[1:]:
        while not palabra.startswith(prefijo):
            prefijo = prefijo[:-1]
            if not prefijo:
                return ""
    return prefijo

valores_romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def romano_a_entero(romano):
    """
    Convierte un número romano a entero.

    Complejidad: O(n)  
    - Se recorre la cadena una vez, verificando valores y sumando/restando.
    """
    total = 0
    previo = 0
    for letra in romano[::-1]:
        actual = valores_romanos[letra]
        if actual < previo:
            total -= actual
        else:
            total += actual
        previo = actual
    return total

def entero_a_romano(numero):
    """
    Convierte un número entero a su representación en números romanos.

    Complejidad: O(log n)  
    - Se usan valores decrecientes en potencias de 10, reduciendo el número en cada paso.
    """
    valores = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    resultado = ""
    for valor, simbolo in valores:
        while numero >= valor:
            resultado += simbolo
            numero -= valor
    return resultado

class TestEjercicios1(unittest.TestCase):
    def test_encontrar_numeros(self):
        self.assertEqual(encontrar_numeros([[1, 3], [2, 2]]), (2, 4))
        self.assertEqual(encontrar_numeros([[9, 1, 7], [8, 9, 2], [3, 4, 6]]), (9, 5))
    
    def test_prefijo_comun(self):
        self.assertEqual(prefijo_comun(["flor", "flores", "floreria"]), "flor")
        self.assertEqual(prefijo_comun(["flor", "flores", "vape"]), "")
    
    def test_romano_a_entero(self):
        self.assertEqual(romano_a_entero("III"), 3)
        self.assertEqual(romano_a_entero("LVIII"), 58)
        self.assertEqual(romano_a_entero("MCMXCIV"), 1994)
    
    def test_entero_a_romano(self):
        self.assertEqual(entero_a_romano(3749), "MMMDCCXLIX")
        self.assertEqual(entero_a_romano(58), "LVIII")

if __name__ == "__main__":
    unittest.main()
