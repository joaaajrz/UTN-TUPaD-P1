# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

# edad = int(input("Ingrese su edad: "))

# if edad >= 18:
#     print("Es mayor de edad")




# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.

# nota = float(input("Ingrese su nota: "))

# if nota >= 6:
#     print("Aprobado")
# else:
#     print("Desaprobado")




# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

# numero = int(input("Ingrese un numero par: "))

# if numero % 2 == 0:
#     print("Ha ingresado un número par")
# else:
#     print("Por favor, ingrese un número par")




# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años. 

# edad = int(input("Ingrese su edad: "))

# if edad < 12:
#     print("Usted pertenece a la categoria niño/a")
# elif edad >= 12 and edad < 18:
#     print("Usted pertenece a la categoria adolescente")
# elif edad >= 18 and edad < 30:
#     print("Usted pertenece a la categoria adulto/a joven")
# else:
#     print("Usted pertenece a la categoria adulto/a")




# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.

# password = input("Ingrese una contrseña: ")
# password_large = len(password)

# if 8 <= password_large <=14:
#     print("Ha ingresado una contraseña correcta")
# else:
#     print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")




# 6) El paquete statistics de python contiene funciones que permiten tomar una lista de números y calcular la moda, la mediana y la media de dichos números. Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

# from statistics import mode, median, mean
# import random
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# moda = mode(numeros_aleatorios)
# mediana = median(numeros_aleatorios)
# media = mean(numeros_aleatorios)

# if media < mediana and mediana > moda:
#     print("Hay sesgo positivo")
# elif media < mediana and mediana < moda:
#     print("Hay sesgo negativo")
# elif media == mediana == moda:
#     print("No hay sesgo")




# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

# VOCALES = ["a", "e", "i", "o", "u"]

# palabra = input("Ingrese una frase o palabra: ")
# uLetra = palabra[-1].lower()


# if uLetra in VOCALES:
#     print(f"{palabra}!")
# else:
#     print(palabra)




# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas.

# nombre = input("Ingrese su nombre: ")
# opcion = int(input("Seleccione 1, si quiere su nombre en mayúsculas. 2, si quiere su nombre en minúsculas. 3, si quiere su nombre con la primera letra mayúscula. "))

# if opcion == 1:
#     print(nombre.upper())
# elif opcion == 2:
#     print(nombre.lower())
# elif opcion == 3:
#     print(nombre.title())
# else:
#     print("La opcion no es valida")




# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

# magnitud = float(input("Ingrese la magnitud del terremoto: "))

# if magnitud < 3:
#     print("Muy leve")
# elif magnitud >= 3 and magnitud < 4:
#     print("Leve")
# elif magnitud >=4 and magnitud < 5:
#     print("Moderado")
# elif magnitud >= 5 and magnitud < 6:
#     print("Fuerte")
# elif magnitud >= 6 and magnitud < 7:
#     print("Muy fuerte")
# else:
#     print("Extremo")




# 10) Utilizando la información aportada sobre las estaciones del año. Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

# hemisferio = input("Ingrese en que hemisferio se encuentra (N/S) ").lower()
# mes = int(input("Ingrese en que mes se encuentre(en forma numerica y sin ceros) "))
# dia = int(input("Por ultimo ingrese que dia es: "))

# if hemisferio == "n":
#     if mes == 12 and dia >= 21 or mes == 1 or mes == 2 or mes == 3 and dia <= 20: 
#         print("Usted se encuentra en invierno")
#     elif mes == 3 and dia >= 21 or mes == 4 or mes == 5 or mes == 6 and dia <= 20: 
#         print("Usted se encuentra en primavera")
#     elif mes == 6 and dia >= 21 or mes == 7 or mes == 8 or mes == 9 and dia <= 20: 
#         print("Usted se encuentra en verano")
#     elif mes == 9 and dia >= 21 or mes == 10 or mes == 11 or mes == 12 and dia <= 20: 
#         print("Usted se encuentra en otoño")
# elif hemisferio == "s":
#     if mes == 12 and dia >= 21 or mes == 1 or mes == 2 or mes == 3 and dia <= 20: 
#         print("Usted se encuentra en verano")
#     elif mes == 3 and dia >= 21 or mes == 4 or mes == 5 or mes == 6 and dia <= 20: 
#         print("Usted se encuentra en otoño")
#     elif mes == 6 and dia >= 21 or mes == 7 or mes == 8 or mes == 9 and dia <= 20: 
#         print("Usted se encuentra en invierno")
#     elif mes == 9 and dia >= 21 or mes == 10 or mes == 11 or mes == 12 and dia <= 20: 
#         print("Usted se encuentra en primavera")