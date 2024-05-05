class Node:
    def __init__(self, data = None, next = None):
                 self.data = data
                 self.next = next


class Linked_list:
    def __init__(self, arr):  # by this method we create a link list from an array
        self.head = None
        self.size = len(arr)
        tail = None

        for data in arr:
            node = Node(data)

            # Check wheather a node is created or not before this
            if self.head == None:
                self.head = node
                tail = node
            else:
                tail.next = node
                tail = node


    # There are three case of insertion. 1) Front insertion 2) Middle insertion 3) End insertion
    def insert(self, data, index = None):
        #if index == None, that we have to insert the element at the end
        if index == None:
            temp = self.head

            while temp.next != None:
                temp = temp.next

            # After running this loop temp will be the last node
            new_node = Node(data)
            temp.next = new_node

        else:
            if index < 0 or index > self.size:
                print("Invalid index !!!")

            elif index == 0:
                node = Node(data, self.head)
                self.head = node

            else:
                it = 1
                previous  = self.head
                while it < index:
                    previous = previous.next
                    it += 1
                # At the end of the loop previous stores the previous node(index-1)

                node = Node(data, previous.next)
                previous.next = node


    #To remove
    def remove(self, index = None):
        #if index == None, that we have to remove the last element
        if index == None:
            iterator = self.head

            while iterator.next.next != None:
                iterator = iterator.next

            # After running this loop iterator will be the 2nd last node
            iterator.next = None

        else:
            if index < 0 or index >= self.size:
                print("Invalid index !!!")

            elif index == 0:
                self.head = self.head.next
            else:
                it = 1
                previous  = self.head
                while it < index:
                    previous = previous.next
                    it += 1
                # At the end of the loop previous stores the previous node(index-1)

                previous.next = previous.next.next



    #To reverse [Out of place]
    def reverse_outplace(self):
        iterator = self.head
        self.head = None

        while iterator != None:
            node = Node(iterator.data)

             # Check wheather a node created or not before this
            if self.head == None:
                self.head = node
            else:
                node.next = self.head
                self.head = node
            iterator = iterator.next



    #To reverse [In place]
    def reverse_inplace(self):
        iterator = self.head
        self.head = None

        while iterator != None:
            temp = iterator.next
            iterator.next = self.head
            self.head = iterator
            iterator = temp



    # To search
    def search(self, key):
        iterator = self.head

        while iterator != None:
            if iterator.data == key:
                return True
            iterator = iterator.next

        return False



    # TO sort (Using Selection Sort Algo)
    def sort(self):
        i = self.head

        while i != None:
            min_node = i
            j = i.next
            while j != None:
                if j.data < min_node.data:
                    min_node = j
                j = j.next

            i.data, min_node.data = min_node.data, i.data
            i = i.next



    # To print the data of link list
    def show_data(self):
        pointer = self.head

        while pointer != None:
            print(pointer.data, end = ' ')
            pointer = pointer.next
        print()



#===============================================================================
arr = [5, 7, 2, 8, 10]
l1 = Linked_list(arr)

# l1.insert(11, 4)
# l1.show_data()

# l1.remove(3)
# l1.show_data()

# l1.reverse_outplace()
# l1.show_data()

# l1.reverse_inplace()
# l1.show_data()

# print(l1.search(10))

# l1.sort()
# l1.show_data()
