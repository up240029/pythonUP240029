# Problemas 1, 2 y 3
edad = 19
Peso = 78.5 
complex = 2+3j
print(type(edad))
print(type(Peso))
print(type(complex))
# Problema 4 
base = float(input("ingrsa el valor de la base: "))
altura = float(input("ingresa el valor de la altura: "))
area = 0.5 * base * altura
print ("El area del triangulo es: ", area )
# Problema 5
lado1 = float(input("ingresa el primer lado: "))
lado2 = float(input("ingresa el segundo lado: "))
lado3 = float(input("ingresa el tercer lado: "))
perimetro = lado1 + lado2 + lado3 
print ("El perimetro es: ",perimetro )
#Programa 6
longitud = float(input("ingresa la longitud: "))
ancho = float(input(" ingresa el ancho: "))
area = longitud * ancho
perimetro = 2 * ( longitud + ancho )
print( "El area es: ", area)
print ( "El perimero es: ", perimetro)
#Programa 7
radio = float(input("ingresa el valor del radio: "))
pi = 3.14
area = pi * radio**2 
perimetro = 2 * pi * radio
print("El area del cireculo es: ",area)
print("El perimertro es: " , perimetro)
#Programa 8
#Pendiente de la recta y = 2x-2
penRecta = 2
interY = -2
interX = interY/penRecta
print("La pendiente de la recta es: ",penRecta)
print("la interseccion en y es: " , interY)
print("La interseccion en x es: " , interX)
#Programa 9
x1 = 2
y1 = 2
x2 = 6
y2 = 10
m1 = y2-y1 
m2 = x2 - x1 
m = m1 /m2
print("la pendiente es: " , m)
#Programa 10
print("pendientes son iguales "if penRecta == m else "las pendientes son diferentes ")
#Programa 11
x = int(input ("inserta el valor de x: "))
y = x**2 + 6*x +9
print("El valro de y es: " , y)
if y == 0 :
    print("y es 0 cuando x es: ", x)
else:
    print("y no es 0 cuado x es: ", x)
    
#Programa 12
print(len("phyton")>len("dragon"))
#Programa 13
print("on"in "phyton"and "on" in "dragon")
#Programa 14
oracion = "I hope this course is not full in jargon" 
print("jargon" in oracion )
#PROGRAMA 15
print("on" not in "phyton" and "on" not in "dragon")
#Programa 16
print(str(float(len("phyton"))))
#Programa 17
num =int(input("ingresa un numero: "))
if num % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")
#Programa 18
res = 7//3 == int(2.7)
print(res)
#Programa 19
res = type("10") == type(10)
print(res)
#Programa 20
res = float("9.8") == 10


print(res)
# Programa 21
hora = float(input("Ingrese las horas que trabajo: "))
Tar = float(input("Ingrese la tarifa: "))
pagoTotal = hora * Tar
print("El pago total es: ", pagoTotal)
#Pograma 22
años = int(input("Ingrese sus años vividos: "))
maxAños = 100
segXaños = 365 * 24 * 60 * 60
# Verificar que no se supere el limite
if años > maxAños:
    print("El maximo de años permitidos es {maxAños}. Se va a usar {maxAños} para el calculo")
    años = maxAños
seg = años * segXaños
print("En {años} años una persona puede vivir {seg} segundos.")
# Programa 23
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")


print('Revisado')




