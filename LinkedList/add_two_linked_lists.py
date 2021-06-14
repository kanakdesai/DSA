class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def add_two_lists(self, first, second):
        prev = None
        temp = None
        carry = 0

        while first is not None and second is not None:
            fdata = 0 if first is None else first.data
            sdata = 0 if second is None else second.data

            sum = carry + fdata + sdata

            carry = 1 if sum >= 10 else 0
            sum = sum % 10 if sum >= 10 else sum

# HERE THE SUM IS GETTING TRANSFERED INTO A NEW LINKED LIST
            temp = Node(sum)

            if self.head is None:
                self.head = temp
            else:
                prev.next = temp

            prev = temp
# HERE THE PREVIOUS NODE POINTERS ARE GETTING CHANGED TO THE NEXT ONES SO THAT THE NODE CAN BE CHANGED
            if first is not None:
                first = first.next
            if second is not None:
                second = second.next

        if carry > 0:
            temp.next = Node(carry)

    def print_linked_list(self):

        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next


first = LinkedList()
second = LinkedList()

first.push(9)
first.push(9)
first.push(9)

second.push(5)
second.push(5)
second.push(5)

first.print_linked_list()

print("the second linked list is: \n")
second.print_linked_list()

print('The linked list after adding is: \n')
third = LinkedList()
third.add_two_lists(first.head, second.head)
third.print_linked_list()
