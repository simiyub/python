"""
Requirement: This function takes a linked list and an integer value k.
The function will remove the node that is position k from the end of the linked list.
Implementation: We use two pointers separated by node count = k.
So when we get to the end of the linked list with the pointer that is ahead,
we know that the lagging pointer is pointing at the node that we want to remove.
So we point the previous node to the one after the one we are removing.
Complexity: O(k) T O(1) S as we traverse to the kth value that we need to remove.
"""


def remove(head, k):
    k_value = head.value
    counter = 1
    first = head
    second = head
    while counter <= k:
        second = second.next
        counter += 1
    if second is None:
        head.value = head.next.value
        head.next = head.next.next
        return k_value
    while second.next is not None:
        second = second.next
        first = first.next

    k_value = first.next.value
    first.next = first.next.next
    return k_value
