import sys
class SetOfStacks :
    def __init__(self,n):
        self.array = []
        self.n =  n 
        self.stack = []
    
    def push(self,elem):
        if len(self.stack) = self.n :
            self.array.append(self.stack)
            self.stack = [elem]
        else :
            self.stack.append(elem)
    
    def pop(self):
        self.array.pop()
    
    def popAtindex(self,index):
        self.array[index].pop()