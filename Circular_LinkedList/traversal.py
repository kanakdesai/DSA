class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CricularList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        temp = self.head
        new_node.next = self.head

        if self.head is not None:
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
        else:
            new_node.next = new_node
        self.head = new_node

    def printList(self):
        temp = self.head
        while self.head is not None:
            print(temp.data)
            temp = temp.next
            if temp == self.head:
                break

cl = CricularList()
cl.push(1)
cl.push(2)
cl.push(3)
cl.push(4)
cl.push(5)
cl.push(6)
cl.printList()