#Nivel 1
#1
edad = int(input('ingresa tu edad: '))
años = int(18-edad)
if edad>= 18:
    print('Tiene edad suficiente para conducir')
else:
    print('espere {} para poder conducir'.format(años))
#2
miEdad = int(19)
tuEdad = int(input('ingresa tu edad: '))
año = int(tuEdad-19)
años =int (tuEdad-19)
añom = int(miEdad-tuEdad)
if miEdad == tuEdad:
    print('tenemos la misma edad')
elif tuEdad == 20:
    print('eres mayor por {} año'.format(año))
elif tuEdad >= 20:
    print('eres mayor  por {} años'.format(años))
else:
    print('eres menor por{} años'.format(añom))
#3
a = int(input('ingerese el primer numero: '))
b = int(input('ingrese el segundo numero: '))
if a > b:
    print(a,' es mayor a ',b)
elif a < b:
    print(a,'es menor a',b)
else:
    print('los numeros son iguales')
#Nivel 2
#1
cal = int(input('ingresa tu calificacion: '))
if cal>= 80:
    print('Tu calificacion es: A')
elif cal > 70 and cal < 79:
    print('Tu calificacion es: B')
elif cal > 60 and cal < 69:
    print('Tu calificacion es: C')
elif cal > 50 and cal < 59:
    print('Tu calificacion es: D')
else:
    print('Tu calificacion es: F')

#2
mes = input('Ingresa el mes:')
if mes in ['Septiembre','Octubre','Noviembre']:
    print('La temporada es otoño')
elif mes in ['Diciembre','Enero','Febrero']:
    print('La temporada es invierno')
elif mes in ['Marzo','Abril','Mayo']:
    print('La temporada es primavera')
else:
    print('La temporada es verano')
#3
fruits = ['banana', 'orange', 'mango', 'lemon']
newFruit = input('Inserta una fruta: ')
if newFruit in fruits:
    print('La fruta ya existe')
else:
    fruits.append(newFruit)
    print('lista modificada ',fruits)
#Nivel 3
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
#1
if 'skills' in person:
    print(person['skills'] [len(person['skills'])//2])
#2
    if 'Python' in person['skills']:
        print(person['skills'])
# 3
if 'skills' in person:
    hab = person['skills']
    if 'JavaScrip'in hab and 'React'in hab:
        print('He is a front end developer')
    elif 'Node' in hab and 'Phyron'in hab and'MongoDB' in hab:
        print('He is a backed developer')
    elif 'React' in hab and 'Node' in hab and 'MongoDB' in hab:
        print('He is a fullstack developer')
    else:
        print('unknown title')
#4
if person['is_marred'] == True and 'Finland' in person['country']:
    print('Asabeneh Yetayeh vive en Finland, y es casado')


print("Revisado")