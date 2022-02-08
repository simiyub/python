"""
Requirement: Given a linked list where each node points to the next node,
this function will return the linked list in reverse order
Implementation: Conceptually, a node is reversed when the next pointer points to the previous node.
However, as this is a singly linked list, we do not have a pointer to the previous node.
So we need to create one. We do this using a temporary node that we initialise to None
as we start traversing the linked list from head.
We also need to keep a reference to the next node after the current node because
if we move the next pointer of the current node to the previous node,
we would lose connection to the rest of the linked list.
Once we have these two temporary references in place,
we start moving our pointers along recursively until the current node is null
and at that point the linked list will be reversed.
Complexity: O(n) T O(1) S as we have to recursively traverse the whole linked list.
However, we do not use any additional space than that of the linked list.
"""


def reverse(head):
    previous = head
    current = head
    while current is not None:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
    return previous
