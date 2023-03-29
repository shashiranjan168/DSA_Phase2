#STACK
'''class stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__top=-1

    def is_full(self):
        if self.__top==self.__max_size-1:
            return True
        return False
    def is_empty(self):
        if self.__top==-1:
            return True
        return False
    def push(self,data):
        if self.is_full():
            print("Stack is full")
        else:
            self.__top+=1
            self.__elements[self.__top]=data
    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            data=self.__elements[self.__top]
            self.__top-=1

            return data

    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            index=self.__top
            while index>=0:
                print(self.__elements[index])
                index-=1
    def get_max_size(self):
        return self.__max_size



ball_stack=stack(4)
print("Is stack Empty:",ball_stack.is_empty())
ball_stack.push(1)
ball_stack.push(2)
ball_stack.push(3)
ball_stack.display()
print("Is stack is full:",ball_stack.is_full())
print("The maximum size of stack is: ",ball_stack.get_max_size())
print("The element deleted is : ",ball_stack.pop())
ball_stack.display()'''

#queue
'''class queue:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__front=0
        self.__rear=-1
    def is_full(self):
        if self.__rear==self.__max_size-1:
            return True
        return False
    def is_empty(self):
        if self.__front>self.__rear:
            return True
        return False
    def enqueue(self,data):
        if self.is_full():
            print("Stack is full")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data
    def dequeue(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            data=self.__elements[self.__front]
            self.__front+=1
            return data

    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            for i in range(self.__front,self.__rear+1):
                print(self.__elements[i])
    def get_max_size(self):
        return self.__max_size
    
queue1=queue(10)
print("Is queue empty: ",queue1.is_empty())
queue1.enqueue(100)
queue1.enqueue(200)
queue1.enqueue(300)
queue1.enqueue(400)
queue1.enqueue(500)
print("Is queue full: ",queue1.is_full())
queue1.display()
print("deleted element: ",queue1.dequeue())
queue1.display()'''

# QUeue insert

'''class queue:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__front=0
        self.__rear=-1
    def is_full(self):
        if self.__rear==self.__max_size-1:
            return True
        return False
    def is_empty(self):
        if self.__front>self.__rear:
            return True
        return False
    def enqueue(self,data):
        if self.is_full():
            print("Stack is full")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data
    def dequeue(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            data=self.__elements[self.__front]
            self.__front+=1
            return data

    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            for i in range(self.__front,self.__rear+1):
                print(self.__elements[i])
    def get_max_size(self):
        return self.__max_size
queue1=queue(10)

queue1.enqueue(13983)
queue1.enqueue(10080)
queue1.enqueue(7113)
queue1.enqueue(2520)
queue1.enqueue(2500)

queue1.display()
s1=[10080,2520]
print (s1)'''
# another way

'''from queue import Queue
q1 = Queue()
q2= Queue()
l=list(map(int,input().split(",")))
for i in l:
    q1.put_nowait(i)
for i in range(q1.qsize()):
    temp=q1.get_nowait()
    if all(temp%i==0 for i in range(1,11)):
        q2.put_nowait(temp)
for i in range(q2.qsize()-1):
    print(q2.get_nowait(),end=",")
print(q2.get_nowait())'''

#another way

'''class queue:
    def __init__(s,max_size) -> None:
        s.__max_size=max_size
        s.__element=[None]*max_size
        s.__front=0
        s.__rare=-1
    def isfull(s):
        if(s.__rare==s._max_size-1):
            return True
        return False
    def isempty(s):
        if(s.__front>s._rare):
            return True
        return False
    def enqueue(s,val):
        if(s.isfull()):
            print("Queue is full")
        else:
            s.__rare+=1
            s.__element[s._rare]=val
            # print("inserted {} in the Queue".format(s._element[s.__rare]))
    def dqueue(s):
        if(s.isempty()):
            print("Queue is empty")
        else:
            x=s.__element[s._front]
            s.__element[s._front]=None
            s.__front+=1
            # print("Deleted {} in the Queue".format(x))
            return x
    def get_max_size(s):
        return s.__max_size
    def display(s):
        # print("The Queue elements are: ",end="")
        print(','.join([str(s._element[i]) for i in range(s.front,s._rare+1)]))
    def front(s):
        return s._element[s._front]
    
def evenly_number(q):
    size=q.get_max_size()
    q1=queue(size)
    while(size>0):
        x=q.dqueue()
        f=1
        for i in range(1,11):
            if(x%i!=0):
                f=0
                break
        if(f==1):
            q1.enqueue(x)
        size-=1
    return q1

a=int(input())
q1=queue(a)
l=[int(i) for i in input().split(",")]
for i in l:
    q1.enqueue(i)
q2=evenly_number(q1)
q2.display()'''

