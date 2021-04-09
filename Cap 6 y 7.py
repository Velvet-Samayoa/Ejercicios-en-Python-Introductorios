#-----------------CAPITULO 6----------------------

#----------OPERADORES DE COMPARACION------------
# print("100 == 100 -->", 100==100)
# print("10 != 100 -->", 10!=100)
# print("5 < 100 -->", 5<100)
# print("100 > 50 -->", 100>50)
# print("14 <= 20 -->", 14<=20)
# print("20 >= 100 -->", 20>=100)


#-------------OPERADORES LÓGICOS---------------
# print("(10 < 40) and (50 > 20)---> ", (10 < 40) and (50 > 20))
# print("(20 < 40) or (30 > 50)---> ",(20 < 40) or (30 > 50))
# print("not 10 < 20 ---> ", not 10 < 20)


#-------Trabajando con una declaración If------
# numero = int(input('Ingrese un número: '))
# if numero < 0:
#  print(numero, 'es negativo')
# print("")
# otro_num = int(input("Ingrese otro número: "))
# if otro_num > 0:
#  print(otro_num, " es positivo.")
#  print(otro_num, " El cuadrado es: ", otro_num*otro_num)
# print("Adiós")


#---------Else en una declaración iF----------
# numero = int(input("Ingresa un número más: "))
# if numero < 0:
#     print("Este Número es negativo")
# else:
#     print("Este número NO es negativo")


#--------------El uso de elif-----------------
# ahorro = int(input("Ingrese cúanto tiene ahorrado: "))
# if ahorro == 0:
#     print("Lo siento, no tiene ahorro.")
# elif ahorro < 1000:
#     print("LO haces bien.")
# elif ahorro < 5000:
#     print("Esa es una buena suma.") 
# elif ahorro < 10000:
#     print("Sea bienvenid@!")
# else:
#     print("GRACIAS.")


#--------Anidamiento de declaraciones If--------
# nevando = True
# temperatura = -10
# if temperatura < 0:
#     print("Se está congelando")
#     if nevando:
#         print("     Ponte las botas.")
#     print("Hora del chocolate caliente!")
# print("Adiós...")
# print("---------------------------")
# nevando = True
# temperatura = -10
# if temperatura < 0:
#     print("Se está congelando")
#     if nevando:
#         print("     Ponte las botas.")
#         print("     Hora del chocolate caliente!")
# print("Adiós...")


#---------Expresiones If--------------
# edad = 18
# estado = None
# if (edad > 15) and (edad < 20):
#     estado = "Adolescente"
# else: 
#     estado = "No es adolescente"
# print("A los ", edad, "--> ", estado)
# print("-----------------------------")
# estado = ("Adolescente" if edad>15 and edad<20 else "No es adolescente")
# print(estado)



#-----------------CAPITULO 7-----------------

#---------------Bucle While----------------
# contador = 5
# print("--INICIANDO--")
# while contador < 15:
#     print(contador, "  ", end='')  #es parte del bucle while
#     contador += 1   #esta también
# print("\n-----------------------------------------")  #ya no es parte del bucle
# print("Terminado...")


#-----------------Bucle For-----------------
    #Se quiere hacer un bucle sobre un conjunto de 
    #valores en un rango
# print("--Imprimiendo valores de un rango--")
# for a in range(0,10):
#     print(a, " - ", end='')
# print("\n-----------------------------------------")
# print("Terminado...")

    #Ahora usando valores de un rango incrementando en 2
# print("Imprimiendo valores en un rango de 2 en 2")
# for a in range(5, 20, 2):
#     print(a, " ", end='')
# print("\n-----------------------------------------")
# print("Terminado...")

    #Ahora usando una variable de bucle "anónima"
# for _ in range(0, 10):
#     print("* ", end='')
# print("\nListo")


#------Declaración de Break Loop (romper bucle)------
# print("Imprimir el código solo si se cumple todas las iteraciones")
# numero = int(input("Ingrese un número para la prueba: "))
# for i in range(10,20):
#     if i == numero:
#         break
#     print(i, " ", end='')
# print("Listo...")


#--------Declaración de bucle continuo--------
# for a in range(19,30):
#     print(a, "\n", end='')
#     if a % 2 == 1:
#         continue
#     print("Este es un Número PAR")
#     print("Amamos los números pares...")
# print("LISTO....")


#-------------Bucle For con Else-------------
    #se imprime el código si se cumplen todas
    #las iteraciones de una lista
# print("Solamente se imprime el código si todas las iteraciones")
# print("están completadas en una lista.....")
# print("-----------------------------------------------------")
# numero = int(input("Ingrese un número de prueba: "))
# for a in range(15,25):
#     if a == numero:
#         break
#     print(a, " ", end='')
# else:
#     print("\n------------------------------")
#     print("Todas las iteraciones fueron un Éxito...")


#----------Juego de tirar dados--------------
import random
MIN = 1
MAX = 10
lanza_denuevo ='si'
while lanza_denuevo == 'si':
    print("\nLos dados están rodando...")
    print("Los valores son: ")
    juego1 = random.randint(MIN, MAX)
    print(juego1)
    juego2 = random.randint(MIN, MAX)
    print(juego2)
    lanza_denuevo = input("Desea rodar los dados otra vez? (si/no):   ")

    