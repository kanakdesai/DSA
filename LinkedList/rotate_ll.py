class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def rotate_LL(self,k):
        if k == 0:
            return
        count = 1
        current = self.head
        while count < k and current is not None:
            current = current.next
            count = count + 1

        if current is None:
            return

        kthNode = current

        while current.next is not None:
            current = current.next

        current.next = self.head
        self.head = kthNode.next

        kthNode.next = None

    def push(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next


ll = LinkedList()
ll3 = LinkedList()
ll.push(48)
ll.push(33)
ll.push(5)
ll.push(8)
ll.push(22)
ll.push(7)
ll.push(6)
ll.push(1)
ll.print_list()
ll.rotate_LL(4)
print("the list after rotating is: \n")
ll.print_list()
