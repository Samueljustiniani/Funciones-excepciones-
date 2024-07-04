#1 ZeroDivisionError: Ocurre cuando se intenta dividir por cero.
try:
    resultado = 10 / 2
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
#2 ValueError: Ocurre cuando una función recibe un argumento del tipo correcto pero con un valor inapropiado.
try:
    numero = int("abc")
except ValueError:
    print("Error: No se puede convertir 'abc' a un entero.")

#3 TypeError: Ocurre cuando se realiza una operación o función con un tipo de dato inapropiado.
try:
    resultado = '10' + 5
except TypeError:
    print("Error: No se puede sumar un string y un entero.")

#4 IndexError: Ocurre cuando se intenta acceder a un índice que no existe en una lista.
lista = [1, 2, 3]
try:
    elemento = lista[5]
except IndexError:
    print("Error: Índice fuera del rango de la lista.")

#5 KeyError: Ocurre cuando se intenta acceder a una clave que no existe en un diccionario.
diccionario = {"nombre": "Alice", "edad": 25}
try:
    valor = diccionario["apellido"]
except KeyError:
    print("Error: La clave 'apellido' no existe en el diccionario.")
