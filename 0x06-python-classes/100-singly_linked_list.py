#!/usr/bin/python3

"""class that represents a node
to be used in a single linked list
"""


class Node:
    """node of a single linked list"""

    def __init__(self, data, next_node=None):
        """init the data and next_node of the node itself"""
        if type(data) != int:
            raise TypeError("data must be an integer")
        if next_node is None or isinstance(next_node, Node):
            self.__data = data
            self.__next_node = next_node
        else:
            raise TypeError("next_node must be a Node object")

    @property
    def data(self):
        """getter for the data field"""
        return self.__data

    @data.setter
    def data(self, value):
        """setter for the data field"""
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """getter for the next_node field"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setter for the next_node field"""
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


"""class that represents a single linked list that contains nodes"""


class SinglyLinkedList:
    """single linked list containing nodes"""

    def __str__(self):
        rtr = ""
        ptr = self.__head

        while ptr is not None:
            rtr += str(ptr.data)
            if ptr.next_node is not None:
                rtr += "\n"
            ptr = ptr.next_node
        return rtr

    def __init__(self):
        """init the head of the single linked list to None"""
        self.__head = None

    def sorted_insert(self, value):
        """inserts a new node in sorted order"""
        if type(value) != int:
            raise TypeError("data must be an integer")
        current = self.__head
        while current is not None:
            if current.data > value:
                break
            prev = current
            current = current.next_node
        new_node = Node(value, current)
        if current == self.__head:
            self.__head = new_node
        else:
            prev.next_node = new_node
