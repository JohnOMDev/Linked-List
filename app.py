"""A python Linked list function to a sequence"""
class Node:

    """Making a Node Class"""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """ Making a Linked Class """

    def __init__(self):
        self.head = None

    def append(self, data):
        """ Appending linked list function """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def reverse(self):
        """ reverse linked list function """
        def reversing(current, prev):
            if not current:
                return prev
            nächste = current.next
            current.next = prev
            prev = current
            current = nächste
            return reversing(current, prev)
        self.head = reversing(current=self.head, prev=None)

    def print_ll(self):
        """ function to print the linked list """
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

if __name__ == '__main__':
    ll = LinkedList()
    def sequence():
        """ defining a fibonaci like sequence: yield 0 to start with and then,
        i will now be 1, and j will also be 1, (0 + 1) """
        i, j = 0, 1
        while True:
            yield i
            i, j = j, i + j

    for index, sequence_number in zip(range(100), sequence()):
        #Looping through 100 sequence elements
        ll.append(sequence_number)
    ll.reverse()
    ll.print_ll()
    