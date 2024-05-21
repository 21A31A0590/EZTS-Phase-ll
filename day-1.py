#angram 
"""
a=input()
b=input()
d=0
if len(a)==len(b):
    for i in range(len(a)):
        c=a[i]
        if a.count(c)!=b.count(c):
            print("not anagram")
            break
        elif a.count(c)==b.count(c):
            d=1
if d==1:
    print("anagram")
"""
#isomorphic
"""
if len(s)==len(t):
for i in range(len(s)):
    if s.count(s[i])!=t.count(t[i]):
        return False
    elif s.count(s[i])==t.count(t[i]) and :
        d=1
if d==1:
    return True
"""
#color of chessboard
"""
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        s="aceg"
        t="bdfh"
        if coordinates[0] in s:
            if int(coordinates[1])%2==0:
                return True
            else:
                return False
        else:
            if int(coordinates[1])%2==0:
                return False
            else:
                return True
"""
#datastructures
#stackoperations
"""
class a:
    def __init__(self):
        self.l=[]
        self.size=5
    def pop(self):
        if (self.l)==0:
            print("empty")
        else:
            self.l.pop()
            print(self.l)
    def push(self,n):
        if self.l==self.size:
            print("full")
        else:
            self.l.append(n)
            print(self.l)
    def peek(self):
        if (self.l)==0:
            print("empty")
        else:
            print(self.l[-1])
ob=a()
ob.push(1)
ob.push(5)
ob.push(1)
ob.push(3)
ob.pop()
ob.peek()
"""
#stack problems
#postfix expression
"""
s=input()
l=[]
for i in range(len(s)):
    if s[i].isdigit():
        l.append(int(s[i]))
    else:
        a=int(l.pop())
        b=int(l.pop())
        if s[i]=="+":
            l.append(a+b)
        elif s[i]=="-":
            l.append(a-b)
        elif s[i]=="*":
            l.append(a*b)
        elif s[i]=="/":
            l.append(a/b)
print(l[0])
"""
#last element to delete
""" 
l=list(map(int,input().split()))
n=int(input())
c=1
while len(l)>1:
    for i in range(n):
        if c%2==0 and len(l)>1:
            l.pop(-1)
        elif len(l)>1:
            l.pop(0)
    c+=1
a=l.pop()
print(a)
"""