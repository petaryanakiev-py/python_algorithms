from functools import reduce
import timeit

squares = [x ** 2 for x in range(10)]
powers_of_two = [2 ** i for i in range(13)]
even_squares = [x for x in squares if x % 2 == 0]
cubes = [x ** 3 for x in range(12)]

def make_even_squares(numbers):
    new_squares = []
    for n in numbers:
        if n % 2 == 0:
            new_squares.append(n ** 2)
    return new_squares

numbers = [x for x in range(10)]

kilometers = [39.2, 36.5, 37.3, 37.8]
feets = map(lambda x: float(3280.8399) * x, kilometers)
reduced_feets = reduce(lambda x, y: x + y, feets) # = sum([x for x in feets])

not_even_squares = filter(lambda x: x % 2, squares)

divided = [x for x in range(100) if x % 2 == 0 if x % 6 == 0]

# if-else statement in list comprehension
some_list = [x + 1 if x >= 1200 else x + 5 for x in squares]

list_of_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [x for y in list_of_list for x in y]

matrix = list_of_list
transposed_matrix = [[row[i] for row in matrix] for i in range(len(matrix))]

print(transposed_matrix)
print(flattened_list)
print(some_list)
print(divided)
print(list(not_even_squares))
print(reduced_feets)
print(list(feets))
print(timeit.timeit('[x ** 2 for x in range(10) if x % 2 == 0]', number = 10000))
print(timeit.timeit('make_even_squares(numbers)', globals=globals(), number=1000))
print(powers_of_two)
print(even_squares)
print(cubes)