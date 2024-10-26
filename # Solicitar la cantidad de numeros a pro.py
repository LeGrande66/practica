# Solicitar la cantidad de numeros a promediar
Cantidad = int(input("¿cuantos numeros quieres promediar?"))
# Crea una lista para almacenar numeros
numeros = []
# Pedir al usuario que ingrese los numeros
for i in range(cantidad):
    num = float(input(f"ingresas numero {i + 1}:"))
    numeros.append(num)
# Calcular promedio
promedio = sum(numeros) / Cantidad
print(f"El promedio de los numeros ingresados es: {promedio}")
