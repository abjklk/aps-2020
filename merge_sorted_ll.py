# merge function to merge 2 sorted linked lists

def merge(headA,headB):
	if (headA==None) && (headB==None):
	    return None
	if (headA!=None) && (headB==None):
	    return headA
	if (headA == None) && (headB!=None):
	    return headB
	if headA.data < headB.data:
	    headA.next = merge(headA.next, headB)
	elif headA.data > headB.data:
	    temp = headB
	    headB = headB.next
	    temp.next = headA
	    headA = temp
	    headA.next = merge(headA.next, headB);
	return headA
