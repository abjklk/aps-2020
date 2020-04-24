def insertNodeAtPosition(head, data, position):
    cur=head
    for i in range(position-1):
        cur=cur.next
    new_node=node(data)
    new_node.next=cur.next
    cur.next=new_node
    return head