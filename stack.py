class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

# Could be represented as Linked List as well
class Stack(object):
    def __init__(self, head = None):
        self.head = head

    def push(self, new_element):
        new_element.next = self.head
        self.head = new_element

    def pop(self):
        poped = self.head
        if self.head:
            self.head = self.head.next
            poped.next = None
        return poped

    def top(self):
        return self.head.value

    def empty(self):
        return self.head == None

# Test Cases
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a Stack
stack = Stack(e1)

# Test stack functionality
stack.push(e2)
stack.push(e3)
print (stack.pop().value)
print (stack.pop().value)
print (stack.pop().value)
print (stack.pop())
stack.push(e4)
print (stack.pop().value)