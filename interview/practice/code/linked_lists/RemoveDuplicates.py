"""
Requirement: Given a head node in a linked list,
this function will return the linked list with duplicates removed.
Implementation: We walk through the linked list and every time we find a value that is a duplicate
of the value before it, we remove it.
Complexity: O(n) T and O(1) S as we walk through the whole linked list removing duplicates.
We do not need extra space to accomplish this task.
"""
import copy


def remove(linked_list):
    copy_list = copy.deepcopy(linked_list)
    current = copy_list
    while current is not None:
        next_distinct = current.next
        while next_distinct is not None and next_distinct.value == current.value:
            next_distinct = next_distinct.next
        current.next = next_distinct
        current = next_distinct
    return copy_list
