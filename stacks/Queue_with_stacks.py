class Queue(object):
    def __init__(self):
        self.stack1=[]
        self.stack2=[]

    def enqueue(self,val):
        self.stack1.append(val)

    def dequeue(self):
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def isEmpty(self):
        return self.stack1==self.stack2==[]


q_obj=Queue()
q_obj.enqueue(3)
q_obj.enqueue(9)
q_obj.enqueue(7)
q_obj.enqueue(5)
print(q_obj.stack1,q_obj.stack2)
q_obj.dequeue()
print(q_obj.stack1,q_obj.stack2)
q_obj.dequeue()
q_obj.dequeue()
q_obj.dequeue()
print(q_obj.stack1,q_obj.stack2)
print(q_obj.isEmpty())
