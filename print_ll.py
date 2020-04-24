from linkedlist import node,SinglyLinkedList

def printLinkedList(head):
    while head.next!=None:
        head=head.next
        print(head.data)