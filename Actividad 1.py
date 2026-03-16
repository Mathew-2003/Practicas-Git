#Actividades introductorias

#1) Escribe un programa que solicite al usuario su año de nacimieto 
#   y muestre en qué año cumplirá 18, 21, 100 años


#edad = int(input("Ingrese su año de nacimiento: "))
#print(f"Cumplirá 18 en el año {edad + 18}")
#print(f"Cumplirá 21 en el año {edad + 21}")
#print(f"Cumplirá 100 en el año {edad + 100}")

#-------------------------------------------------------------------------

#2) Escribe un programa que solicite al usuario una cantidad de segundos
#   y muestre cuántas horas, minutos y segundo equivalen

#seg_ingresado = int(input("Ingrese una cantidad de segundos: "))
#horas = seg_ingresado // 3600
#minutos = (seg_ingresado%3600) // 60 
#segundos = (seg_ingresado%3600) % 60
#print(f"{horas} : {minutos} : {segundos}")

#-------------------------------------------------------------------------

#3) 3. Crea un programa que solicite al usuario un número 
# y muestre su tabla de multiplicar del 1 al 10 utilizando un bucle for.

#multiplo = int(input("Ingrese un numero: "))
#for num in range(1,11):
#    print(f"{num} x {multiplo} = {num * multiplo}")

#-------------------------------------------------------------------------

#4) Crea un programa que dado un número N ingresado por el usuario, 
#   imprima los números del 1 al N pero saltee los múltiplos de 5

#n = int(input("Ingrese un numero: "))
#for num in range(1,(n+1)):
#    if (num % 5) != 0:
#        print(f"{num}", end="-")

#-------------------------------------------------------------------------

#5) Escribe un programa que simule una caja registradora: 
# el usuario ingresa precios de productos de a uno. 
# Cuando ingresa 0, el programa se detiene y muestra el total acumulado. 
# Nota: utilizá la sentencia break cuando haga falta.

#suma = 0
#while True:
#    producto = float(input("Ingrese un precio: $"))
#    if producto == 0:
#        break
#    suma += producto
#print(f"El total del carrito es de ${suma}")

#-------------------------------------------------------------------------

#6) Modifica el ejercicio 4 para que, en lugar de imprimir los números, 
# genere dos listas: una con los múltiplos de 5 y otra 
# con el resto de los números. Imprimí ambas listas al finalizar.

#n = int(input("Ingrese un numero: "))
#lista_a = []
#lista_b = []
#for num in range(1, (n+1)):
#    (lista_b if num % 5 == 0 else lista_a).append(num)
#print("Lista A: ",lista_a)
#print("Lista B: ",lista_b)

#-------------------------------------------------------------------------

#7) Escribe un programa que solicite al usuario una lista de palabras. 
# Luego, construí una oración uniendo únicamente las palabras que tengan 
# más de 3 letras, separadas por espacios. Las palabras cortas deben ser 
# excluidas del resultado final.

#lista_palabras = input("Ingrese una lista de palabras: ").split()
#nueva_lista = [p for p in lista_palabras if len(p) > 3]
#print(" ".join(nueva_lista))
