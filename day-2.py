#linked list
"""
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def beg(self,data,next):
        self.data=data
        self.next=next
a=Node(1)
b=Node(2)
c=Node(3)
a.next=b
b.next=c
print(a.next.next.data)
"""
#automatic insertion in linked list
"""
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def beg(self,value):
        n=Node(value)
        if self.head==None:
            self.head=n
        else:
            n.next=self.head
            self.head=n
    def mid(self,value):
        n=Node(value)
        if self.head==None:
            self.head=n
        elif self.head.next==None:
            self.head.next=n
        else:
            a=self.listcount()
            a=a//2
            c=self.head
            d=1
            while d!=a:
                c=c.next
                d+=1
            n.next=c.next
            c.next=n
    def end(self,value):
        n=Node(value)
        if self.head==None:
            self.head=n
        else:
            c=self.head
            while(c.next!=None):
                c=c.next
            c.next=n
    def particular(self,value,y):
        n=Node(value)
        if self.head==None:
            self.head=n
        else:
            c=self.head
            while c.data!=y:
                c=c.next
            n.next=c.next
            c.next=n
    def listcount(self):
        c=self.head
        n=0
        while(c!=None):
            c=c.next
            n+=1
        return n
    def print(self):
        c=self.head
        while(c!=None):
            print(c.data,end="->")
            c=c.next
        print("null")
l=linkedlist()
l.beg(4)
l.beg(3)
l.beg(2)
l.beg(1)
l.print()
l.end(5)
l.end(6)
l.print()
l.particular(7,4)
l.print()
l.mid(9)
l.print()
print(l.listcount())
"""
#automatic deletion in linked list
"""
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def beg(self,value):
        n=Node(value)
        if self.head==None:
            self.head=n
        else:
            n.next=self.head
            self.head=n
    def end(self,value):
        n=Node(value)
        if self.head==None:
            self.head=n
        else:
            c=self.head
            while(c.next!=None):
                c=c.next
            c.next=n
    def delatbeg(self):
        if self.head==None:
            print("list is empty")
            return 0
        else:
            self.head=self.head.next
    def delatmid(self):
        if self.head==None:
            print("list is empty")
            return 0
        elif self.head.next==None:
            self.head=None
        else:
            a=self.listcount()
            a=a//2
            c=self.head
            d=1
            while d!=a:
                c=c.next
                d+=1
            c.next=c.next.next
    def delatparticular(self,value):
        if self.head==None:
            print("list is empty")
            return 0
        else:
            c=self.head
            while c.next.data!=value:
                c=c.next
            c.next=c.next.next
    def delatend(self):
        if self.head==None:
            print("list is empty")
            return 0
        else:
            c=self.head
            while c.next.next!=None:
                c=c.next
            c.next=None
    def listcount(self):
        c=self.head
        n=0
        while(c!=None):
            c=c.next
            n+=1
        return n
    def print(self):
        c=self.head
        while(c!=None):
            print(c.data,end="->")
            c=c.next
        print("null")
l=linkedlist()
l.beg(4)
l.beg(3)
l.beg(2)
l.beg(1)
l.print()
l.end(5)
l.end(6)
l.print()
l.delatbeg()
l.print()
l.delatmid()
l.print()
l.delatend()
l.print()
l.delatparticular(5)
l.print()
"""
#count of linked list
"""
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def beg(self,value):
        n=Node(value)
        if self.head==None:
            self.head=n
        else:
            n.next=self.head
            self.head=n
    def end(self,value):
        n=Node(value)
        if self.head==None:
            self.head=n
        else:
            c=self.head
            while(c.next!=None):
                c=c.next
            c.next=n
    def particular(self,value,y):
        n=Node(value)
        if self.head==None:
            self.head=n
        else:
            c=self.head
            while c.data!=y:
                c=c.next
            n.next=c.next
            c.next=n
    def listcount(self):
        c=self.head
        n=0
        while(c!=None):
            c=c.next
            n+=1
        print(n)
    def print(self):
        c=self.head
        while(c!=None):
            print(c.data,end="->")
            c=c.next
        print("null")
l=linkedlist()
l.beg(5)
l.beg(3)
l.beg(2)
l.beg(1)
l.print()
l.end(6)
l.end(7)
l.print()
l.particular(4,3)
l.print()
l.listcount()
"""
#fast slow pointer(linked list)
"""
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def beg(self,value):
        n=Node(value)
        if self.head==None:
            self.head=n
        else:
            n.next=self.head
            self.head=n
    def mid(self,value):
        n=Node(value)
        if self.head==None:
            self.head=n
        elif self.head.next==None:
            self.head.next=n
        else:
            a=self.listcount()
            a=a//2
            c=self.head
            d=1
            while d!=a:
                c=c.next
                d+=1
            n.next=c.next
            c.next=n
    def end(self,value):
        n=Node(value)
        if self.head==None:
            self.head=n
        else:
            c=self.head
            while(c.next!=None):
                c=c.next
            c.next=n
    def particular(self,value,y):
        n=Node(value)
        if self.head==None:
            self.head=n
        else:
            c=self.head
            while c.data!=y:
                c=c.next
            n.next=c.next
            c.next=n
    def pointer(self,value):
        n=Node(value)
        if self.head==None:
            self.head=n
        elif self.head.next==None:
            self.head.next=n
        else:
            fast=self.head
            slow=self.head
            while fast.next!=None and fast.next.next!=None:
                fast=fast.next.next
                slow=slow.next
            n.next=slow.next
            slow.next=n
    def delpointer(self):
        t=None
        slow=self.head
        fast=self.head
        while fast.next!=None and fast.next.next!=None:
            t=slow
            fast=fast.next.next
            slow=slow.next
        t.next=slow.next
    def listcount(self):
        c=self.head
        n=0
        while(c!=None):
            c=c.next
            n+=1
        return n
    def print(self):
        c=self.head
        while(c!=None):
            print(c.data,end="->")
            c=c.next
        print("null")
l=linkedlist()
l.beg(4)
l.beg(3)
l.beg(2)
l.beg(1)
l.print()
l.end(5)
l.end(6)
l.print()
l.particular(7,4)
l.print()
l.mid(9)
l.print()
print(l.listcount())
l.pointer(10)
l.print()
l.delpointer()
l.print()
"""
#reverse of linked list
"""
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def beg(self,value):
        n=Node(value)
        if self.head==None:
            self.head=n
        else:
            n.next=self.head
            self.head=n
    def mid(self,value):
        n=Node(value)
        if self.head==None:
            self.head=n
        elif self.head.next==None:
            self.head.next=n
        else:
            a=self.listcount()
            a=a//2
            c=self.head
            d=1
            while d!=a:
                c=c.next
                d+=1
            n.next=c.next
            c.next=n
    def end(self,value):
        n=Node(value)
        if self.head==None:
            self.head=n
        else:
            c=self.head
            while(c.next!=None):
                c=c.next
            c.next=n
    def particular(self,value,y):
        n=Node(value)
        if self.head==None:
            self.head=n
        else:
            c=self.head
            while c.data!=y:
                c=c.next
            n.next=c.next
            c.next=n
    def reverse(self):
        c=self.head
        pre=None
        nex=None
        while c!=None:
            nex=c.next
            c.next=pre
            pre=c
            c=nex
        self.head=pre
    def listcount(self):
        c=self.head
        n=0
        while(c!=None):
            c=c.next
            n+=1
        return n
    def print(self):
        c=self.head
        while(c!=None):
            print(c.data,end="->")
            c=c.next
        print("null")
l=linkedlist()
l.beg(4)
l.beg(3)
l.beg(2)
l.beg(1)
l.print()
l.end(5)
l.end(6)
l.print()
l.particular(7,4)
l.print()
l.mid(9)
l.print()
print(l.listcount())
l.reverse()
l.print()
"""
#overall program
"""
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def beg(self,value): #insertion at beggining
        n=Node(value)
        if self.head==None:
            self.head=n
        else:
            n.next=self.head
            self.head=n
    def mid(self,value): #insertion at middle
        n=Node(value)
        if self.head==None:
            self.head=n
        elif self.head.next==None:
            self.head.next=n
        else:
            a=self.listcount()
            a=a//2
            c=self.head
            d=1
            while d!=a:
                c=c.next
                d+=1
            n.next=c.next
            c.next=n
    def end(self,value): #insertion at end
        n=Node(value)
        if self.head==None:
            self.head=n
        else:
            c=self.head
            while(c.next!=None):
                c=c.next
            c.next=n
    def particular(self,value,y): #insertion at particular element
        n=Node(value)
        if self.head==None:
            self.head=n
        else:
            c=self.head
            while c.data!=y:
                c=c.next
            n.next=c.next
            c.next=n
    def pointer(self,value): #insertion using fast slow pointer
        n=Node(value)
        if self.head==None:
            self.head=n
        elif self.head.next==None:
            self.head.next=n
        else:
            fast=self.head
            slow=self.head
            while fast.next!=None and fast.next.next!=None:
                fast=fast.next.next
                slow=slow.next
            n.next=slow.next
            slow.next=n
    def delatbeg(self): #deletion at beggining
        if self.head==None:
            print("list is empty")
            return 0
        else:
            self.head=self.head.next
    def delatmid(self): #deletion at middle
        if self.head==None:
            print("list is empty")
            return 0
        elif self.head.next==None:
            self.head=None
        else:
            a=self.listcount()
            a=a//2
            c=self.head
            d=1
            while d!=a:
                c=c.next
                d+=1
            c.next=c.next.next
    def delatend(self): #deletion at end
        if self.head==None:
            print("list is empty")
            return 0
        else:
            c=self.head
            while c.next.next!=None:
                c=c.next
            c.next=None
    def delatparticular(self,value): #deletion at particular element
        if self.head==None:
            print("list is empty")
            return 0
        else:
            c=self.head
            while c.next.data!=value:
                c=c.next
            c.next=c.next.next
    def delpointer(self): #insertion using fast slow pointer
        t=None
        slow=self.head
        fast=self.head
        while fast.next!=None and fast.next.next!=None:
            t=slow
            fast=fast.next.next
            slow=slow.next
        t.next=slow.next
    def reverse(self): #reverse of a linked list
        c=self.head
        pre=None
        nex=None
        while c!=None:
            nex=c.next
            c.next=pre
            pre=c
            c=nex
        self.head=pre
    def listcount(self): #count of linked list
        c=self.head
        n=0
        while(c!=None):
            c=c.next
            n+=1
        return n
    def print(self): #printing a linked list
        c=self.head
        while(c!=None):
            print(c.data,end="->")
            c=c.next
        print("null")
l=linkedlist()
l.beg(4)
l.beg(3)
l.beg(2)
l.beg(1)
l.print()
l.mid(8)
l.print()
l.end(5)
l.end(6)
l.particular(7,4)
l.print()
l.pointer(10)
l.print()
l.print()
l.delatbeg()
l.print()
l.delatmid()
l.print()
l.delatend()
l.print()
l.delatparticular(5)
l.print()
l.delpointer()
l.print()
l.reverse()
l.print()
print(l.count())
"""