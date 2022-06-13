# -*- coding: utf-8 -*-

import os
import time

def openMenu():
  """None->Integer
    Muestra un menú de opciones y devuelve la 
    opción ingresada por el usuario.
    Opciones:
    1. Factorial 
    2. Fibonacci
    3. Promedio Aritmetico
    4. Primo
    5. Para Salir

  """
  os.system ("clear") 
  print ("1. Factorial")
  print ("2. Fibonacci")
  print ("3. Promedio aritmético")
  print ("4. Determina si es un número primo")
  print ("5. Operaciones básicas")
  print ("6. Exit")

  opcion = int (input("Ingrese la opción elegida: ? "))
  return opcion

def subMenu():
  os.system("clear")
  print ("a. Sumar")
  print ("b. Restar")
  print ("c. Multiplicar")
  print ("d. Dividir")
  print ("e. Volver al principal") 

  opcionSub = input("Ingrese la opción elegida: ? ")
  accionesSub(opcionSub)

def accionesSub(opcion):
  if (opcion == "a"):
    numero1 = int(input("Ingrese el primer número a sumar: "))
    numero2 = int(input("Ingrese el segundo número a sumar: "))
    resultado = suma(numero1, numero2)
    print("El resultado de la suma entre", numero1, "y", numero2, "es :", resultado)
    time.sleep(5)
  elif (opcion == "b"):
    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número a restar: "))
    resultado = resta(numero1, numero2)
    print("El resultado de la resta entre", numero1, "y", numero2, "es :", resultado)
    time.sleep(5)
  elif (opcion == "c"):
    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número a multiplicar: "))
    resultado = multiplicar(numero1, numero2)
    print("El resultado de la multiplicación entre", numero1, "y", numero2, "es :", resultado)
    time.sleep(5)
  elif (opcion == "d"):
    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número a dividir: "))
    resultado = dividir(numero1, numero2)
    print("El resultado de la division entre", numero1, "y", numero2, "es :", resultado)
    time.sleep(5)
  elif (opcion == "e"):
    respuesta = openMenu()

    return respuesta
  else:
    print("La opción ingresada no es correcta")
    time.sleep(3)
    subMenu()

def suma(numero1, numero2):
  resultado = numero1 + numero2
  return resultado

def resta(numero1, numero2):
  resultado = numero1 - numero2
  return resultado

def multiplicar(numero1, numero2):
  resultado = numero1 * numero2
  return resultado

def dividir(numero1, numero2):
  resultado = numero1 / numero2
  return resultado
    
def factorial (numero):
  """Integer -> Integer"""
  print("Se debe genera el código para calcular el factorial de: ", numero)
  respuesta = 1
  for i in range(1, numero+1):
    respuesta = respuesta * i
  return respuesta

def fibonacci(numero):
  """Integer -> Integer"""
  print("Se debe genera el código para calcular el fibonacci de: ", numero)
  respuesta = 0
  if numero == 0 or numero == 1:
      respuesta = numero

  numero1 = 0
  numero2 = 1
  for i in range(2, numero+1):
    respuesta = numero1 + numero2
    numero1 = numero2
    numero2 = respuesta

  return respuesta

def promedioAritmetico (numero1, numero2):
  """Integer Integer-> Integer"""
  print("Se debe genera el código para calcular el promedio de: ", numero1, " con ", numero2 )
  respuesta = (numero1 + numero2) / 2
  return respuesta

def esPrimo (numero):
  """Integer -> Boolean"""
  print("Se debe genera el código para calcular si es primo o no el: ", numero, " dado ")

  divisores = 0
  respuesta = ''
  
  for i in range(1, numero+1):
    if (numero % i == 0):
      divisores = divisores + 1
    else:
      divisores = divisores

  if divisores <= 2:
    respuesta = "Es primo"
  else:
    respuesta = "No es primo"

  return respuesta
  
def realizarAcciones(opcion):
  """ Integer -> None
      Realiza una acción según la opción del menú elegida. Si la opcion no es valida entonces muestra en pantalla un mensaje de error. 
  """
  if (opcion ==  1):
    numero= int(input("Ingrese nro a calcular? "))
    respuesta = factorial (numero)
    print ("El factorial del numero dado es: ", respuesta)
    time.sleep(5)
  elif (opcion == 2):
    numero= int(input("Ingrese nro a calcular? "))
    respuesta = fibonacci (numero)
    print ("El fibonacci del numero dado es: ", respuesta)
    time.sleep(5)
  elif (opcion == 3):
    numero1= int(input("Ingrese 1er nro a calcular? "))
    numero2= int(input("Ingrese 2do numero a calcular? "))
    respuesta = promedioAritmetico(numero1, numero2)
    print ("El promedio aritmetico del numero dado es:", respuesta)
    time.sleep(5)
  elif (opcion == 4):
    numero = int(input("Ingrese nro a calcular si es primo? "))
    respuesta = esPrimo(numero)
    print ("El resultado de la operacion dada es:", respuesta)
    time.sleep(5)
  elif (opcion == 5):
    subMenu()
  else:
    print ("La opción seleccionada no es valida.")
    

def main():
  respuesta = openMenu()
  while (respuesta != 6):
    realizarAcciones(respuesta)
    respuesta= openMenu()
  print("Gracias por usar este Menú")


main()
 

