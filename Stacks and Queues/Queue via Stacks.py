import sys
class MyQueue :
    def __init__(self):
        self.stack = []
    
    def push(self,elem):
        self.stack.append(elem)

    def pop(self):
        self.stack.pop(0)

q = MyQueue()
q.push(5)
q.push(7)
q.push(8)
q.pop()
