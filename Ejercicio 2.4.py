"""
Ejercicio 2.4¶
Escribe un programa que le pida al usuario una temperatura en grados Celsius, la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida.
"""
temperatura_celsius = float(input("Escribe una temperatura en grados celsius : "))
fahrenheit = (temperatura_celsius*9/5)+32
print(f"{temperatura_celsius}º son {fahrenheit}Fº")
