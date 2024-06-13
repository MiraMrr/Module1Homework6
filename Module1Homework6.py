my_dict = {'Irina': 1969, 'Igor': 1967, 'Svetlana': 1970}
print('Dict: ', my_dict)
print('Existing value: ', my_dict.get('Irina'))
print('Not existing value: ', my_dict.get('Dmitriy'))
my_dict.update({'Evgeniy': 1991,
                'Karina': 1994})
igor = my_dict.pop('Igor')
print('Deleted value: ', igor)
print('Modified dictionary: ', my_dict)


my_set = {1, 2, 3.5, 4.5, 'five', 'six', 2, 2, 4.5, 'six', 1}
print('Set: ', my_set)
my_set.add((8, 9, 10))
my_set.add('eleven')
my_set.discard(1)
print('Modified set: ', my_set)
