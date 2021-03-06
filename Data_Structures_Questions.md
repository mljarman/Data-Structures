Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

1. What is the runtime complexity of `enqueue`? O(1) because memory is not contiguous so no shifting needs to take place.

2. What is the runtime complexity of `dequeue`? O(1) because memory is not contiguous so no shifting needs to take place.

3. What is the runtime complexity of `len`? O(n)? Need to iterate through linked list to see how many there are.

## Binary Search Tree

1. What is the runtime complexity of `insert`? O(log n) because we eliminate 1 side of the tree depending if its larger or smaller.

2. What is the runtime complexity of `contains`? O(log n) because we eliminate 1 side of the tree depending if its larger or smaller.

3. What is the runtime complexity of `get_max`? O(log n) because we eliminate 1 side of the tree depending if its larger or smaller.
## Heap

1. What is the runtime complexity of `_bubble_up`?

2. What is the runtime complexity of `_sift_down`?

3. What is the runtime complexity of `insert`?

4. What is the runtime complexity of `delete`?

5. What is the runtime complexity of `get_max`?

## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?

2. What is the runtime complexity of `ListNode.insert_before`?

3. What is the runtime complexity of `ListNode.delete`?

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?

5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?

6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?

7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?

9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?

10. What is the runtime complexity of `DoublyLinkedList.delete`?

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?
