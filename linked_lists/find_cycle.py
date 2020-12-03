class Node(object):
    def __init__(self,val):
        self.val=val
        self.next=None


def find_cycle(node):
    vis=[]
    while(node):
        if node not in vis:
            vis.append(node)
        else:
            print(vis)
            return True
        node=node.next
    print(vis)
    return False

def rev_linkedlist(node):
    prev=None
    cur=node
    next=None
    while cur:
        next=cur.next
        cur.next=prev
        prev=cur
        cur=next

def n_last_node(n,node):
    k=1
    c=0
    temp=node
    while temp:
        c+=1
        temp=temp.next
    while node.next:


        if c+1-n==k:
            return node.val
        k = k + 1
        node = node.next

    return  "Not found"



############

a = Node(1)
b = Node(2)
c = Node(3)
d= Node(4)

a.next = b
b.next = c
c.next= d
d.next=None
# Cycle Here!

print(n_last_node(1,a))

#print(find_cycle(a))
# rev_linkedlist(a)
# print(d.next.val)
# # CREATE NON CYCLE LIST
# x = Node(1)
# y = Node(2)
# z = Node(3)
#
# x.next = y
# y.next = z
# print(find_cycle(x))




