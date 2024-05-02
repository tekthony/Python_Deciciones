# DECICIONES

En Python, las decisiones se basan en evaluar expresiones como verdaderas o falsas y tomar decisiones en consecuencia. Las estructuras de control de flujo como if, elif, y else permiten dirigir el flujo del programa según estas condiciones.

1.-Usando `if`, `elif`, y `else` para tomar decisiones múltiples:

``` PYTHON
x = 10

if x > 10:
    print("x es mayor que 10.")
elif x == 10:
    print("x es igual a 10.")
else:
    print("x es menor que 10.") 
```

2.-Decisión basada en la pertenencia a una lista:

``` PYTHON
frutas = ['manzana', 'banana', 'cereza']

if 'manzana' in frutas:
    print("Sí, tenemos manzanas.")
else:
    print("No, no tenemos manzanas.")
```

3.-Uso de operadores lógicos para combinar condiciones:

``` PYTHON
edad = 25
ciudad = "Nueva York"

if edad >= 18 and ciudad == "Nueva York":
    print("¡Eres mayor de edad y vives en Nueva York!")
else:
    print("No cumples con los requisitos.")
```

4.-Decisión anidada para casos más complejos:

``` PYTHON
puntuacion = 75

if puntuacion >= 90:
    print("A")
elif puntuacion >= 80:
    print("B")
elif puntuacion >= 70:
    print("C")
elif puntuacion >= 60:
    print("D")
else:
    print("F")
```

5.-Uso de operador ternario para decisiones simples:

``` PYTHON
x = 5
resultado = "positivo" if x > 0 else "negativo o cero"
print("El número es", resultado)
```


