from linkedlist import node,SinglyLinkedList

# Turtle Hare Method
def has_cycle(head):
    slow_p = head 
    fast_p = head 
    while(slow_p and fast_p and fast_p.next): 
        slow_p = slow_p.next
        fast_p = fast_p.next.next
        if slow_p == fast_p: 
            return 1
    return 0