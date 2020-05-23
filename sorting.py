# Naive sorting algorithms
# O(n^2)

def bubble_sort(input_array):
    size = len(input_array)
    for i in range(size):
        for j in range(size - i - 1):
            if input_array[j] > input_array[j + 1]:
                temp = input_array[j]
                input_array[j] = input_array[j + 1]
                input_array[j + 1] = temp

def selection_sort(input_array):
    for i in range(len(input_array)):
        min_index = i
        for j in range(i, len(input_array)):
            if input_array[j] < input_array[min_index]:
                min_index = j
        temp = input_array[i]
        input_array[i] = input_array[min_index]
        input_array[min_index] = temp

def insertion_sort(input_array):
    for i in range(1, len(input_array)):
        key = input_array[i]
        j = i - 1
        while j >= 0 and key < input_array[j]:
            input_array[j + 1] = input_array[j]
            j -= 1
        input_array[j + 1] = key


# Better sorting algorithms
# O(n*log(n))
# Merge sort - not in place - O(n)
def merge_sort(input_array):
    if len(input_array) > 1:
        middle_index = len(input_array) // 2
        # divide into two halves
        left_half = input_array[:middle_index]
        right_half = input_array[middle_index:]

        # reqursively divide until reaching one element arrays
        merge_sort(left_half)
        merge_sort(right_half)

        # conquer == merge the divided arrays
        left_counter = right_counter = final_counter = 0
        while left_counter < len(left_half) and right_counter < len(right_half):
            if left_half[left_counter] < right_half[right_counter]:
                input_array[final_counter] = left_half[left_counter]
                left_counter += 1
            else:
                input_array[final_counter] = right_half[right_counter]
                right_counter += 1
            final_counter += 1
            
        while left_counter < len(left_half):
            input_array[final_counter] = left_half[left_counter]
            left_counter += 1
            final_counter += 1

        while right_counter < len(right_half):
            input_array[final_counter] = right_half[right_counter]
            right_counter += 1
            final_counter += 1

def partition(input_array, low_index, high_index):
    # Pivot can be different depending on choosing strategy
    pivot = input_array[high_index]
    # as firstly no element is considered smaller than pivot:
    smaller_index = low_index - 1

    for current_index in range(low_index, high_index):
        if input_array[current_index] < pivot:
            smaller_index += 1
            input_array[current_index], input_array[smaller_index] = input_array[smaller_index], input_array[current_index]
    
    # putting the pivot in its right place
    smaller_index += 1
    input_array[smaller_index], input_array[high_index] = input_array[high_index], input_array[smaller_index]
    return smaller_index    

def quick_sort_placeholder(input_array, low_index, high_index):
    if low_index < high_index:
        partition_index = partition(input_array, low_index, high_index)
        quick_sort_placeholder(input_array, low_index, partition_index - 1)
        quick_sort_placeholder(input_array, partition_index + 1, high_index)

# O(n * log(n)) average and best case
# O(n^2) in its worst case (for already sorted array)
def quick_sort(input_array):
    quick_sort_placeholder(input_array, 0, len(input_array) - 1)

# O(l + n), where l is the upper bound (range) and n is the number of elements 
# Space complexity: again O(l + n)
def counting_sort(input_array, upper_bound):
    counting_arr = [0] * (upper_bound + 1)

    for element in input_array:
        counting_arr[element] += 1

    current_index = 0
    for i in range(upper_bound + 1):
        while counting_arr[i] > 0:
            input_array[current_index] = i
            counting_arr[i] -= 1
            current_index += 1

# Test Cases
arr = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
bubble_sort(arr)
selection_sort(arr)
insertion_sort(arr)
print(arr)
merge_sort(arr)
quick_sort(arr)
count_arr = [6, 5, 4, 6, 7, 1, 9, 3, 3, 1, 2, 6, 7, 3]
counting_sort(count_arr, 9)
print(count_arr)