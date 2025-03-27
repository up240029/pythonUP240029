#Nivel 1
#1
def addTwoNumbres ():
    c = 2
    b = 4
    a = b + c
    print(a)
addTwoNumbres ()
#2
def areaCirculo ():
    radio = 12
    pi = 3.1416
    area = pi * radio **2
    print(area)
areaCirculo ()
#3
def addAllNums (*args):
    if all ( isinstance(arg,(int, float )) for arg in args ):
        return sum(args)
    else:
        return print(' todos los resultados deben de ser numeros ')
    
conjunto = [1,2,3]
res = addAllNums(*conjunto)
print(res)
#4
def convertCelToFa ():
    celcius = float(input('Ingrese la temperatura: '))
    farenheit = celcius * 1.8 + 32
    print('la temperatura es', farenheit)
convertCelToFa ()
#5
def checkSeason ():
    mes = input('inserte el mes: ')
    if mes in ['Septiembre','Octubre','Noviembre']:
        print('Es otoño')
    elif mes in ['Diciembre','Enero','Febrero']:
        print('Es invierno')
    elif mes in ['Marzo','Abril','Mayo']:
        print('Es primavera')
    else:
        print('Es verano')
checkSeason ()
#6
def calculateSlope (x1,y1,x2,y2):
    slope = (y2 - y1) / (x2 - x1)
    return slope
pendiente = calculateSlope (1,2,3,6)
print ('la pendiente es ', pendiente)
#7