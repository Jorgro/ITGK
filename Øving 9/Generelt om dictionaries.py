my_family = {}

def add_family_members(role, name):
    my_family.setdefault(role,[]).append(name)
    return my_family


add_family_members('bror', 'Arne')
add_family_members('mor', 'Anne')
add_family_members('bror', 'Geir')

def printer(dictionary):
    for key, value in my_family.items():
        print(f'{key}: {", ".join(value)}')
printer(my_family)
