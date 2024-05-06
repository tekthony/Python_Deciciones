# EJERCICIOS PRACTICOS.

## 1.- Escribe un programa que solicite al usuario dos números y luego imprima cuál de los dos es mayor, o si son iguales.

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

if num1 > num2:
    print("El primer número es mayor.")
elif num2 > num1:
    print("El segundo número es mayor.")
else:
    print("Los dos números son iguales.")

## 2.- Crea un programa que solicite al usuario un número e imprima si es positivo, negativo o cero.

num = float(input("Ingrese un número: "))

if num > 0:
    print("El número es positivo.")
elif num < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")
    
## 3.- Desarrolla un programa que tome un número del usuario e imprima si es par o impar.

num = int(input("Ingrese un número: "))

if num % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")
    
## 4.- Crea un programa que realice una operación básica de suma, resta, multiplicación o división según la elección del usuario.

print("Operaciones disponibles:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion = int(input("Seleccione la operación (1/2/3/4): "))
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

if opcion == 1:
    resultado = num1 + num2
    print("El resultado de la suma es:", resultado)
elif opcion == 2:
    resultado = num1 - num2
    print("El resultado de la resta es:", resultado)
elif opcion == 3:
    resultado = num1 * num2
    print("El resultado de la multiplicación es:", resultado)
elif opcion == 4:
    if num2 == 0:
        print("No se puede dividir por cero.")
    else:
        resultado = num1 / num2
        print("El resultado de la división es:", resultado)
else:
    print("Opción inválida.")
    
## 5.- Escribe un programa que determine si un año ingresado por el usuario es un año bisiesto o no.

año = int(input("Ingrese un año: "))

if (año % 4 == 0 and año % 100 != 0) or año % 400 == 0:
    print("El año", año, "es bisiesto.")
else:
    print("El año", año, "no es bisiesto.")