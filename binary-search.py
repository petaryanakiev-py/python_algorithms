def binary_search(input_array, value):
    low_index = 0
    high_index = len(input_array) - 1
    while low_index <= high_index:
        middle_index = (int)((low_index + high_index) / 2)
        if (input_array[middle_index] == value):
            return middle_index
        elif value < input_array[middle_index]:
            high_index = middle_index - 1
        else:
            low_index = middle_index + 1
    return -1

def binary_search_recursive(input_array, value, low_index, high_index):
    middle_index = (int)((low_index + high_index) / 2)
    if low_index > high_index:
        return -1
    elif value == input_array[middle_index]:
        return middle_index
    elif value < input_array[middle_index]:
        return binary_search_recursive(input_array, value, low_index, middle_index - 1)
    else:
        return binary_search_recursive(input_array, value, middle_index + 1, high_index)

def binary_search_placeholder(input_array, value):
    return binary_search_recursive(input_array, value, 0, len(input_array) - 1)

# Test Cases
test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
test_val3 = 1
print(binary_search_placeholder(test_list, test_val1))
print(binary_search_placeholder(test_list, test_val2))
print(binary_search_placeholder(test_list, test_val3))