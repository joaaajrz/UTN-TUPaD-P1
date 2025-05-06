# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

# for i in range(0, 100+1):
#    print(i)


# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

# num = int(input("Ingrese un numero "))
# cont= 0

# while num > 1 or num < -1:
#     num /= 10
#     cont += 1

# print(f"El numero ingresado {cont} digitos")


# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

# num1 = int(input("Ingrese un numero "))
# num2 = int(input("Ingrese otro numero "))
# sum = 0
# if num1 < num2:
#     for i in range (num1+1,num2):
#         sum += i
#     print(f"La suma de los numeros comprendidos entre {num1} y {num2} es {sum}")
# elif num1 > num2:
#     for i in range (num2+1,num1):
#         sum += i
#     print(f"La suma de los numeros comprendidos entre {num1} y {num2} es {sum}")
# else:
#     print(f"{num1} y {num2} son iguales")


# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

# num = int(input("Ingrese un numero entero (ingrese 0 para parar) "))
# acum = num

# while num != 0:
#     num = int(input("Ingrese un numero entero (ingrese 0 para parar) "))
#     acum += num
# print(acum)


# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

# import random
# numSecreto = random.randint(0,9)

# numUser = int(input("Adivina el numero secreto entre 0 y 9 "))
# intentos = 1

# while numUser != numSecreto:
#     numUser = int(input("INCORRECTO! Vuelve a intentarlo "))
#     intentos += 1

# print(f"Felicidades adivinaste el numero secreto({numSecreto}) en {intentos} intentos")


# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

# for i in range(100,0,-2):
#     print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

# num1 = int(input("Ingrese un numero "))
# sum = 0

# if num1 > 0:
#     for i in range (0,num1):
#         sum += i
#     print(f"La suma de los numeros comprendidos entre {num1} y 0 es {sum}")
# elif num1 < 0:
#     for i in range (num1+1,0):
#         sum += i
#     print(f"La suma de los numeros comprendidos entre {num1} y 0 es {sum}")
# else:
#     print(f"El numero ingresado no puede ser 0")

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).

# pares = 0
# impares = 0
# negativos = 0
# positivos = 0

# num = int(input("Ingrese un numero "))
# if num % 2 == 0:
#     pares += 1
# else:
#     impares += 1
# if num >= 0:
#     positivos += 1
# else:
#     negativos +=1

# for i in range(1,100):
#     num = int(input("Ingrese otro numero "))
#     if num % 2 == 0:
#         pares += 1
#     else:
#         impares += 1
#     if num >= 0:
#         positivos += 1
#     else:
#         negativos +=1

# print(f"De los numeros ingresados, {positivos} numeros son positivos, {negativos} numeros son negativos, {pares} numeros son pares y {impares} numeros son impares")



# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor)

# from statistics import mean

# numeros = [int(input("Ingrese un numero ")) for i in range(100)]
# media = mean(numeros)
# print(f"La media de los valores ingresados es: {media}")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

# numInvertido = 0
# num = int(input("Ingresa un numero "))
# copiaNum = num

# while num > 0:
#     ultimaCifra = num % 10
#     numInvertido = numInvertido * 10 + ultimaCifra
#     num //= 10
#     print(num)

# print(f"El numero {num} invertido es: {numInvertido}")
