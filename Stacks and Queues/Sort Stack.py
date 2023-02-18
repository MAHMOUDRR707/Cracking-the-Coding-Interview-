import sys
class sortStack :
    def __init__(self):
        self.stack = []
    
    def push(self,elem):
        self.stack.append(elem)
        self.stack =  sorted(sef.stack,reverse =  True)

    def pop(self):
        self.stack.pop()
    def peek(self):
        return self.stack[-1]

