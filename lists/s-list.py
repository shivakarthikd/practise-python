
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def push(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def del_node(self,key):
        temp=self.head
        prev=temp
    def del_node_pos(self,pos):
        temp=self.head
        i=1
        prev=temp
        while(temp):
            if i==pos:
                break
            i=i+1
            prev=temp
            temp=temp.next
        if i==1:
            self.head = temp.next
            temp=None
            return
        elif i==pos:
            prev.next=temp.next
            temp=None
            return
        else:
            print("no position found,", "Node only has",i-1,"elements")


        while(temp):
            if temp.data==key:
                break
            prev=temp
            temp=temp.next
        if temp==prev:
            self.head=temp.next
            temp=None
            return
        elif temp:
            prev.next=temp.next
            temp=None
            return
        if temp is None:
            return "no key"

    def len_list(self,head):
        if head is None:
           return 0
        else:
            return 1+self.len_list(head.next)
    def get_len(self):
        return self.len_list(self.head)



llist= LinkedList()
temp1=llist.head
for i in range(10):
    llist.push(i)
llist2=LinkedList()

for i in range(6,12):
    llist2.push(i)
temp2=llist2.head

m_list=LinkedList()
temp=m_list
head=None
while temp1 and temp2:
    if temp1.data < temp2.data:
        temp.data=temp1.data
        temp1=temp1.next
    else:
        temp.data=temp2.data
        temp2=temp2.next

temp.del_node_pos(12)
# t=None
# for i in range(6):
#     n_node = Node(i)
#     n_node.next=t
#     t=n_node
#
# temp=llist.head
# while(temp):
#     print(temp.data)
#     temp=temp.next
#     # print("node new",n_node.data)
#     # n_node=n_node.next
# print(llist.get_len())
# llist.del_node_pos(3)
# print("after deleted")
# print(llist.get_len())
# temp1=llist.head
# while(temp1):
#     print(temp1.data)
#     temp1=temp1.next

