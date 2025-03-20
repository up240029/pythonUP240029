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
# 
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
 