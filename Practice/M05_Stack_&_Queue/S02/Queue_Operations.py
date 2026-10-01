# Queue implementation using front and rear pointers
class Queue:
    def __init__(self,size):
        self.size=size 
        self.front=-1
        self.rear=-1
        self.q=[None]*self.size
    def enqueue(self,val):
        if self.rear==self.size-1:
            return "Queue is Full"
        self.rear+=1
        self.q[self.rear]=val 
    def dequeue(self):
        if self.front==self.size-1:
            return "Queue is Empty"
        self.front+=1
        val=self.q[self.front]
        return val
    def display(self):
        if self.front==-1:
            print("Queue is empty")
            return 
        for i in range(self.front,self.rear+1):
            print(self.q[i],end="->")
        print()
q=Queue(5)
q.enqueue(110)
q.enqueue(290)
q.enqueue(306)
q.dequeue()
q.display()

#implementation of Queue using Linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None 
class Queue_LL:
    def __init__(self):
        self.front=None
        self.rear=None
    def enqueue(self,val):
        new_node=Node(val)
        if self.front is None:
            self.front=self.rear=new_node
            return 
        self.rear.next=new_node
        self.rear=new_node
    def dequeue(self):
        if self.front is None:
            return "Queue is Empty"
        val=self.front.data
        self.front=self.front.next
        if self.front is None:
            self.rear=None
        return val
    def display(self):
        temp=self.front
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print()
q=Queue_LL()
q.enqueue(90)
q.enqueue(64)
q.dequeue()
q.display()  

