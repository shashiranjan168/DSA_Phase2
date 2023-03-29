# LINKED LIST
'''class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class SLinkedList:
   def __init__(self):
      self.headval = None

list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
# Link first Node to second node
list1.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3
Traversing a Linked List
Singly linked lists can be traversed in only forward direction starting form the first data element. We simply print the value of the next data element by assigning the pointer of the next node to the current data element.

Example
class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class SLinkedList:
   def __init__(self):
      self.headval = None

   def listprint(self):
      printval = self.headval
      while printval is not None:
         print (printval.dataval)
         printval = printval.nextval

list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Link first Node to second node
list.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3

list.listprint()'''

#ANOTHER WAY

class Node:
    def __init__(self,data,next):
        self.data=data
        self.nxt=next
        
class linkedList:
    def _init_(self):
        self.head=None


    def insert_begining(self,data):   
        node=Node(data,self.head)
        self.head=node



    def insert_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        itr=self.head
        while itr.nxt:
            itr=itr.nxt

        itr.nxt=Node(data,None)

    def insert_values(self,lst):
        self.head=None
        for i in lst:
            self.insert_end(i)

    def get_len(self):
        c=0
        itr=self.head
        while itr:
            c+=1
            itr=itr.nxt
        return c
    def remove_at(self,index):
        if index<0 or index>=self.get_len():
            raise Exception("Not a vaild index")
        if index==0:
            self.head=self.head.nxt
            return
        c=0
        itr=self.head
        while itr:
            if c == index-1:
                itr.nxt=itr.nxt.nxt
                
            itr=itr.nxt
            c+=1
    def del_end(self):
        itr=self.head
        c=0
        while itr:
            if c==self.get_len()-2:
                itr.nxt=None
                return
            itr=itr.nxt
            c+=1
    def del_begining(self):
        self.head=self.head.nxt
        

    def insert_at(self,data,index):
        if index<0 or index>=self.get_len():
            raise Exception("Not a vaild index")
        if index==0:
            self.insert_begining(data)
            return
        c=0
        itr=self.head
        while itr:
            if c== index-1:
                node=Node(data,itr.nxt)
                itr.nxt=node

            itr=itr.nxt
            c+=1
        
            
    def print_list(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr=self.head
        llstr=''

        while itr:
            llstr+=str(itr.data)+"--->"
            itr=itr.nxt

            
        print(llstr)
        

ll=linkedList()
#ll.insert_begining(5)
#ll.insert_begining(7)
#ll.insert_end(8)
#ll.insert_end(9)
ll.insert_values([1,2,3,4])
print(ll.get_len())
ll.print_list()
ll.remove_at(2)
print(ll.get_len())
ll.print_list()
ll.insert_at(0,2)
ll.print_list()
ll.del_end()
ll.print_list()
ll.del_begining()
ll.print_list()