# two pointer  for 2 list
'''l1=list(input().split(","))
l2=list(input().split(","))
l=len(l1)
for i in range(l):
    for j in range(l):
        if i+j==l-1:
            if l2[j]=="None":
                print(l1[i],end=" ")
                break
            else:
                print(l1[i]+l2[j],end=" ")
                break'''
# 2 queue merging

'''class queues:
    def __init__(s,max_size) -> None:
        s.__max_size=max_size
        s.__element=[None]*max_size
        s.__front=0
        s.__rare=-1
    def isfull(s):
        if(s.__rare==s.__max_size-1):
            return True
        return False
    def isempty(s):
        if(s.__front>s.__rare):
            return True
        return False
    def enqueue(s,val):
        if(s.isfull()):
            print("Queue is full")
        else:
            s.__rare+=1
            s.__element[s.__rare]=val
            # print("inserted {} in the Queue".format(s._element[s._rare]))
    def dqueue(s):
        if(s.isempty()):
            print("Queue is empty")
        else:
            x=s.__element[s.__front]
            s.__element[s.__front]=None
            s.__front+=1
            # print("Deleted {} in the Queue".format(x))
            return x
    def get_max_size(s):
        return s.__max_size
    def display(s):
        # print("The Queue elements are: ",end="")
        print(','.join([str(s.__element[i]) for i in range(s.__front,s.__rare+1)]))
        print()
    def front(s):
        return s.__element[s.__front]

def merge(q1,q2):
    s1=q1.get_max_size()
    s2=q2.get_max_size()
    q=queues(s1+s2)
    if(s1>=s2):
        for i in range(s2):
            q.enqueue(q1.dqueue())
            q.enqueue(q2.dqueue())
        for i in range(s1-s2):
            q.enqueue(q1.dqueue())
    else:
        for i in range(s1):
            q.enqueue(q1.dqueue())
            q.enqueue(q2.dqueue())
        for i in range(s2-s1):
            q.enqueue(q2.dqueue())
    q.display()

n=int(input())
m=int(input())
q_int=queues(n)
q_char=queues(m)
l_int=[q_int.enqueue(int(i)) for i in input().split(',')]
l_char=[q_char.enqueue(i) for i in input().split(',')]
merge(q_int,q_char)'''

# ANOTHER WAY TO MERINGING QUEUE
class Queue:
    def __init__(self, max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0
        
    def is_full(self):
        if(self.__rear==self.__max_size-1):
            return True
        return False
    
    def is_empty(self):
        if(self.__front>self.__rear):
            return True
        return False
    
    def enqueue(self,data):
        if(self.is_full()):
            print("Queue is full!!!")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data
            
    def dequeue(self):
        if(self.is_empty()):
            print("Queue is empty!!!")
        else:
            data=self.__elements[self.__front]
            self.__front+=1
            return data
        
    def display(self):
        for index in range(self.__front,self.__rear+1):
            print(self.__elements[index],end=",")
        print()
    def get_max_size(self):
        return self.__max_size
    

l1=list(input().split(","))
l2=list(input().split(","))
q1=Queue(len(l1))
q2=Queue(len(l2))

for i in l1:
    q1.enqueue(i)
for j in l2:
    q2.enqueue(j)


q3=Queue(len(l1)+len(l2))
ctr=0
for i in range(len(l1)+len(l2)):t
    if i%2==0 and ctr<q1.get_max_size():
        q3.enqueue(q1.dequeue())
        ctr+=1
    else:
        q3.enqueue(q2.dequeue())
q3.display()
        
        
