from linkedlist import node,SinglyLinkedList

def compare_lists(llist1, llist2):
    if llist1==None or llist2==None:
        return 0
    while llist1.next!=None:
        if llist1.data!=llist2.data:
            return 0
            break
        llist1=llist1.next
        llist2=llist2.next
        if llist2==None:
            return 0
    if llist2.next!=None:
        return 0
    return 1
