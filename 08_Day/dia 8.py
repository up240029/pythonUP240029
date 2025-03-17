# Programa 1
dog = {}
# Programa 2
dog['nombre'] = 'candy'
dog['color'] = 'cafe'
dog['raza'] = 'labrador'
dog['patas'] = '4'
dog['edad'] = '5'
print(dog)
#Programa 3
estudiantes = {
    'Nombre': 'Javier',
    'Apellido': 'Marquez',
    'Genero': 'Masculino',
    'Edad': '19',
    'Estado civil': 'Soltero',
    'Habilidades': ['Veloz','Inteligente','matematicas'],
    'Pais': 'Mexico',
    'Ciudad': 'Aguascalentes',
    'Direccion': {
        'Calle': 'Haciendas gracias a Dios no. 155',
        'Colonia': 'Haciendas de Aguascalientes'
    }

    }
#Programa 4
print(len(estudiantes))
#Programa 5
print(estudiantes['Habilidades'])
print(type(estudiantes['Habilidades']))
#Programa 6
estudiantes['Habilidades'].append('programar')
estudiantes['Habilidades'].append('conducir')
print(estudiantes)
#Programa 7
keys = estudiantes.keys()
print(keys)
#Programa 8
values = estudiantes.values()
print(values)
#Programa 9
print(estudiantes.items())
#Programa 10
estudiantes.pop('Direccion')
print(estudiantes)
#Programa 11
del estudiantes
