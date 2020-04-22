import sys
sys.path.append('./Data-Structures/doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.dll = DoublyLinkedList() # self.ordering = DoublyLinkedList()
        self.dict = dict() # self.storage = {}
        self.size = 0 # len(self.ordering)



    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # if key is in our cache:
        if key in self.dict:
            node = self.dict[key]
            self.dll.move_to_front(node)
            return node.value[1]
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # if key already exists, overwrite value and move to front
        if key in self.dict:
            self.dict[key].value = (key, value) # node.value = (key, value)
            node = self.dict[key]
            self.dll.move_to_front(node)
            return # nothing after this gets executed if relevant
        # if at max capacity, delete tail & add new
        elif self.dll.length == self.limit: # self.size == self.limit
            lru_key = self.dll.tail.value[0]
            del self.dict[lru_key]
            self.dll.remove_from_tail()
            self.size -= 1
        #  if new and not at max capacity, add to head (will skip deleting tail)
        self.dll.add_to_head((key, value))
        self.dict[key] = self.dll.head
        self.size += 1
