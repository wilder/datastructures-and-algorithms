""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""

def check_left(prev, node):  
    if not node:
        return True
    
    if prev <= node.data:
        return False
    
    return check_left(node.data, node.left) and check_right(node.data, node.right)

def check_right(prev, node):
    if not node:
        return True
    
    if prev >= node.data:
        return False
    
    return check_left(node.data, node.left) and check_right(node.data, node.right)

def check_binary_search_tree_(root):
    b = True
    if root:
        b = check_left(root.data, root.left) and check_right(root.data, root.right)
        
    return b
