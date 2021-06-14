class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class CircularList:
    def __init__(self):
        self.last = None
    def add_to_empty(self, data):
        if self.last != None:
            return self.last
        temp = Node(data)
        self.last = temp
        self.last.next = self.last
        return self.last

    def addBegin(self,data):

        if self.last == None:
            return self.add_to_empty(data)
        temp = Node(data)

        temp.next = self.last.next
        self.last.next = temp
        return self.last

    def addEnd(self, data):
        if self.last == None:
            return self.add_to_empty(data)
        temp = Node(data)

        temp.next = self.last.next
        self.last.next = temp

        return self.last
    def add_after(self, data, item):
        if self.last == None:
            return None
        temp = Node(data)
        p = self.last.next
        while p:
            if p.data == item:
                temp.next = p.next
                p.next = temp

                if p == self.last:
                    self.last = temp
                    return self.last
                else:
                    return self.last
            p = p.next
            if p == self.last.next:
                print('Not found in list')
                break

    def printList(self):
        temp = self.last
        while self.last is not None:
            print(temp.data)
            temp = temp.next
            if temp == self.last:
                break

cl = CircularList()
cl.add_to_empty(1)
cl.addBegin(2)
cl.addEnd(3)
cl.add_after(5,2)
cl.addEnd(5)
cl.addBegin(6)
cl.printList()

