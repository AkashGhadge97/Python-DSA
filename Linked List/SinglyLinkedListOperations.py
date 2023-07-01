# Class to create a new node
from random import randrange


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Class to create a Single Licked List
class LinkedList:

    # Create Empty linked list
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # Print the linked list
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result

    # Append a node at the end of the linked list
    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    # Insert a node at the beginning of the linked list
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    # Inserting a new node at given position
    def insert_at_given_position(self, value, position):
        new_node = Node(value)
        temp_node = self.head
        for _ in range(position-1):
            temp_node = temp_node.next
        new_node.next = temp_node.next
        temp_node.next = new_node
        self.length += 1


new_linked_list = LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)

new_linked_list.prepend(40)
new_linked_list.prepend(50)

new_linked_list.append(80)
print(new_linked_list.__str__())

new_linked_list.insert_at_given_position(100, 2)
print(new_linked_list.length)

print(new_linked_list.__str__())
