#Programa elaborado por: Velvet Samayoa
#Examen primer parcial

#-----------Ejercicio 1-------------
print("\n(¡Hola a ‘” Todas “’ y “’ Todos!’”’)")

#-----------Ejercicio 2-------------
nombre_usuario = input("\n¿Cúal es tu nombre?     --> ")
print("¡HOLA ", nombre_usuario,"!")

#-----------Ejercicio 3-------------
a=1
b=0
ope1 = b|b
ope2 = b|a
ope3 = a|b
ope4 = a|a
print("\nOPERACION LOGICA *OR*")
print(" ------------")
print("| A | B | Q | ")
print(" ------------")
print("|",b,"|",b,"|",ope1,"|")
print(" ------------")
print("|",b,"|",a,"|",ope2,"|")
print(" ------------")
print("|",a,"|",b,"|",ope3,"|")
print(" ------------")
print("|",a,"|",a,"|",ope4,"|")
print(" ------------")

#------------Ejercicio 4------------
puntos = float(input("\n¿Cúantos puntos recibe por hora estudiada?  --> "))
hr_martes = float(input("¿Cúantas horas estudia el curso el día martes?  --> "))
hr_jueves = float(input("¿Cúantas horas estudia el curso el día jueves?  --> "))
hr_semana = (puntos*hr_martes)+(puntos*hr_jueves)
hr_mes = hr_semana * 4
print("Usted a la semana obtiene: " + str("{:.2f}".format(hr_semana)) + " puntos")
print("Usted en el mes obtiene: " + str("{:.2f}".format(hr_mes)) + " puntos")


#-----------Ejercicio 5-------------
numero = int(input("\nPor favor ingrese un numero entero:  -->"))
sumatoria = numero*(numero + 1) / 2
print("La sumatoria de los numeros de 1 a " + str(numero)+ " es de: " + str(sumatoria))

#-----------Ejercicio 6-------------
libras = float(input("\n   ¿Cúanto pesa? (en lb) -->"))
kg = libras*0.453592
estatura = float(input("    ¿Cúanto mide? (en mt) -->"))
mt_c = estatura**2
imc = kg / mt_c
print("\n-----Tu índice de masa corporal es: " + str("{:.2f}".format(imc))+"-----")

#------------Ejercicio 7--------------
num1 = float(input("\nIngrese un número flotante:  "))
num2 = float(input("Ingrese otro número flotante:  "))
print("División de "+str(num1)+ " entre "+ str(num2))
num3 = num1 / num2
num4 = num1 % num2
print("El cociente es: ", "{:.2f}".format(num3))
print("El resto es: ", "{:.2f}".format(num4))

#------------Ejercicio 8----------------
cap = float(input("\n¿Cúanto capital desea invertir? -->  "))
tasa = float(input("¿Cúanto tasa de interés desea? -->  "))
tiempo = float(input("¿Cúantos años desea la inversión? -->  "))
i = tasa /100
interes = cap * i * tiempo
capf = cap + interes
print("El interes generado fue de: ", "{:.2f}".format(interes))
print("El capital final es de: ", "{:.2f}".format(capf))

#------------Ejercicio 9----------------
cant_bar = int(input("\n¿Cúantos barrenos desea en el pedido? -->  "))
cant_sier = int(input("¿Cúantas sierras desea agregar? -->  "))
bar = 112 * cant_bar
sier = 75 * cant_sier
peso = bar + sier
peso_lb = peso * 2.20462
print("El peso final del pedido es: "+  str(peso) + " kg.")
print("El peso en libras es de:  ", "{:.2f}".format(peso_lb))

#------------Ejercicio 10----------------
rams = int(input("\n¿Cúantas RAM semi-nuevas desea adquirir? -->  "))
precio = 20 * rams
des = precio * 0.6
print("El total con precio normal sería: ", str(precio))
print("El total con el descuento del 60"+"%"+" es: ", "{:.2f}".format(precio-des))
print("Usted ahorró: "+ str(des))

