def height(root):
    if not root:
        return -1
    lefth = height(root.left)
    righth = height(root.right)
    if lefth > righth:
        return lefth + 1
    return righth + 1
