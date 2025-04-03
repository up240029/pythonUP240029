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
#6
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def sixOrMoreCharst (countrie):
    if len(countrie) >=6:
        return True
    return False
rest = filter(sixOrMoreCharst,countries)
print(list(rest))
#7
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def starWhitE (countrie):
    return countrie.startswith("E")
rest = filter(starWhitE,countries)
print(list(rest))
#8
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = reduce(
    lambda x, y: x + y,map(lambda x: x * 2, filter(lambda x: x % 2 == 0, numbers)))
print(resultado)
#9
lista = [1,2,3,'hola','javi','marquez']
def getSrtingsList(list):
    return [item for item in list if isinstance(item, str)]
rest = getSrtingsList(lista)
print(rest)
#10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def addNumbers (x,y):
    return int(x) + int (y)
total = reduce(addNumbers,numbers)
print(total)
#11
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
def paisOracion (x,y):
    return x + ', ' + y
oracion = reduce(paisOracion,countries)
oracion1 = oracion + 'son paises de europa'
print(oracion1)
#12
from paises import countries
def categorizeCountries (countries,pattern):
    return list(filter(lambda country: pattern in country.lower(),countries))
print(categorizeCountries(countries,'land'))
#13
def countCountriesByInitial(countries):
    return dict(map(lambda letter: (letter, sum(1 for country in countries if country.startswith(letter))), sorted(set(map(lambda x: x[0], countries)))))
print(countCountriesByInitial(countries))
#14
def firsTen (countries):
    return list(map(lambda x:x, countries[:10]))
print(firsTen(countries))
#15
def LastTen (countries):
    return list(map(lambda x:x, countries[-10:]))
print(LastTen(countries))
#Nivel 3
#1
import paisesdata as paises
def obtenerNombre(pais):
    return pais["name"]
def obtenerCapital(pais):
    return pais["capital"]
def obtenerPoblacion(pais):
    return pais["population"]
def ordenarPorNombre(paises):
    return sorted(paises, key=obtenerNombre)
def ordenarPorCapital(paises):
    return sorted(paises, key=obtenerCapital)
def ordenarPorPoblacion(paises, reverse=False):
    return sorted(paises, key=obtenerPoblacion, reverse=reverse)
paisesLista = paises.paises  
ordenadoPorNombre = ordenarPorNombre(paisesLista)
print("\nOrdenado por nombre:")
for pais in ordenadoPorNombre:
    print(pais["name"])
ordenadoPorCapital = ordenarPorCapital(paisesLista)
print("\nOrdenado por capital:")
for pais in ordenadoPorCapital:
    print(pais["capital"])
ordenadoPorPoblacion = ordenarPorPoblacion(paisesLista, reverse=True)
print("\nOrdenado por población (de mayor a menor):")
for pais in ordenadoPorPoblacion:
    print(f"{pais['name']} - {pais['population']}")
#2
from collections import Counter

def contarTop10Idiomas():
    idiomas = []
    for pais in paises.paises:  
        if "languages" in pais:  
            idiomas.extend(pais["languages"]) 
    top10Idiomas = Counter(idiomas).most_common(10)
    return top10Idiomas
def mostrarTop10Idiomas():
    top10Idiomas = contarTop10Idiomas()
    print("Los 10 idiomas más hablados globalmente son:")
    for idioma, count in top10Idiomas:
        print(f"{idioma}: {count}")
mostrarTop10Idiomas()
#3
def clasificarPaisesMasPoblados():
    paisesOrdenados = sorted(paises.paises, key=lambda pais: pais["population"], reverse=True)
    return paisesOrdenados[:10]
def mostrarTop10PaisesMasPoblados():
    top10Paises = clasificarPaisesMasPoblados()
    print("Los 10 países más poblados son:")
    for pais in top10Paises:
        print(f"{pais['name']}: {pais['population']}")
mostrarTop10PaisesMasPoblados()

print("revisado")