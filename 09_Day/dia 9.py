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
fruta = input('Ingresa la fruta:')
if fruta in fruits:
    print('Esta fruta si existe en esta lista')
else:
    fruits.append(fruta)
    print(fruits)