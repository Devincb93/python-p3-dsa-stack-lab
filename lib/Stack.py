class Stack:
    def __init__(self, items = None, limit = 100):
        if items is None:
            items = []
        self.items = items
        self.limit = limit

    def empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
        
        
    def push(self, item):
        if not self.full():  # Check if stack is full before pushing
            self.items.append(item)
        else:
            raise OverflowError("push to full stack")
        

    def pop(self):
        if not self.empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")
        

    def peek(self):
        if not self.empty():
            return self.items[-1]
        else:
            raise IndexError("peek from empty stack")
        
    
    def size(self):
        return len(self.items)
        

    def full(self):
        return len(self.items) == self.limit
            
        

    def search(self, target):
        for i, item in enumerate(self.items):
            if item == target:
                return i
        return self.items[-1]
        
