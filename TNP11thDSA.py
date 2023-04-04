#deletion in binary tree
'''class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(str(root.key) + "->",end="")
        inorder(root.right)
def insert(node,key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left= insert(node.left,key)
    else:
        node.right = insert(node.right,key)
    return node
def minValueNode(node):
    current = node
    while(current.left is not None):
        current = current.left
    return current

def deleteNode(root,key):
    if root is None:
        return root
    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif key > root.key:
        root.right = deleteNode(root.right,key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = deleteNode(root.right, temp.key)
    return root

root = None
root = insert(root,8)
root = insert(root,3)
root = insert(root,1)
root = insert(root,6)
root = insert(root,7)
root = insert(root,10)
root = insert(root,14)
root = insert(root,4)

print("Inorder traversal: ", end=" ")
inorder(root)
print("\nDelete 10")
root = deleteNode(root, 10)
inorder(root)
root = deleteNode(root, 8)
inorder(root)'''
#Queue  even and odd element:

'''class queue:
    def __init__(self,size):
        self.front=0
        self.rear=-1
        self.size=size
        self.elements=[None]*size
    def enqueue(self,data):
        if self.rear == self.size-1:
            print("Queue is full")
        else:
            self.rear+=1
            self.elements[self.rear]=int(data)
    def dequeue(self):
        if self.front>self.rear:
            print("Queue is empty")
            return
        else:
            value=self.elements[self.front]
            self.front+=1
            return value
    def display(self):
        for i in range(self.front,self.rear+1):
            print(self.elements[i])
    def count_ele(self):
        c=0
        for i in range(self.front,self.rear+1):
            c+=1
        return c
            
print("Enter the required size")
size=int(input())
q=queue(size)
list(map(q.enqueue,input().split()))

qo=queue(size)
qe=queue(size)
q.display()
print("length of queue: ",q.count_ele())
i=0
length=q.count_ele()
while i<length:
    n=q.dequeue()
    if n%2==0:
        qe.enqueue(n)
    else:
        qo.enqueue(n)
    i+=1
print("even queue")
qe.display()
print("Odd queue")
qo.display()'''
# merging of list
def listMerger(ll1,ll2,n):
    counter=1
    itr=ll1.headNode
    while(counter<n):
        counter+=1
        itr=itr.nextNode
    temp=itr.nextNode
    itr.nextNode=ll2.headNode
    itr2=ll2.headNode
    while itr2.nextNode!=None:
        itr2=itr2.nextNode
    itr2.nextNode=temp
    return ll1
    

class node:
    def __init__(self,data):
        self.data=data
        self.nextNode=None

class sLinkedList:
    def _init_(self):
        self.headNode=None
    
    def insertAtEnd(self,data):
        if self.headNode ==None:
            self.headNode=node(int(data))
            return
        itr=self.headNode
        while itr.nextNode !=None:
            itr=itr.nextNode
        itr.nextNode=node(int(data))
    
    def printList(self):
        itr=self.headNode
        while itr !=None:
            print(itr.data,end=" ")
            itr=itr.nextNode
        print()



llist1=sLinkedList()
llist2=sLinkedList()
list(map(llist1.insertAtEnd,input().split("->")))
list(map(llist2.insertAtEnd,input().split("->")))
llist1.printList()
llist2.printList()
n=int(input())
llist1=listMerger(llist1,llist2,n)
llist1.printList()
