# Ejercicios 1 - Modelado y Programación

En este repo vienen las soluciones a los ejercicios 1.

## Cómo ejecutar las pruebas unitarias

Para ejecutar con pruebas unitarias

```bash
python ejercicios1.py
```

##  Cómo ejecutar cada ejercicio individualmente

Para probar cada ajercicio sin las pruebas es asi:

### En una terminal 

```bash
python
```

## Importamos las funciones para probarlas:
```bash
from ejercicios1 import encontrar_numeros, prefijo_comun, romano_a_entero, entero_a_romano
```
## Luego se puede ejecutar cada ejercicio con sus respectivos parametros:
```bash
matriz = [[5, 3], [4, 5]]
print(encontrar_numeros(matriz))
```

```bash
cadenas = ["programa", "progreso", "proyecto"]
print(prefijo_comun(cadenas)) 
```
```bash
print(romano_a_entero("XIII")) 
```
```bash
print(entero_a_romano(77))  
```

#### Importante
Toda la implementacion la hice desde Windows, las intrucciones las hice basado en eso