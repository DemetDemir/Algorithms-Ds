#Linked List

class Node:

    """
    An object for storing a single node of a linked list.
    Models two attributes : data and the link to the next node of the list.
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data

"""
N1 = Node(10)
print(repr(N1))
N2 = Node(20)
print(repr(N2))
N1.next_node = N2
print(N1.next_node)
"""
class Linked_List:

    """
    Returns the number of nodes and Takes linear time O(n)
    Singly linked list
    """
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None
    
    def size(self):
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node
        return count

    def add(self, data):
        new_Node = Node(data)
        new_Node.next_node = self.head
        self.head = new_Node



l = Linked_List()
l.add(1)
l.add(2)
l.add(3)
print(l.size())
    
