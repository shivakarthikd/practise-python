class StackObj():
    def __init__(self,val):
        self.data=val
        self.next=None


class Stack(object):
    def __init__(self):
        self.head=None
        self.n=0
    def isEmpty(self):
        return self.n==0
    def push(self,item):
        temp=self.head
        self.head=StackObj(item)
        self.head.next=temp
        self.n+=1
    def pop(self):
        temp=self.head.next
        self.head=None
        self.head=temp
        self.n-=1
    def peek(self):
        return self.head.data
    def size(self):
        return self.n

s_obj= Stack()
s_obj.push(1)
s_obj.push(3)
s_obj.push(3)
s_obj.push(4)
s_obj.push(9)
s_obj.pop()
print(s_obj.peek())
print(s_obj.size())
print(s_obj.isEmpty())

