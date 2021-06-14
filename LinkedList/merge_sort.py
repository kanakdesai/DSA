class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def merge_sorted(self,head1, head2):
        temp = None
        if head1 is None:
            return head2
        if head2 is None:
            return head1
        if head1.data <= head2.data:
            temp = head1
            temp.next = self.merge_sorted(head1.next, head2)
        if head2.data <= head1.data:
            temp = head2
            temp.next = self.merge_sorted(head1, head2.next)
        return temp
    def merge_sort(self, h):
        if h == None or h.next == None:
            return h

        middle = self.get_middle(h)
        temp = middle.next
        middle.next = None
        # print("this is middle: "+str(middle.data))
        left = self.merge_sort(h)
        right = self.merge_sort(temp)

        final = self.merge_sorted(left, right)
        return final

    def get_middle(self, head):
        if head is None or head.next is None:
            return head
        fast = head
        slow = head
        while fast.next.next is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def push(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next
# def printList(head):
#     if head is None:
#         print(' ')
#         return
#     curr_node = head
#     while curr_node:
#         print(curr_node.data, end = " ")
#         curr_node = curr_node.next
#     print(' ')
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
ll3.merge_sort(ll.head)
# printList(ll.head)
ll.print_list()
