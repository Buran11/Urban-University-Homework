#2023/09/25 00:00|Практическое задание по теме: "Словари и множества"

#Словари Dict
my_dict = {'Slava': 1985, 'Dasha': 1996, 'Marina': 1965}
print(f'Dict: {my_dict}')
print(f'Existing value: {my_dict.get('Slava')}')
print(f'Not existing value: {my_dict.get('Max')}')
my_dict.update({'Plina': 1989,
               'Sasha': 1986})
print(f'Deleted value: {my_dict.pop('Dasha')}')
print(f'Modified dictionary: {my_dict}')

#Множества Set
my_set = {33, 'fire', 5, 5, 'ice', 'fire'}
print(f'Set: {my_set}')
my_set.add('earth')
my_set.add((5.7, 'rock', 5))
my_set.remove(33)
print(f'Modified set: {my_set}')