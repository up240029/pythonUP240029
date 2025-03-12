it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
#Nivel 1
#Programa 1
print(len(it_companies))
#Programa 2
it_companies.add('Twiter')
print(it_companies)
#Programa 3
it_companies.update(['Tesla', 'Space x'])
print(it_companies)
#Programa 4
it_companies.remove('Google')
print(it_companies)
#Programa 5
#¿Cuál es la diferencia entre eliminar y descartar?
#Si usas el comando remove () si el caracter o el valor no se encuentra en el set, este arrojara error  y 
#con el comando discard no te dara nada
#Nivel 2
#1
print(A.union(B))
#2
print(A.intersection(B))
#3
print(A.issubset(B))
#4
print(A.isdisjoint(B))
#5
print(A.union(B))
print(B.union(A))
#6
print(A.symmetric_difference(B))
#7
del A
#Nivel 3





