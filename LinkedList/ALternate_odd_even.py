class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next



    def rearrange_odd_even(self):
        odd=[]
        even=[]
        i = 1
        current = self.head
        while current:
            if current.data % 2 == 0 and i % 2 != 0:
                even.append(current)
            elif current.data % 2 != 0 and i % 2 == 0:
                odd.append(current)
            i = i + 1
            current = current.next
        while len(odd) != 0 and len(even) != 0:
            odd[-1].data, even[-1].data = even[-1].data, odd[-1].data
            odd.pop()
            even.pop()
        return current

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
ll.push(10)
ll.printList()
print('\n')
ll.rearrange_odd_even()
ll.printList()

