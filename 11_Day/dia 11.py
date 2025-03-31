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
def sloveQuadraticEqn (a,b,c):
    if a == 0 :
        return
    dis = b**2 - 4*a*c
    if dis > 0 :
        x1=(-b+dis**0.5)/(2*a)
        x2=(-b-dis**0.5)/(2*a)
        return x1,x2
    elif dis == 0:
        x = -b/(2*a)
        return x
    else :
        return 'No tiene solucion'
Ecuacion = sloveQuadraticEqn (a = 2, b = 3, c = 7)
print ('La solucion es :', Ecuacion)
#8
def printList (lista) :
    for elemento in lista :
        print (elemento)
printList( lista = [2,3,5,6,1,8,])
#9
def reverseList (lista):
    listaIn=[]
    for i in range(len(lista)-1,-1,-1):
        listaIn.append(lista[i])
    return listaIn
print(reverseList(lista=[4,7,3,9,5]))

#10
def capitalizeListItems (items):
    return [item.upper() for item in items]
List = ['q','d','d']
listM =capitalizeListItems(List)
print(listM)
#11
def addItem (lista,elemento):
    lista.append(elemento)
    return lista
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(addItem(food_staff,'Meat'))
#12
def removeItem (lista,elemento):
    lista.remove(elemento)
    return lista 
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(removeItem(food_staff, 'Mango'))
#13
def sumaNumeros(num):
    suma=0
    for i in range(1,num+1):
        suma=suma+i
    return suma
print(sumaNumeros(num=5))
#14
def sumaImpares(num):
    suma=0
    for i in range(1,num+1,2):
        suma=suma+i
    return suma
print(sumaImpares(num=7))
#15
def sumaPares(num):
    suma=0
    for i in range(0,num+1,2):
        suma=suma+i
    return suma
print(sumaPares(num=5))
#Nivel 2
#1
def evensAndOdds (num) :
    impar = 0
    par = 0
    for i in range (1,num +1):
        if i % 2 == 0:
            par = par +1
        else :
            impar = impar + 1
    return par, impar 
print(evensAndOdds(num = 100))
#1.1
def factorial (num) :
    fac = 1
    for i in range (1,num + 1):
        fac = fac*i
        return fac
print(factorial(num = 7))
#2
def isEmpty (cosa):
    if len(cosa) == 0:
        return True
    else :
        return False
    
print (isEmpty(cosa = []))
#3
def media(lista):
    return sum(lista)/len(lista)
print(media(lista=[1,2,3,4,5]))
#No entendi si tenia que hacer todas las funciones o solo elegir una jajaj 
# Nivel 3
#1
def isPrime (n):
    if n <=1:
        return False
    for i in range (2,int(n**0.5)+1):
        if n % i == 0:
            return False
        return True
print(isPrime(n = 13))
#2
def allUnique (list):
    return len(list) == len(set(list))
print(allUnique([1,3,4,6,6]))
#3
def sameType (list):
    return all(isinstance(list[0],type(elemento)) for elemento in list)
print(sameType([1,2,3,4]))
#4
def isPythonVariable(variable):
    if variable.isidentifier():
        return True
    else:
        return False
print(isPythonVariable(variable='variable1'))