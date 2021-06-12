class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def merge2(self,head1 , head2):
        #this is a temp node created and all the nodes will be stored in the temp node itself
        temp = None
        if head1 is None:
            return head2
        if head2 is None:
            return head1
    # here it is checked which number from which linked list needs to be stored i.e which no is small will go first in temp
        if head1.data <= head2.data:
            temp = head1
            temp.next = self.merge2(head1.next, head2)

        else:
            temp = head2
            temp.next = self.merge2(head1, head2.next)
        return temp





    def push(self,x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

ll = LinkedList()
ll.push(48)
ll.push(33)
ll.push(22)
ll.push(1)
ll2 = LinkedList()
ll2.push(8)
ll2.push(7)
ll2.push(6)
ll2.push(5)
ll3 = LinkedList()
ll.merge2(ll.head,ll2.head)

ll.print_list()