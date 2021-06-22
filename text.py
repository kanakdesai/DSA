class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularList:
    def __init__(self):
        self.last = None

    def add_in_empty(self, data):
        if self.last != None:
            return
        temp = Node(data)
        self.last = temp
        self.last.next = self.last
        return self.last

    def add_infront(self, data):
        if self.last == None:
            return self.add_in_empty(data)
        temp = Node(data)
        temp.next = self.last.next
        self.last.next = temp
        return self.last
    def add_after(self, data, key):
        if self.last == None:
            return
        temp = Node(data)
        p = self.last.next
        while p:
            if p.data == key:
                temp.next = p.next
                p.next = temp
                if p == self.last:
                    temp = self.last
                    return self.last
                else:
                    return self.last

            p = p.next
            if p == self.last.next:
                return print("The key was not found in the node: ")
    def split(self, head1 , head2):
        temp = self.last
        fast = self.last
        slow = self.last
        while fast.next.next is not self.last and fast.next is not self.last:
            fast = self.last.next.next
            slow = self.last.next

        temp = head1.last.next
        slow = head1.last

        slow.next = head2.last.next
        fast = head2.last

        # return head1 and head2
    def printList(self):
        temp = self.last
        while self.last is not None:
            print(temp.data)
            temp = temp.next
            if temp == self.last:
                break

cl = CircularList()
cl.add_in_empty(2)
cl.add_infront(3)
cl.add_infront(3)
cl.add_infront(3)
cl.add_infront(3)
cl.add_infront(3)
cl.printList()
cl1 = CircularList()
cl2 = CircularList()
cl.split(cl1, cl2)
cl1.printList()

