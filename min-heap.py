
class MinHeap(object):

    def __init__(self):
        self.heap = [0]
        self.size = 0

    def parent(self, pos):
        return pos // 2
    
    def left_child(self, pos):
        return pos * 2

    def right_child(self, pos):
        return (pos * 2) + 1

    def is_leaf(self, pos):
        return pos <= self.size and pos >= self.size // 2

    def swap(self, first_pos, second_pos):
        self.heap[first_pos], self.heap[second_pos] = self.heap[second_pos], self.heap[first_pos]

    def bubble_up(self, pos):
        while self.parent(pos) > 0:
            if self.heap[pos] < self.heap[self.parent(pos)]:
                self.swap(pos, self.parent(pos))
            pos = self.parent(pos)

    def insert(self, element):
        self.heap.append(element)
        self.size += 1
        self.bubble_up(self.size)

    def min_child(self, pos):
        if self.right_child(pos) > self.size:
            return self.left_child(pos)
        else:
            if self.heap[self.left_child(pos)] < self.heap[self.right_child(pos)]:
                return self.left_child(pos)
            return self.right_child(pos)

    def sink_down(self, pos):
        while self.left_child(pos) <= self.size:
            min_child = self.min_child(pos)
            if self.heap[pos] > self.heap[min_child]:
                self.swap(pos, min_child)
            pos = min_child

    def pop_min(self):
        returning_value = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.sink_down(1)
        return returning_value

    def heapify(self, list_elements):
        index = len(list_elements) // 2
        self.size = len(list_elements)
        self.heap = [0] + list_elements[:]
        while index > 0:
            self.sink_down(index)
            index -= 1

# Tests
if __name__ == "__main__":

    heap = MinHeap()
    heap.insert(4)
    heap.insert(12)
    heap.insert(5)
    print(heap.pop_min())
    print(heap.pop_min())