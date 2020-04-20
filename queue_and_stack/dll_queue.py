import sys
sys.path.append('./Data-Structures/doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        # add an item to the back of the queue.
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        # remove and return an item from the front of the queue
        if self.storage.length != 0: # should be length or head is not None.
            self.size -= 1
            return self.storage.remove_from_head()
        else:
            return None

    def len(self):
        return self.size
