#Remove alpha
'''class Node:
    def __init__(self,data,next):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

    def insert_end(self,data):
        if self.head is None:
            node=Node(data,None)
            self.head=node
            return
        
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)
            
    def print_list(self):
        itr=self.head
        llstr=""
        while itr:
            llstr+=str(itr.data)+"--->"
            itr=itr.next
        print(llstr)
    def remove_alpha(self):
        itr=self.head
        s=""
        while itr:
            if (itr.data == "/" or itr.data == "") and (itr.next.data =="/" or itr.next.data ==""):
                s+=" "
                itr=itr.next
            elif itr.data == "/" or itr.data == "*":
                s+=" "
            else:
                s+=itr.data
            itr=itr.next
        return s
                
            
ll=LinkedList()
list(map(ll.insert_end,input().split(",")))
ll.print_list()
print(ll.remove_alpha())'''
# Remove delete
'''class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        selected_node = self.headval
        while selected_node != None:
            print (selected_node.dataval)
            selected_node = selected_node.nextval
    
    def insertAtEnd(self,value):
        new_node=Node(value)
        if self.headval is None:
            self.headval=new_node
            return
        currentNode=self.headval
        while currentNode.nextval is not None:
            currentNode=currentNode.nextval
        currentNode.nextval=new_node
    
    def removeDuplicates(self):
        currentNode=self.headval
        while currentNode.nextval is not None:
            while currentNode.dataval==currentNode.nextval.dataval:
                currentNode.nextval=currentNode.nextval.nextval
            currentNode=currentNode.nextval
        



q1=SLinkedList()
list(map(q1.insertAtEnd,input().split()))
q1.listprint()
print("==========")
q1.removeDuplicates()
q1.listprint()'''
#Linear search in python
'''def linearSearch(array,n,x):
    
    #Going through array sequentially
    for i in range(0,n):
        if(array[i]==x):
            return i
    return -1
    
array = [2,4,0,1,9]
x = 1
n = len(array)
result = linearSearch(array, n, x)
if(result == -1):
    print("Element not found")
else:
    print("Element found at index: ",result)'''
#Binary search in python
'''def binarySearch(array,x,low,high):
    while low<= high:
        mid= low+(high-low)//2
        if array[mid]==x:
            return mid
        elif array[mid]<x:
            low=mid+1
        else:
            high=mid-1
    return -1
array=[3,4,5,6,7,8,9]
x=9
result=binarySearch(array,x,0,len(array)-1)
if result != -1:
    print("Element present at index"+str(result))
else:
    print("Not found")'''
# binary tree trversing
"""class Node:
    def __init__(self,item):
        self.left=None
        self.right=None
        self.val = item
        
def inorder(root):
    if root:
        inorder(root.left)
        print(str(root.val) + "->",end='')
        inorder(root.right)
            
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.val) + "->",end='')
    
def preorder(root):
    if root:
        print(str(root.val) + "->",end='')
        preorder(root.left)
        preorder(root.right)
            
root = Node(1)

root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Inorder traversal")
inorder(root)
print("\nPostorder traversal")
postorder(root)
print("\nPreorder traversal")
preorder(root)"""

# binary search tree
"""class Node:
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
inorder(root)"""
# train question
class Compartment:
    def __init__(self, name, total_seating, num_passengers):
        self.name = name
        self.total_seating = total_seating
        self.num_passengers = num_passengers

class Train:
    def __init__(self, train_name, compartment_list):
        self.train_name = train_name
        self.compartment_list = compartment_list

    def get_train_name(self):
        return self.train_name

    def get_compartment_list(self):
        return self.compartment_list

    def count_compartments(self):
        return len(self.compartment_list)

    def check_vacancy(self):
        count = 0
        for compartment in self.compartment_list:
            if compartment.num_passengers < 0.5 * compartment.total_seating:
                count += 1
        return count

compartment_list = [Compartment("A", 100, 50), Compartment("B", 80, 30), Compartment("C", 120, 70), Compartment("D", 90, 40)]
train = Train("Express", compartment_list)

print(train.count_compartments())  
print(train.check_vacancy())
