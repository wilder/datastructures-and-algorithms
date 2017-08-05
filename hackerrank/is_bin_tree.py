""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
import sys
def check(node, minv, maxv):  
    if not node:
        return True
    
    if node.data >= maxv or node.data <= minv:
        return False
    
    return check(node.left, minv, node.data) and check(node.right, node.data, maxv)

def check_binary_search_tree_(root):
    b = True
    if root:
        b = check(root.left, -sys.maxsize, root.data) and check(root.right, root.data, sys.maxsize) 
    return b
