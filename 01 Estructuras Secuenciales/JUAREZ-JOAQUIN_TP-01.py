#Punto 1: Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.  
#print("Hola Mundo!")


#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”. 
#nombre = input("¿Cual es tu nombre? ")
#print(f"Hola {nombre}!")


#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. 
#nombre = input("¿Cual es tu nombre? ")
#apellido = input("¿Cual es tu apellido? ")
#edad = int(input("¿Cual es tu edad? "))
#lugarResidencia = input("¿Donde vives? ")
#print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugarResidencia}")


#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro. 
#pi = 3.14159
#radio = float(input("Ingrese el radio del circulo: "))
#area = pi * radio ** 2
#perimetro = 2 * pi * radio
#print(area)
#print(perimetro)


#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.
#seg = int(input("Ingrese una cantidad de segundo: "))
#horas = seg / 3600
#print(f"{seg} segundos equivalen a {horas} horas")


#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.
#num = int(input("Ingrese un numero: "))
#print(num," por 1, es:",(num * 1))
#print(num," por 2, es:",(num * 2))
#print(num," por 3, es:",(num * 3))
#print(num," por 4, es:",(num * 4))
#print(num," por 5, es:",(num * 5))
#print(num," por 6, es:",(num * 6))
#print(num," por 7, es:",(num * 7))
#print(num," por 8, es:",(num * 8))
#print(num," por 9, es:",(num * 9))
#print(num," por 10, es:",(num * 10))


#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos. 
#num1 = int(input("Ingrese un numero entero distinto a 0: "))
#num2 = int(input("Ingrese otro numero entero distinto a 0: "))
#rSum = num1 + num2
#rDiv = num1 / num2
#rMul = num1 * num2
#rRes = num1 - num2

#print(f"Si sumamos {num1} mas {num2} da {rSum}")
#print(f"Si dividimos {num1} por {num2} da {rDiv}")
#print(f"Si multiplicamos {num1} por {num2} da {rMul}")
#print(f"Si a {num1} le restamos {num2} da {rRes}")


#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. 
#alt = int(input("Ingrese su altura en centimetros: "))
#alt = alt/100 
#peso = float(input("ingrese su peso en Kg: "))
#print(f"Su indice de masa corporal es {peso / alt**2}")


#Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. 
#tempC = float(input("Ingrese una temperatura en Celsius: "))
#tempF = (9/5) * tempC + 32
#print(f"{tempC}°C son {tempF}°F")


# 10) Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de dichos números.
#num1 = float(input("Ingrese un numero: "))
#num2 = float(input("Ingrese un numero mas: "))
#num3 = float(input("Ingrese otro numero: "))
#promedio = (num1 + num2 + num3) / 3
#print(f"El promedio entre {num1}, {num2} y {num3} es {promedio}")