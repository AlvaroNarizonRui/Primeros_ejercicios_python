"""
Ejercicio 2.2
Escribe un programa para pedirle al usuario las horas de trabajo y el precio por hora y calcule el importe total del servicio.
"""
def calcularImporte(horas,precio) -> float:
    importe = horas * precio
    return importe

#Entrada
horas = int(input("Escribe las horas de trabajo : "))
precio = int(input("Escribe el precio por hora de trabajo : "))
#Procesamiento
importe = calcularImporte(horas,precio)
#Salida
print(f"Tu importe total por el servicio es de {importe} euros")