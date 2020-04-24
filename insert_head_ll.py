def insertNodeAtHead(llist, data):
    if llist==None:
        llist=node(data)
        return llist
    else:
        x=node(data)
        x.next=llist
        return x