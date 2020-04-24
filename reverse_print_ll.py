from linkedlist import node,SinglyLinkedList

def reversePrint(head):
    x=[]
    while(head.next!=None):
        x.append(head.data)
        head=head.next
    x.append(head.data)
    for i in x[::-1]:
        print(i)