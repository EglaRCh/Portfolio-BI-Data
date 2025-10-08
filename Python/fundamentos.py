# Práctica: Promedio de notas
notas = [7.5, 8.0, 9.0, 6.5, 10]

#Calcular promedio
suma = 0
for nota in notas:
    suma += nota

promedio = suma / len(notas)
print(f"El promedio de las notas es: {promedio}")

#Filtrar notas mayores a 8
notas_altas = []
for nota in notas:
    if nota > 8:
        notas_altas.append(nota)

print(f"Notas mayores a 8:{notas_altas}")

"""
--> Promedio de notas
notas = [...] : se declara una lista [] que contiene valores numéricos (float type)

suma = 0 : variable acumuladora
for nota un notas: recorre la lista elemento por elemento
suma += nota : va sumando cada valor
len(notas) : devuelve cuántos elementos hay en la lista ~longitud
prometio = suma / len(notas) : divide la suma total entre la cantidad de notas y lo asigna a la variable 'promedio

Se imprime el resultado usando f-strings (formato dinámico en cadenas)

--> Filtrado de valores
notas_altas = [] : crea una lista vacia para guardar las notas filtradas asignada a la varianble 'notas_altas
if nota > 8 : es la condicion que selecciona solo los valores identificados como nota > 8
append (nota) : agrega esos valores a la listafiltrada 


También se puede simplificar con list comprehension 
    notas_altas = [n for n in notas if n > 8] 
    --> la variable notas_altas es una lista de un bucle (for) en cada elemento n en la lista de notas si el elemento n es mayor a 8

"""
#Condicionales

print ("-----Ejercicio Condicionales if/else-------")
edades = [12, 17, 25, 34, 15 ,25]

for edad in edades:
    if edad < 18:
        print(f"{edad} años: Menor de edad")
    elif 18 >= edad <= 65:
        print(f"{edad} años: Adulto")
    else:
        print(f"{edad} años: Adulto mayor")

#Bucles

print("------Ejercicio Bucles for/while")
precios = [150,75,200,50,120]

print("USando for:")
for precio in precios:
    if precio > 100:
        print(precio)
    
print("Usando while")
i = 0
while i < len(precios):
    if precios[i] > 100:
        print(precios[i])
    i += 1

#Funciones

print("----Ejercicio Funciones con parámetros y retorno")

def min_max(lista):
    minimo = min(lista)
    maximo = max(lista)
    return minimo, maximo

test = [1,5,9,11,4]
minimo, maximo = min_max(test)
print(f"Mínimo: {minimo} \nMáximo: {maximo}")


