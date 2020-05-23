def get_fib(position):
    if position == 0 or position == 1:
        return position
    return get_fib(position - 1) + get_fib(position - 2)

def factorial(number):
    if number == 1:
        return 1
    return number * factorial(number - 1)

# Test Cases
print(get_fib(3))
print(get_fib(9))