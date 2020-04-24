def deleteNode(head, position):
    cur=head
    if position==0:
        head=head.next
        return head
    for i in range(position-1):
        cur=cur.next
    cur.next=cur.next.next
    return head