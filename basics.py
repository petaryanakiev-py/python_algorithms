def sum(a, b):
    return a + b

def divide(divident, divisor):
    quotient = divident / divisor
    remainder = divident % divisor
    return quotient, remainder

answer = 42 #integer
answer = "The answer is 42."

flag = False # boolean
string = "This is example string"

arr = ["string", 1, 2, 3, 4, "another string"]
tuples = ("Tuple", 1, 2, 3, "another element")

dictionary = {'one': 1, 'two': 2, 'three': 3}
not_initialized_variable = None

if flag == True:
    print("Flag is true")
else:
    print("Flag is false")

for item in arr:
    print(item)

print(sum(1, 5))
print(divide(12, 3))

def calculate_stuff(x, y):
    (q, r) = divide(x,y)
    print(q, r)

calculate_stuff(3, 4)

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def birthaday(self):
        self.age += 1

me = Person("Pesho", 22)
print(me.name, me.age)

def decode():
    value = input("Enter your string: ")
    print(value)

colors = ['red', 'blue', 'green']
i = 0
while i < len(colors):
    print(colors[i])
    i = i + 1

for i in range(3):
    print(colors[i])

other = colors # = does not make a copy
other[0] = 'yellow'

for i in range(3):
    print(colors[i])
    print(other[i])

squares = [1, 4, 9, 16]
sum = 0
for number in squares:
    sum += number
print(sum)

colors[0] = 'black'
if 'yellow' in colors:
    print('Yellow is there')
else:
    print('Yellow is not there')

# common list methods
colors.append('white')
colors.append('brown')
colors.append('orange')
colors.insert(1, 'grey')
colors += ['pink', 'purple'] # same as colors.extend(['pink', 'purple'])
colors.sort()
colors.remove('pink')
colors.reverse()
colors.pop(0)
print(colors.index('grey'))
print(colors[1:-1]) # prints colors from index 1 to the last but one