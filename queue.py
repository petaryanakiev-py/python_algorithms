class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

# Could be implemented with python list as well
class Queue(object):
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail
    
    def enqueue(self, new_element):
        new_element.next = None
        if self.head and not self.tail:
            self.tail = new_element
            self.head.next = new_element
        elif not self.head:
            self.head = self.tail = new_element
        else:
            last = self.tail
            last.next = new_element
            self.tail = new_element

    def dequeue(self):
        dequeued = self.head
        self.head = self.head.next
        dequeued.next = None
        return dequeued

    def peek(self):
        return self.head

# Test Cases
e1 = Element(9)
e2 = Element(3)

queue = Queue(e1)
queue.enqueue(e2)

print(queue.dequeue().value)
print(queue.dequeue().value)
# print(queue.dequeue().value)

storage = [12]
print(storage)