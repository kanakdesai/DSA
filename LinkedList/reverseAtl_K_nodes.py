class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def reverse_k(self, k):
        count = 0
        current = self.head
        prev = None
        while current and count < k:
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1
        self.head = prev

        if self.head is not None:
            self.head.next = current

        count = 0
        while current and count < k:
            current = current.next
            count +=1



    def length(self):
        count = 0
        temp = self.head
        while temp is not None:
            count += 1
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next
def reverse_k_nodes(head, k):
    prev = None
    current = head
    next = None
    count = 0
    while current and count< k:
        next = current.next
        current.next = prev
        prev = current
        current = next
        count = count + 1

    if head is not None:
        head.next = current

    count = 0
    while current and count < k+1:
        current = current.next
        count = count + 1

    if current is not None:
        current.next = reverse_k_nodes(current.next, k)
    return prev


ll = LinkedList()
ll.push(1)
ll.push(2)
ll.push(3)
ll.push(4)
ll.push(5)
ll.push(6)
ll.push(7)
ll.push(8)
ll.push(9)

ll.printList()
print('\n')


reverse_k_nodes(ll, 2)
ll.printList()