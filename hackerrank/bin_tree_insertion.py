"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""

def insert(r,val):
    if not r:
        return Node(val)
    
    root = r
    while True:
        if val > r.data:
            if not r.right:
                r.right = Node(val)
                return root
            r = r.right

        else:
            if not r.left:
                r.left = Node(val)
                return root
            r = r.left
