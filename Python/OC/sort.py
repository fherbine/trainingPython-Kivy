from random import Random

lst1 = ['fherbine', '42', 42, 'toto', 'tata', 'tutu', 'titi']
players = [
    {'name': 'fherbine', 'age': 20, 'level': 100000},
    {'name': 'bad_player', 'age': Random().randint(0, 100), 'level': 0},
    {'name': 'bad_player', 'age': Random().randint(0, 100), 'level': 0},
    {'name': 'bad_player', 'age': Random().randint(0, 100), 'level': 0},
    {'name': 'bad_player', 'age': Random().randint(0, 100), 'level': 0},
    {'name': 'bad_player', 'age': Random().randint(0, 100), 'level': 0},
    {'name': 'bad_player', 'age': Random().randint(0, 100), 'level': 0},
    {'name': 'bad_player', 'age': Random().randint(0, 100), 'level': 0},
    {'name': 'bad_player', 'age': Random().randint(0, 100), 'level': 0},
]


print(lst1)
lst1.pop(2)
lst1.sort()
print(lst1)

Random().shuffle(lst1)

print(lst1)
print(sorted(lst1))

print(players)
print(sorted(players, key=lambda player: player['age']))
print(sorted(players, key=lambda player: player['level'], reverse=True))
