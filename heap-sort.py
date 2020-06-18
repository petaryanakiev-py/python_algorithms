from heapq import heappop, heappush

def heap_sort(array):
    heap_list = []
    for element in array:
        heappush(heap_list, element)

    ordered_array = []
    while heap_list:
        ordered_array.append(heappop(heap_list))

    return ordered_array

# Tests
array = [6, 8, 1, 9, 3, 22, 2, 12, 65]
print(heap_sort(array))