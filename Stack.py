# Initialize class for Stack
class Stack:
    # We only need an empty list
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    # This will add an item to the front of our Stack
    def push(self, item):
        self.items.append(item)
    
    # This will remove an item from the front of our Stack and return the Stack
    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]
    
    def getSize(self):
        return len(self.items)

# Create a Stack object to test our methods
s = Stack()

# Should return True
s.isEmpty()
s.push('Item 1')
s.push(6)
s.push('Stak')

# Should print 'Stak'
print(s.peek())

# Should return 3
print(s.getSize())

s.pop()
s.pop()
# Should return 1
print(s.getSize())

# Should return False
print(s.isEmpty())
s.pop()
print(s.isEmpty())

