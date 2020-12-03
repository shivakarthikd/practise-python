class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # This function prints contents of linked list
    # starting from head
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.val)
            temp = temp.next


class Solution:
    def mergeKLists(self, lists:ListNode) :
        l=list()

        for i in lists:
            temp=i.head
            while (temp):
                l.append(ListNode(temp.val))
                temp=temp.next
        for i in l.sort():
            print(i.val)




    # Code execution starts here
if __name__ == '__main__':
    # Start with the empty list
    ls=list()
    llist = LinkedList()

    llist.head = ListNode(1)
    second = ListNode(2)
    third = ListNode(3)

    llist.head.next = second   # Link first node with second
    second.next = third;  # Link second node with the third node
    ls.append(llist)
    llist1 = LinkedList()

    llist1.head = ListNode(1)
    second1 = ListNode(2)
    third1 = ListNode(3)

    llist1.head.next = second1 ;  # Link first node with second
    second1.next = third1
    ls.append(llist1)
    llist2 = LinkedList()

    llist2.head = ListNode(1)
    second2 = ListNode(2)
    third2 = ListNode(3)

    llist2.head.next = second2  # Link first node with second
    second2.next = third2
    ls.append(llist2)


    #llist.printList()
    #llist1.printList()
    #llist2.printList()
    sol=Solution()
    sol.mergeKLists(ls)