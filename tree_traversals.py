# Inorder, Preorder and Postorder tree traversals.

from bst import Node,insert

def inorder(root): 
    if root: 
        inorder(root.left) 
        print(root.val) 
        inorder(root.right) 
  
def preorder(root):
	if root:
		print(root.val) 
		preorder(root.left)
		preorder(root.right) 


def postorder(root):
	if root:
		postorder(root.left)
		postorder(root.right)
		print(root.val) 


r = Node(50) 
insert(r,Node(30)) 
insert(r,Node(20)) 
insert(r,Node(40)) 
insert(r,Node(70)) 
insert(r,Node(60)) 
insert(r,Node(80)) 

# Uncomment to test
# inorder(r)
# print("*******")
# preorder(r)
# print("*******")
# postorder(r)