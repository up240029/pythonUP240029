#Nivel 1
#1
# La funcion map toma una funcion y un iterable como parametros, la funcion filter filtra los elementos que cumplen con
# el criterio de filtrado establecido y reduccion  funciona igual que map y filter pero no devuelve un iterabele  si no un
#unico valor.
#2
#Las funciones de orden superior permiten tomar funciones como parametros y sel resultado que devuelva puede ser otra funcion 
#Un cierre es una funcion anidada dentro de una funcion que es encapsulada y luego devolviendo la funcion anidada 
# Y un decorador permite al usuario añadir nuevas funciones a un objeto existente sin modificar su estructura 
#3 
from functools import reduce
numbers_str = ['1', '2', '3', '4', '5']
def suma (x,y):
    return int(x) + int(y)
total = reduce(suma,numbers_str)
print(total)
#4
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
for countrie in countries:
    print(countrie)
#5
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
for name in names:
    print(name)
#6
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    print(num)
#Nivel 2
#1
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def ChangeUpper (countrie):
    return countrie.upper ()
rest = map(ChangeUpper,countries)
print(list(rest))
#2
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def cuadrado (n):
    return n ** 2
rest = map(cuadrado,numbers)
print(list(rest))
#3
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
def changeUpperNames (name):
    return name.upper()
rest =map(changeUpperNames,names)
print(list(rest))
#4
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def onlyLand (countrie):
    if 'land' in countrie:
        return True
    return False
rest = filter(onlyLand,countries)
print(list(rest))
#5
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def sixChart(countrie):
    if len(countrie) == 6:
        return True
    return False
rest = filter(sixChart,countries)
print(list(rest))



