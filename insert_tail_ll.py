def insertNodeAtTail(head, data):
    if head==None:
        head=node(data)
        return head
    else:
        new_node=node(data)
        cur=head
        while(cur.next!=None):
            cur=cur.next
        cur.next=new_node
        return head