from bst import Node,insert
from tree_traversals import inorder

def minValueNode(node): 
    current = node
    while(current.left is not None): 
        current = current.left  
    return current

def deleteNode(root, key): 
  
    # Case 1 
    if root is None: 
        return root  
  
    # Case 2 : left subtree 
    if key < root.val: 
        root.left = deleteNode(root.left, key) 
  
    # Case 3 : right subtree 
    elif(key > root.val): 
        root.right = deleteNode(root.right, key) 
  
    # Case 4 : This node
    else: 
          
        # Node with only one child or no child 
        if root.left is None : 
            temp = root.right  
            root = None 
            return temp  
              
        elif root.right is None : 
            temp = root.left  
            root = None
            return temp 
  
        # Node with two children: Get the inorder successor 
        # (smallest in the right subtree) 
        temp = minValueNode(root.right) 
  
        # Copy the inorder successor's content to this node 
        root.val = temp.val 
  
        # Delete the inorder successor 
        root.right = deleteNode(root.right , temp.val) 

    return root  

r = Node(50) 
insert(r,Node(30)) 
insert(r,Node(20)) 
insert(r,Node(40)) 
insert(r,Node(70)) 
insert(r,Node(60)) 
insert(r,Node(80))

# Uncomment to test
# inorder(r)
# print("*****")
# deleteNode(r,30)
# inorder(r)