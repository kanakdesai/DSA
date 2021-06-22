class Node:
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev
class LinkedList:
    def __init__(self):
        self.head = None
    #here we are adding the node infront of the DLL
    def push(self, new_data):
        new_node = Node(data=new_data)
        new_node.next = self.head
        new_node.prev = None

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

    def add_after(self, newdata, prev):
        if prev == None:
            return print("not available in the DLL")
        new_node = Node(data=newdata)
        new_node.next = prev.next
        prev.next = new_node
        new_node.prev = prev

        if new_node.next != None:
            new_node.next.prev = new_node
    def append(self, new_data):

        new_node = Node(data=new_data)
        last = self.head
        new_node.next = None
        if self.head is None:
            new_node = self.head
            new_node.prev = None
        while last.next is not None:
            last = last.next

        last.next = new_node
        new_node.prev = last

    def addAfter(self, node, new_data):
        if node is None:
            print("the given node cannot be none ")
            return

        new_node = Node(data=new_data)
        new_node.prev = node.prev
        node.prev = new_node

        new_node.next = node

        if new_node.prev != None:
            new_node.prev.next = new_node
        else:
            self.head = new_node
        return self.head

    def printList(self):
        if self.head is None:
            print("list is empty ")
            return
        temp = self.head
        while temp is not None:
            print(temp.data)
            last = temp
            temp = temp.next
        print('\n')
        while last is not None:
            print(last.data)
            last = last.prev
ll = LinkedList()
ll.push(1)
ll.push(2)
ll.push(3)
ll.push(4)
ll.push(5)
ll.append(6)
ll.printList()