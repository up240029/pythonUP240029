#Programa 1
emptyTuple= ()
print(len(emptyTuple))
#Programa 2
hermanos = ('Santiago','Isai','Octavio')
Hermanas = ('Sofia','Luna','Majo')
print(hermanos)
print(Hermanas)
#Programa 3
hermanes = hermanos + Hermanas
#Programa 4
print('Tengo {} hermanos'.format(len(hermanes)))
#Programa 5
miembrosFam = hermanes + ('Paco', 'Cony')
print(miembrosFam)
#Nivel 2
#1
Hr1, Hr2, Hr3, Hr4, Hr5, Hr6, Pap, Mom, *rest = miembrosFam
print(rest) 
#2
tupAnimal = ('Leche','huevo','carne')
tupVerduras =('zanahoria','Brocoli','lechuga')
tupFrutas = ('Manzana','Mango','Guayaba')
foodStuffTp = tupAnimal + tupVerduras + tupFrutas
print(foodStuffTp)
#3
foodStuffTp = list(foodStuffTp)
#4
print(foodStuffTp[3:6])
#5
print(foodStuffTp[0:3],foodStuffTp[6:9])
#6
del foodStuffTp
# 7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)