class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def reverseGroup(self, head, k):
        if head == None:
            return
        next = None
        count = 0
        prev = None
        current = head
        while current is not None and count <= k:
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1

        if next is not None:
            head.next = self.reverseGroup(next, k)

        return prev

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
ll.push(1)
ll.push(2)
ll.push(3)
ll.push(4)
ll.print_list()

ll.head = ll.reverseGroup(ll.head,2)
ll.print_list()