# Initialize class for Deque 
class Deque:
    # Only item we need is an empty list
    def __init__(self):
        self.items = []
    
    def getSize(self):
        return len(self.items)
    
    # Next 4 methods allow for the addition and removal of items on both sides of our list
    def addFront(self,item):
        self.items.append(item)
        
    def addRear(self,item):
        self.items.insert(0,item)
    
    def removeFront(self):
        return self.items.pop()
    
    def removeRear(self):
        return self.items.pop(0)
    
    def isEmpty(self):
        return len(self.items) == 0

# Creation of a random Deque item to test its methods
d = Deque()

# Should return True
print(d.isEmpty())
d.addRear(4)
d.addRear('Test')
d.addFront('Crest')
# Should return 3
print(d.getSize())
d.removeRear()
# Should now return 2
print(d.getSize())