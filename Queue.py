# Initialize class for Queue
class Queue:
    # Only item we need is an empty list
    def __init__(self):
        self.items = []
    
    def getSize(self):
        return len(self.items)
    
    # Next 2 methods allow for addition of items to the back and removal from the front of our Queue
    def enqueue(self,item):
        self.items.insert(0,item)
    
    def dequeue(self):
        return self.items.pop()
    
    def isEmpty(self):
        return len(self.items) == 0

# Creation of a random Queue item to test its methods
q = Queue()

# Should return True
print(q.isEmpty())
q.enqueue('5')
q.enqueue(4)
q.enqueue('Bunny')
# Should return 3
print(q.getSize())
q.dequeue()
# Should return 2
print(q.getSize())
