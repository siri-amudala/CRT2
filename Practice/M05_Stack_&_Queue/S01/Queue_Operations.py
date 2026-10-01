class queue:
    def __init__(self):
        self.q = []
    def enqueue(self,val):
        self.q.append(val)
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.q.pop(0)
    def is_empty(self):
        return len(self.q)==0
    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.q[0]
    def size(self):
        return len(self.q)
qu=queue()
qu.enqueue(10)
qu.enqueue(20)
qu.enqueue(30)
print(qu.is_empty())
print(qu.peek())
print(qu.dequeue())
print(qu.size())

