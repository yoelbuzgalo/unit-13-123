"""
Node class used to implement noce-based data structures.

@author GCCIS Faculty
"""
class Node:
    __slots__ = ["__value", "__next"]

    def __init__(self, value, next=None):
        self.__value = value
        self.__next = next

    def get_value(self):
        return self.__value

    def get_next(self):
        return self.__next

    def set_next(self, next):
        self.__next = next
    
    def __eq__(self, other):
        if type(self) == type(other):
            return self.__value == other.__value \
                and self.__next == other.__next
        else:
            return False

    def __str__(self):
        return str(self.__value)

def print_node(node):
    if node == None:
        return
    else:
        print(node.get_value(), end = '')
        print(', ', end = '')
        print_node(node.get_next())