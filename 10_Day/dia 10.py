#Nivel 1
#1
cont = 0
while cont <= 10:
    print(cont)
    cont = cont + 1

print('ciclo for')

numeros = [0,1,2,3,4,5,6,7,8,9,10]
for numero in numeros:
    print(numero)
#2
nums = [10,9,8,7,6,5,4,3,2,1,0]
for num in nums:
    print(nums)
print('ciclo while')

cont2 = 10 
while cont2 > -1:
    print(cont2)
    cont2 = cont2 -1
# 3
triangulo = '#'
for t in range(8):
    print(triangulo*t)
#4
sq = '#'
for c in range(8):
    print(sq*8)

#5
oper = 0
while oper< 11:
    print('{} x {}= {}'.format(oper,oper,oper*oper))
    oper = oper +1 

