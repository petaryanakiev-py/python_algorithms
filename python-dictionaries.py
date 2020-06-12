questions = ['name', 'quest', 'favourite color']
answers = ['lancelot', 'the holy grail', 'blue']

for q, a in zip(questions, answers):
    print('What is your {0}? It is {1}.'.format(q, a))

for i in reversed(range(1, 10, 2)):
    print(i)

# dictionary comprehension
squares = {x: x ** 2 for x in range(10)}

if 4 in squares:
    print('Four\'s there')
else:
    print('Four isn\'t there')

for key, value in squares.items():
    print(key, value)

print(squares)