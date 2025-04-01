#Nivel 1 
#1
import random
import string
def randomUserId ():
    return ''.join(random.choices(string.ascii_letters + string.digits, k= 6))
print('Este es su usuario ', randomUserId())
#2
def userIdGenByUser ():
    noCar = int(input('Ingrese el numero de caracteres '))
    noIds = int(input('ingrese el numero de ids '))
    Ids = [
        ''.join(random.choices(string.ascii_letters + string.digits, k= noCar))
        for _ in range(noIds)
    ]
    return Ids
print(userIdGenByUser())
#3
def genRgbColor ():
    rojo = random.randint(0,255)
    azul = random.randint(0,255)
    verde = random.randint(0,255)
    return(rojo,azul,verde)
print(genRgbColor())
#Nivel 2
#1
def listOfHexaColors (n):
    hexaColor = [

    ]
    for j in range(5):
     for _ in range (n):
        color = '#'+ ''.join(random.choices('0123456789ABCDEF',k=6))
        hexaColor.append(color)
     return hexaColor
print(listOfHexaColors(5))
#Segun yo es asi la  verdad no le entendi muy bien 
#2
def listOfRgbColors (n):
   return[(random.randint(0,255),random.randint(0,255),random.randint(0,255)) for _ in range(n)]

print(listOfRgbColors(5))

   
