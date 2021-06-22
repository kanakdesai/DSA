class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularList:
    def __init__(self):
        self.last = None

    def push(self, data):
        new_node = Node(data)
        if self.last is None:
            self.last = new_node
            self.last.next = new_node
            return self.last
        new_node.next = self.last.next
        self.last.next = new_node
        return self.last

    def split(self, head1 , head2):
        temp = self.last
        fast = self.last
        slow = self.last
        while fast.next is not self.last and fast.next.next is not self.last:
            fast = self.last.next.next
            slow = self.last.next

        temp = head1.last.next
        slow = head1.last

        slow.next = head2.last.next
        fast = head2.last

        return head1 and head2



