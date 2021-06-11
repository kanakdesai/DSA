class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


    def detect_loop(self):
        slow_p = self.head
        fast_p = self.head
        while(slow_p and fast_p and fast_p.next):
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                return True
            return False




    def count_occurance(self, key):
        count = 0
        temp = self.head
        while temp is not None:
            if temp.data == key:
                count += 1
            temp = temp.next

        return count

    def printFromLast(self, n):
        count = 0
        temp = self.head
        while temp is not None:
            count += 1
            temp = temp.next

        if n > count:
            print("Long")
            return
        temp = self.head
        for i in range(0, count-n):
            temp = temp.next

        print(temp.data)

# GETS THE MIDDLE NODE OF THE LINKED LIST
    def middle_node(self):
        count = 0
        temp = self.head
        if temp is None:
            print("cant find middle node")
            return
        while temp is not None:
            count = count+1
            temp = temp.next
        temp = self.head
        for i in range(0,round(count/2)):
            temp = temp.next

        print('the middle node is: '+str(temp.data))




    def pariwiseSwap(self):
        temp = self.head
        if temp is None or temp.next is None:
            return
        while(temp is not None and temp.next is not None):
            if temp.data == temp.next.data:
                temp = temp.next.next

            else:
                temp.data, temp.next.data = temp.next.data, temp.data
                temp = temp.next.next



    def swap_nodes(self,x,y):

        if x == y:
            return

        prevX = None
        currX = self.head
        while currX != None and currX.data != x:
            prevX = currX
            currX = currX.next


        prevY = None
        currY = self.head
        while currY != None and currY.data != y:
            prevY = currY
            currY = currY.next

        if currY == None or currX == None:
            return

        if prevX != None:
            prevX.next = currY
        else:
            self.head = currY


        if prevY != None:
            prevY.next = currX
        else:
            self.head = currX


    #swapping out the next of x and y
        temp = currX.next
        currX.next = currY.next
        currY.next = temp


    def search_element(self, key):
        current = self.head
        while current is not None:
            if current.data == key:
                return True
            current = current.next
        return False


    def Get_th(self,index):
        count = 0
        current = self.head
        while(current):
            if(count == index):
                return current.data
            count = count + 1
            current = current.next
        return False


#This is deleting the node with the help of the pointer of the previous node
    def delete_at(self, position):

        if self.head is None:
            return

        temp = self.head

        if position == 0:
            self.head = temp.next
            temp = None
            return

    #find previous node of the node to be deleted
        for i in range(position-1):
           temp = temp.next
           if temp is None:
               break


        if temp is None:
            return
        if temp.next is None:
            return

        next = temp.next.next

        temp.next = None
        temp.next = next

    def length_list(self):
        count = 0
        current = self.head
        while current is not None:
            current = current.next
            count += 1

        return count


#used to delete a node according to the data of the linked list
    def delete_Node(self, key):

        temp = self.head
        #delete the head of the list
        if(temp is not None):
            if temp.data == key:
                self.head = temp.next
                temp = None

        #deleting the node at a given point
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next
        temp = None

    def delete_list(self):
        current = self.head
        while current:
            prev = current.next
            del current.data
            current = prev



    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print("Should be in between the linked list")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node



    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return

        last = self.head

        while( last.next ):
            last = last.next

        last.next = new_node

    def printList(self):
        i = self.head
        while(i):
            print(i.data)
            i = i.next


if __name__ == '__main__':
    llist = LinkedList()
    llist.append(6)
    llist.push(6)
    llist.push(6)
    llist.push(7);
    llist.append(1);
    llist.append(4)
    llist.printList()
    print('the key from the back of the list is: \n')
    print(llist.count_occurance(6))
    print(llist.detect_loop())
    # llist.printFromLast(1)
    # llist.printFromLast(1)
    # llist.printFromLast(1)    # print("the list after par wise swap  is: \n")
    #
    # llist.pariwiseSwap()
    # llist.printList()
    # llist.insertAfter(llist.head.next, 8)
    # print('Created linked list is: ')
    # llist.printList()
    # print('\n')
    # # print(llist.search_element(6))
    # print(llist.Get_th(2))

    # print("the count of the list is: "+str( llist.length_list()))
    #
    # print("Deleting the linked list")
    # llist.delete_list()
    #
    # print("Link list deleted ")
