import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        # add item to stack
        self.storage.add_to_tail(value)
        self.size += 1
    def pop(self):
        # remove item from stack (LIFO)
        if self.storage.length != 0: # should this be length? had tail
            self.size -= 1
            return self.storage.remove_from_tail()
        else:
            return None

    def len(self):
        # size of stack
        return self.size
