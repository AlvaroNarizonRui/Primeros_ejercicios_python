"""
Ejercicio 2.6
Escribe un programa que pida el importe final de un artículo y calcule e imprima por pantalla el IVA que se ha pagado y 
el importe sin IVA (suponiendo que se ha aplicado un tipo de IVA del 10%).
"""
importe_final = float(input("Escribe el importe final de un artículo : "))
iva = importe_final*10/100
importe_base = importe_final - iva
print(f"El importe sin IVA de tu artículo son  {importe_base} euros")