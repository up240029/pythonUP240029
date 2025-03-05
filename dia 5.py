#Programa 1
emptyList =[]
print(len(emptyList))
#Programa 2
list = ['Azucar','Avena','Leche','Pan','Huevos']
#Programa 3
print(len(list))
#Programa 4
print(list[0])
print(list[2])
print(list[4])
#Programa 5
mixedDataTypes = ['Javier', '19', '77.8', 'single', 'Hacienda gracias a dios no. 155']
#Programa 6
itCompanies =['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
#Programa 7
print(itCompanies)
#Programa 8
print(len(itCompanies))
#Programa 9
print(itCompanies[0],itCompanies[3],itCompanies[6])
#Programa 10
print(itCompanies)
itCompanies[0] = 'Meta'
print(itCompanies)
#Programa 11
print(itCompanies)
itCompanies.append('E-bay')
print(itCompanies)
#Programa 12
itCompanies.insert(3, 'tesla')
print(itCompanies)
#Programa 13
itCompanies[0] = itCompanies[0].upper()
print(itCompanies)
#Programa 14
print('#'.join(itCompanies))
#Programa 15
doesExist = 'tesla' in itCompanies
print(doesExist)
#Programa 16
itCompanies.sort()
print(itCompanies)
#Programa 17
itCompanies.reverse()
print(itCompanies)
#Programa 18
print(itCompanies[3:9])
#Programa 19
print(itCompanies[0:6])
#Programa 20
print(itCompanies[0:4]+itCompanies[5:9])
#Programa 21
del itCompanies[0]
print(itCompanies)
#Programa 22
del itCompanies[5]
print(itCompanies)
#Programa 23
itCompanies.pop() 
print(itCompanies)
#Programa 24
del itCompanies
#Programa 25
#itCompanies.clear()// Con este comando limpias o destruyes la lista 
#Programa 26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
lista = front_end + back_end
print(lista)
#Programa 27
fullStak= lista.copy()
fullStak.insert(5,'python')
fullStak.insert(6,'sql')
print(fullStak)
# Nivel 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages[0],ages[len(ages)-1])
ages.insert(0,19)
ages.insert(-1, 26)
print(ages)

