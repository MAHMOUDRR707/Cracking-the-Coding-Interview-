import sys
class stack :
    def __init__(self):
        self.array = []
    
    def push(self,elem):
        self.array.append(elem)
    
    def pop(self):
        elem = self.array.pop()
    
    def getMin(self):
        return min(self.array())
