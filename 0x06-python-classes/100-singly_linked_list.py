#!/usr/bin/python3
"""SinglyLinkedList module

This nodule contains class that define Node and SinglyLinkedList objects
as well as methods used for creating and handling this objects.

"""


class Node():
    """Defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initializes attributes of a Node object

        Args:
            data (int): value of the node
            next_node (Node): the next node
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        "get or set the data of the node"""
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """get or set the next node of the current node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if type(value) is Node or next_node is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")

class SinglyLinkedList:
    """Defines a singly linked list"""

    def __init__(self):
        """Initializes attributes for the SinglyLinkedList object"""
        self.__head = None

    def __str__(self):
        """Sets the print behaviour of the SinglyLinkedList object"""
        sll_str = ""
        node = self.__head

        if node is not None:
            while node is not None:
                sll_str += str(node.data) + "\n"
                node = node.next_node

        return sll_str[:-1]

    def sorted_insert(self, value):
        """Inserts a new value in a sorted manner

        Args:
            value (int): new value to inserted in the node
        """
        node = self.__head

        if node is None or self.__head.data >= value:
            self.__head = Node(value, self.__head)
        else:
            while node.next_node is not None and node.next_node.data < value:
                node = node.next_node
            node.next_node = Node(value, node.next_node)
