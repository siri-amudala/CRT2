'''
Double Linked List:
Dats store Node
Node 3 parts
1.Previous
2.Data
3.Next

Algorithm:
1.Create Node.
2.Insert the data into the node.
3.Generate the connection between the nodes.
4.Traverse all the nodes.

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
node1=Node(10)
node2=Node(20)
node3=Node(30)
node4=Node(40)

node1.next=node2
node2.prev=node1
node2.next=node3
node3.prev=node2
node3.next=node4
node4.prev=node3

def traverse():
    curr=node1
    while curr:
        print(curr.data,end="-> ")
        curr=curr.next
    print("None")
traverse()

def reverse_traverse():
        curr=node4
        while curr:
            print(curr.data,end="<- ")
            curr=curr.prev
        print("None")
reverse_traverse()
'''

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None 

def insert_begin(head,data):
    new_node=Node(data)
    new_node.next=head
    if head:
        head.prev=new_node
    return new_node

def insert_end(head,data):
    new_node=Node(data)
    if head is None:
        return new_node
    curr=head
    while curr.next:
        curr=curr.next
    curr.next=new_node
    new_node.prev=curr
    return head

def instertion_after(node,data):
    if node is None:
        print("Error")
        return
    new_node=Node(data)
    new_node.next=node.next
    new_node.prev=node
    if node.next:
        node.next.prev=new_node
    node.next=new_node
    return node

def insertion_before(node,data):
    if node is None:
        print("Error")
        return
    new_node=Node(data)
    new_node.prev=node.prev
    new_node.next=node.next
    if node.next:
        node.next.prev=new_node
    else:
        node.next=new_node
    return node

def traverse(head):
    curr=head
    while curr:
        print(curr.data,end="-> ")
        curr=curr.next
    print("None")

head=None

head=insert_begin(head,10)
head=insert_begin(head,30)
print("Insertion at the beginning:")
traverse(head)

head=insert_end(head,10)
print("Insertion at the end:")
traverse(head)

head=instertion_after(head.next,15)
print("Insertion after a node:")
traverse(head)



