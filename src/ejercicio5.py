"""
Ejercicio 2.5
Escribe un programa que pida el importe sin IVA de un artículo y el tipo de IVA a aplicar y calcule e imprima por pantalla el precio final del artículo.
"""
importe_base = float(input("Escribe el importe sin IVA : "))
iva = int(input("Qué porcentaje de IVA se va a aplicar : "))
iva_aplicado = importe_base*iva/100
importe_final = iva_aplicado + importe_base
print(f"El importe total es : {importe_final} euros")
