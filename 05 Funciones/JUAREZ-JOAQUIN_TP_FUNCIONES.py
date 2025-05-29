# 1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.

# def imprimir_hola_mundo():
#     return "Hola Mundo!"

# print(imprimir_hola_mundo())


# 2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario

# def saludar_usuario(nombre):
#     return f"Hola {nombre}!"

# nombre = input("Ingrese su nombre: ")

# print(saludar_usuario(nombre))


# 3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

# def informacion_personal(nombre,apellido,edad,residencia):
#     return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}"

# nombre = input("Ingrese su nombre: ")
# apellido = input("Ingrese su apellido: ")
# edad = input("Ingrese su edad: ")
# residencia = input("Ingrese donde reside: ")

# print(informacion_personal(nombre,apellido,edad,residencia))


# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

# from math import pi

# def calcular_area_circulo(radio):
#     return pi * (radio ** 2)

# def calcular_perimetro_circulo(radio):
#     return 2 * pi * radio

# radio = float(input("Ingrese el radio del circulo(en centimetros): "))
# area = calcular_area_circulo(radio)
# perimetro = calcular_perimetro_circulo(radio)

# print(f"El area del circulo es {area} cm2, mientras que su perimetro es de {perimetro} cm")


# 5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

# def segundos_a_horas(segundos):
#     return segundos / 3600 

# seg = int(input("Ingrese la cantidad de horas: "))

# print(f"{seg} segundos son {segundos_a_horas(seg)} horas")


# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.

# def tabla_multiplicar(numero):
#     lista_multiplos= []
#     for i in range(1,11):
#         multiplo = numero * i
#         lista_multiplos.append(multiplo)
#     return lista_multiplos

# num = int(input("Ingrese un numero entero: "))

# print(tabla_multiplicar(num))


# 7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

# def operaciones_basicas(a, b):
#     suma = (a + b)
#     resta = (a - b)
#     multiplicacion = (a * b)
#     division = (a / b)
#     return (suma, resta, multiplicacion, division)

# num1 = int(input("Ingrese un numero entero: "))
# num2 = int(input("Ingrese otro numero entero: "))

# print(operaciones_basicas(num1,num2))



# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

# def calcular_imc(peso, altura):
#     return peso / (altura ** 2)

# peso = float(input("Ingrese su peso en kilogramos "))
# altura = float(input("Ingrese su altura en metros "))

# print(calcular_imc(peso, altura))


# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

# def celsius_a_fahrenheit(celsius):
#     return (1.8 * celsius) + 32

# t = float(input("Ingrese la temperatura en Celsius"))

# print(celsius_a_fahrenheit(t))




# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando esta función.

# def calcular_promedio(a, b, c):
#     return (a + b + c)/3

# num1 = float(input("Ingrese un numero: "))
# num2 = float(input("Ingrese otro numero: "))
# num3 = float(input("Ingrese otro numero: "))

# print(calcular_promedio(num1, num2, num3))