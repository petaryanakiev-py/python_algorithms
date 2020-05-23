# the single unit in the linked list
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

# The linked list with elements itself
class LinkedList(object):
    def __init__(self, head = None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        current = self.head
        while position > 0 and current.next:
            current = current.next
            position -= 1
        return current

    def insert(self, new_element, position):
        if position == 0:
            new_element.next = self.head
            self.head = new_element
        else:
            current = self.head
            previous = None
            while position > 0:
                previous = current
                current = current.next
                position -= 1
            new_element.next = current
            previous.next = new_element

    def delete(self, value):
        current = self.head
        if current.value == value:
            self.head = current.next
        else:
            previous = None
            while current.next:
                previous = current
                current = current.next
                if current.value == value:
                    previous.next = current.next
                    current.next = None
                    break
    
    def size(self):
        current = self.head
        size = 0
        while current.next:
            size += 1
            current = current.next
        return size + 1

# Test Cases

e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

for i in range(ll.size()):
    print(ll.get_position(i).value)

print("\n")

ll.insert(e4,3)
for i in range(ll.size()):
    print(ll.get_position(i).value)

print("\n")

ll.delete(1)
for i in range(ll.size()):
    print(ll.get_position(i).value)