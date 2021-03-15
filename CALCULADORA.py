#!/usr/bin/python3

import sys
import os
import time
import os as sistema

# Set color
R = '\033[31m' # Red
N = '\033[1;37m' # White
G = '\033[32m' # Green
O = '\033[0;33m' # Orange
B = '\033[1;34m' #Blue

print (""+O+"")
os.system('clear')

def pedirOpcionCorrecta():
        correcto=False
        num=0
        while(not correcto):
                try:
                        num = int(input("Elige una opcion: "))
                        correcto=True
                except ValueError:
                        print('Error, Elige una opcion correcta: ')

        return num

salir = False
opcion = 0

while not salir:
	print ("""
   _    _        _              _    __    __    __    _
  / )  /_|  /   / )  /  /  /   /_|  /  )  /  )  /__)  /_|
 (__  (  | (__ (__  (__/  (__ (  | /(_/  (__/  / (   (  | """)
	print ("")
	print ("""
	 _ _ _ _ _ _ _ _ _ _ _
	|		      |
	| 1. SUMA	      |
	|		      |
	| 2. RESTA	      |
	|		      |
	| 3. MULTIPLICACION   |
	|		      |
	| 4. DIVISION         |
	|		      |
	| 5. POTENCIACION     |
	|		      |
	| 6. SALIR	      |
	|_ _ _ _ _ _ _ _ _ _ _|""")
	print ("")

	opcion = pedirOpcionCorrecta()

	if opcion == 1:
		print ("")
		print ("Suma")
		print ("")
		a = int(input("Ingresa el primer valor: "))
		b = int(input("Ingresa el segundo valor: "))
		suma = a + b
		print ("El resultado es:", suma)
		time.sleep(6)
		os.system('clear')
	elif opcion == 2:
		print ("")
		print ("Resta")
		print ("")
		a = int(input("Ingresa el primer valor: "))
		b = int(input("Ingresa el segundo valor: "))
		resta = a - b
		print ("El resultado es:", resta)
		time.sleep(6)
		os.system('clear')
	elif opcion == 3:
		print ("")
		print ("Multiplicacion")
		print ("")
		a = int(input("Ingresa el primer valor: "))
		b = int(input("Ingresa el segundo valor: "))
		multi = a * b
		print ("El resultado es:", multi)
		time.sleep(6)
		os.system('clear')
	elif opcion == 4:
		print ("")
		print ("Division")
		print ("")
		a = int(input("Ingresa el primer valor: "))
		b = int(input("Ingresa el segundo valor: "))
		divi = a / b
		print ("El resultado es:", divi)
		time.sleep(6)
		os.system('clear')
	elif opcion == 5:
		print ("")
		print ("Potenciacion")
		print ("")
		a = int(input("Ingresa el primer valor: "))
		b = int(input("Ingresa el segundo valor: "))
		poten = a ** b
		print ("El resultado es:", poten)
		time.sleep(6)
		os.system('clear')
	elif opcion == 6:
		salir = True
	else:
		print ("Introduce un numero entre 1 y 6")
print ("¡Fín!, espero le haya gustado esta herranienta, hasta luego")
print ("")

