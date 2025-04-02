#1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
numFil = [num for num in numbers if num <= 0]
print(numFil)
#2
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
listaAplanada = [num for i in list_of_lists for j in i for num in j]
print(listaAplanada)
#3
tupleList = [(i, 1, i, i**2, i**3, i**4, i**5)for i in range (11)] 
print(tupleList)