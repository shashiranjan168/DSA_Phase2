#REVERSE OF LINKED LIST
'''class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def revers(self):
        prev=None
        current-self.head
        while(current is not None):
            next=current.next
            current.next=prev
            prev=current
            current=next
        self.head=prev
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data,end=" ")
            temp=temp.next

llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)

print ("Given linked list")
llist.printList()
llist.reverse()
print ("\nReversed linked list")
llist.printList()'''
#DOuble linked list

'''class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_forward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> '
            itr = itr.next
        print(llstr)

    def print_backward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        last_node = self.get_last_node()
        itr = last_node
        llstr = ''
        while itr:
            llstr += itr.data + '-->'
            itr = itr.prev
        print("Link list in reverse: ", llstr)

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next

        return itr

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    def insert_at_begining(self, data):
        if self.head == None:
            node = Node(data, None, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None, itr)

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            self.head.prev = None
            return

        count = 0
        itr = self.head
        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break

            itr = itr.next
            count+=1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)



ll = DoublyLinkedList()
ll.insert_values(["banana","mango","grapes","orange"])
ll.print_forward()
print(ll.get_last_node().data)
ll.print_backward()
ll.insert_at_end("figs")
ll.print_forward()
ll.insert_at(0,"jackfruit")
ll.print_forward()
ll.insert_at(6,"dates")
ll.print_forward()
ll.insert_at(2,"kiwi")
ll.print_forward()'''

# insertion at endin double linked list

'''class Node:
    def __init__(self,value):
        self.previous=None
        self.data=value
        self.next=None
class DoublyLinkedList:
    def __init__(self):
        self.head=None
    def isEmpty(self):
        if self.head is None:
            return True
        return False
    def length(self):
        temp=self.head
        count=0
        while temp is not None:
            temp = temp.next
            count+=1
        return count
    def insertAtBeginning(self,value):
        new_node = Node(value)
        if self.isEmpty():
            self.head=new_node
        else:
            new_node.next = self.head
            self.head.previous= new_node
            self.head=new_node
    def insertAtEnd(self,value):
        new_node=Node(value)
        if self.isEmpty():
            self.insertAtBeginning(value)
        else:
            temp=self.head
            while temp.next is not None:
                temp = temp.next
            temp.next=new_node
            new_node.previous=temp
    def printLinkedList(self):
        temp = self.head
        while temp is not None:
            print(temp.data,sep=" ")
            temp=temp.next

x = DoublyLinkedList()
print(x.isEmpty())
x.insertAtEnd(5)
#x.printLinkedList()
x.insertAtEnd(15)
x.insertAtEnd(25)
x.insertAtEnd(35)
x.printLinkedList()
print("no of nodes",x.length())'''

#INSERTION at position, delete/insert from last and beginning

'''class Node:
    def __init__(self,value):
        self.previous=None
        self.data=value
        self.next=None
class DoublyLinkedList:
    def __init__(self):
        self.head=None
    def isEmpty(self):
        if self.head is None:
            return True
        return False
    def length(self):
        temp=self.head
        count=0
        while temp is not None:
            temp = temp.next
            count+=1
        return count
    def insertAtBeginning(self,value):
        new_node = Node(value)
        if self.isEmpty():
            self.head=new_node
        else:
            new_node.next = self.head
            self.head.previous= new_node
            self.head=new_node
    def insertAtEnd(self,value):
        new_node=Node(value)
        if self.isEmpty():
            self.insertAtBeginning(value)
        else:
            temp=self.head
            while temp.next is not None:
                temp = temp.next
            temp.next=new_node
            new_node.previous=temp
    def insertAtPosition(self,value,position):
        temp = self.head
        count = 0
        while temp is not None:
            if count==position-1:
                break
            count+=1
            temp = temp.next
        if position == 1:
            self.insertAtBeginning(value)
        elif temp is None:
            print("There are less than {}-1 elements in the linkedlist.Cannot insert at {} position.".format(position, position))
        elif temp.next is None:
            self.insertAtEnd(value)
        else:
            new_node = Node(value)
            new_node.next=temp.next
            new_node.previous=temp
            temp.next.previous=new_node
            temp.next = new_node
    def printLinkedList(self):
        temp = self.head
        while temp is not None:
            print(temp.data,sep=" ")
            temp=temp.next
    def deleteFromBeginning(self):
        if self.isEmpty():
            print("Linked List is empty.cannot delete elements.")
        elif self.head.next is None:
            self.head= None
        else:
            self.head=self.head.next
            self.head.previous=None
    def deleteFromLast(self):
        if self.isEmpty():
            print("Linked List is empty.cannot delete elements.")
        elif self.head.next is None:
            self.head= None
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.previous.next=None
            temp.previous=None
        
            

x = DoublyLinkedList()
print(x.isEmpty())
x.insertAtEnd(5)
#x.printLinkedList()
x.insertAtEnd(15)
x.insertAtEnd(25)
x.insertAtEnd(35)
x.printLinkedList()
print("no of nodes",x.length())
x.deleteFromBeginning()
print("insert at position 2 number 8")
x.insertAtPosition(8, 2)
x.printLinkedList()'''

# Postfix evaluation
class Evaluate:
    def __init__(self,capacity):
        self.top=-1
        self.capacity=capacity
        self.array=[]
    def isEmpty(self):
        return True if self.top==-1 else False
    def peek(self):
        return self.array[-1]
    def pop(self):
        if not self.isEmpty():
            self.top-=1
            return self.array.pop()
        else:
            return "$"
    def push(self,op):
        self.top += 1
        self.array.append(op)
    def evaluatePostfix(self,exp):
        for i in exp:
            if i.isdigit():
                self.push(i)
            else:
                val1 = self.pop()
                val2 = self.pop()
                self.push(str(eval(val2 + i + val1)))
                
        return int(self.pop())
    
if __name__=='__main__':
    exp = "231*+9-"
    obj = Evaluate(len(exp))
    print("postfix evaluation: %d" %(obj.evaluatePostfix(exp)))
