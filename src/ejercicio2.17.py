"""
Ejercicio 2.17¶
Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e
imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
"""
nombre = input("Escribe tu nombre de usuario : ")
numero = int(input("Escribe un número : "))
while numero > 0:
    print(f"{nombre}")
    numero -= 1
