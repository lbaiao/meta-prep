# https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem

def height(root):
    if root is None:
        return 0    
    if root.left is None and root.right is None:
        return 0
    left_height = 0
    right_height = 0
    if root.left != None:        
        left_height += 1 + height(root.left)
    if root.right != None:
        right_height += 1 + height(root.right)
    if left_height > right_height:
        return left_height
    else:
        return right_height
